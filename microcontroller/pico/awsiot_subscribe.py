import machine
import network
import time
from mqtt import MQTTClient

#WIFI parameters
SSID = "{your_wifi_ssid}"
PASSWORD = "{your_wifi_password}"

# AWS endpoint parameters.
# Should be different for each device can be anything
CLIENT_ID = "{your_thing_name}"
AWS_ENDPOINT = b'{your_iot_endpoint}'
SUBSCRIBED_CHANNEL='led'

def get_ssl_params():
    """ Get ssl parameters for MQTT"""
    # These keys must be in der format the keys
    # downloaded from AWS website in pem format
    keyfile = '/private.der'
    with open(keyfile, 'rb') as f:
        key = f.read()
    certfile = "/certificate.der"
    with open(certfile, 'rb') as f:
        cert = f.read()    
    ssl_params = {'key': key,'cert': cert, 'server_side': False}
    return ssl_params

def mqtt_callback(topic, msg):
    """ Callback function for received messages"""
    print("received data:")
    print("topic: %s message: %s" %(topic, msg))
    if topic==b'led':
        # on pico w in is connected to wireless chip so led code must adept to it
        led = machine.Pin("LED", machine.Pin.OUT)
        if msg==b'on':
            led.on()
        elif msg==b'off':
            led.off()
        else:
            print("I dont know what to do with %s" % msg)
          
  
def check_wifi(wlan):
    """Wait for connection"""
    while not wlan.isconnected():
        time.sleep_ms(500)
        print("... trying to connect to WIFI")
        wlan.connect( SSID, PASSWORD )
        if not wlan.isconnected():
            print("not connected to wifi")
        if wlan.isconnected():
            print("connected to wifi")

# Setup WiFi connection.
print("begin")
wlan = network.WLAN( network.STA_IF )
wlan.active( True )

check_wifi(wlan)
ssl_params=get_ssl_params()

# Connect to MQTT broker.
mqtt = MQTTClient( CLIENT_ID, AWS_ENDPOINT, port = 8883, keepalive = 10000, ssl = True, ssl_params = ssl_params )
mqtt.set_callback(mqtt_callback)
mqtt.connect()
print('Connected to AWS IoT')
# Subscribe to our led channel for led commands
# you will only receive messages from subscribed channels
mqtt.subscribe(SUBSCRIBED_CHANNEL)

print("Subscribed to channel %s, waiting for messages..." % SUBSCRIBED_CHANNEL)
while True:
    #Check for messages from MQTT
    mqtt.check_msg()
    time.sleep(1)