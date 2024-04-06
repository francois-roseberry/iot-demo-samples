# MicroPython samples for the Pico W

MicroPython is a Python3 implementation for the Pico (and Pico W)

## Install MicroPython

Hold down the BOOTSEL button on the Pico while connecting it to the computer. It will appear as a USB drive. Download the MicroPython [firmware](https://micropython.org/download/), unzip it and drag-and-drop the .uf2 file on the Pico to flash the firmware. The Pico will reboot. Disconnect the Pico afterwards.

## Develop using VS Code

- Assuming VS Code is installed and up-to-date, install the necessary extensions:

```
code --install-extension ms-python.python
code --install-extension visualstudioexptteam.vscodeintellicode
code --install-extension ms-python.vscode-pylance
code --install-extension paulober.pico-w-go
```

- Connect your Pico to the computer (without holding down the BOOTSEL). The MicroPython installation will expose a virtual serial port over USB, which the vs code extension uses to auto-connect to the Pico. run > MicroPico > Configure Project command via Ctrl+Shift+P (or the equivalent on your platform) VS Code command palette. If all goes well and the Pico connected, you should see 'Pico connected' in the VS code status bar.
- The extension provides a terminal, which is a Python REPL running on the PICO.
- To run a Python file on the Pico, just select that file, right-click it, then select 'Run current file on Pico'.
- To stop it, click 'Stop' in the vs code status bar.
- Select 'Upload current file to Pico' to upload a non-runnable file (like an asset or library).

Note that these last 3 actions will be grayed off if the Pico isn't connected.

## Samples

- The `blink.py` toggles on and off the onboard LED every second, forever
- The `awsiot_subscribe.py` connects to the WIFI (be sure to replace the SSID/password in the file - you can also establish the connection beforehand using MicroPython device controller tab in vs code), then connects to AWS IoT (be sure to replace the iot endpoint in the file) using the certificates in `/certs` and subscribe to the `led` topic. If it receives an `on` message, it turns on the led, and turns it off when it receives an `off` message. It uses the file `mqtt.py` to do so. To run it, upload both .der files, the `mqtt.py` file, and run the `awsiot_subscribe` file on the Pico. You should see the output in the pico terminal in vs code.
- The `awsiot_temperature.py`, like the previous sample, also connects to the WIFI and to AWS IoT. But it reads the internal temperature sensor and then, as an exercise, you must publish that data to AWS IoT.
