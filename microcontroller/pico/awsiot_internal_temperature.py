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
PUBLISH_CHANNEL='temperature'

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

def read_internal_temp_sensor():
    """Read internal temperature sensor of RPi Pico W"""
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    return temperature

# Setup WiFi connection.
print("begin")
wlan = network.WLAN( network.STA_IF )
wlan.active( True )

check_wifi(wlan)
ssl_params=get_ssl_params()

# Connect to MQTT broker
mqtt = MQTTClient( CLIENT_ID, AWS_ENDPOINT, port = 8883, keepalive = 10000, ssl = True, ssl_params = ssl_params )
mqtt.connect()
print('Connected to AWS IoT')
print("Sending messages...")
while True:
    # Get temperature
    temperature=read_internal_temp_sensor()
    print('{"temp":%s}'% temperature)
    # TODO publish data to MQTT (don't forget to send in JSON) using mqtt.publish()
    time.sleep_ms(2000)