# iot-demo-samples
Just code templates for IoT devices for a demo

## Microcomputers

Microcomputers are full computers that run an OS (generally Linux). The difference with normal computers is that they generally have input and output pins (GPIO, or General purpose input-output, ports). These input pins allow them to read data from  real-world devices and the output pins allow them to act on real-world devices. They also have far fewer resources than normal computers.

See [here](microcomputer/pizero-w/node/README.md)

## Microcontrollers

Microcontrollers are single-threaded. They just do one thing: run the code given to them. There is generally no OS. They have much, much less resources.

### Pico W

The Pico is an open-source board developped by Raspberry Pi. It has a dual-core ARM processor with 264 kB internal RAM, and 2MB of onboard flash memory. The 'W' version has a wireless chip that supports the 2.4GHz. At the time of writing, it costs less than 10$. All specs [here](https://www.raspberrypi.com/products/raspberry-pi-pico/).

Contrary to most microcontrollers that support only C/C++ development, the Pico also supports Python development. See [here](microcontroller/pico-w/python/README.md)
