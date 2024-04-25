from machine import Pin
import dht
import network
import time

from mqtt import MQTTClient

#WIFI parameters
SSID = "{your wifi ssid}" # <-- Modify this
PASSWORD = "{your wifi password}" # <-- Modify this

# AWS endpoint parameters.
# Should be different for each device can be anything
DEVICE_NAME = "{your device name}" # <-- Modify this
AWS_ENDPOINT = b'a1yyxsoszwfl05-ats.iot.us-east-1.amazonaws.com' # <-- Make sure this is right

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

# Connect to MQTT broker
mqtt = MQTTClient( DEVICE_NAME, AWS_ENDPOINT, port = 8883, keepalive = 10000, ssl = True, ssl_params = ssl_params )
mqtt.connect()
print('Connected to AWS IoT')
print("Sending messages...")

sensor = dht.DHT22(Pin(22))
topic = "$aws/rules/thing_data_rule/%s"% (DEVICE_NAME)

while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print('Temperature: %3.1f C' %temperature)
        print('Humidity: %3.1f %%' %humidity)
        print('Sending data to AWS IoT topic %s' %topic)
        mqtt.publish(topic, msg = b'{"temperature":%s,"humidity":%s}'% (temperature, humidity))
        time.sleep_ms(2000)
    except OSError as e:
        print('Failed to read sensor.')