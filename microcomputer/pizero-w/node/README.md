# Nodejs sample for the Zero W

Yes, the node verrsion is slightly outdated. The official node website does not have binaries for nodejs past version 10.

## Install

`npm install`

## Develop

You can either develop on the Pi using command line tools, or on your machine with your IDE and upload it to the Pi with `scp`.

## Sample

The program connect to AWS IoT (given you provide the certificates, endpoint, and thing name), then reads a connected temperature/humidity sensor every few seconds. The exercise is to make a successful connection to AWS IoT and publish the data.
