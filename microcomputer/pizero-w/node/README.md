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

When holding the board face up and the pins are on the right side, here are some of the pin numbers and their function:

3.3v         -  1  2 - 5V

GPIO 2 (I2C) -  3  4 - 5V

GPIO 3 (I2C) -  5  6 - GND

GPIO 4       -  7  8 - GPIO 14, TXD (UART)

GND          -  9 10 - GPIO 15, RXD (UART)

GPIO 17      - 11 12 - GPIO 18, CLK

GPIO 27      - 13 14 - GND

GPIO 22      - 15 16 - GPIO 23

3.3v         - 17 18 - GPIO 24

etc.


## Sample

The program connect to AWS IoT (given you provide the certificates, endpoint, and thing name), then reads a connected temperature/humidity sensor every few seconds. The exercise is to make a successful connection to AWS IoT and publish the data.
