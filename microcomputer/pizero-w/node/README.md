# Nodejs sample for the Zero W

Yes, the node version is slightly outdated. The official node website does not have binaries for nodejs past version 10.

## Install

`npm install`

## Develop

You can either develop on the Pi using command line tools, or on your machine with your IDE and upload it to the Pi with `scp`.

## Connecting the DHT22

The DHT22 has 3 ports: VCC, Data and GND

Connect the VCC to the 3.3v pin on the PI (pin 1)
Connect the GND to any ground pin on the PI (like pin 6)
Connect the Data to the GPIO 4 (pin 7)

When holding the board face up and the pins are on the right side, the pins are numbered from 1 to 40, left to right, down to bottom. Here are some of their functions:

Pin 1 and 17: 3.3v
Pin 2 and 4: 5v
Pin 6, 9, 14, 20, 25, 30, 34 and 39: GND
Pin 7: GPIO 4
Pin 11: GPIO 17

You can find the full pinout diagram easily on the internet


## Sample

The program connect to AWS IoT (given you provide the certificates, endpoint, and thing name), then reads a connected temperature/humidity sensor every few seconds. The exercise is to make a successful connection to AWS IoT and publish the data.
