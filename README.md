# IoT26-HW04 - Raspberry Pi Flask GPIO Web Server

## 1. Objective

This assignment is to create a web server on Raspberry Pi using Flask and control two LEDs through GPIO pins.

## 2. Hardware

- Raspberry Pi
- Breadboard
- 2 LEDs
- 2 resistors
- Jumper wires
- PC or laptop

## 3. Software

- Raspberry Pi OS
- Python 3
- Flask
- RPi.GPIO

## 4. Project Description

In this project, Raspberry Pi works as a standalone web server.

A Flask web application was created to control two GPIO pins.  
When the user clicks the ON or OFF button on the web page, the corresponding LED connected to the Raspberry Pi GPIO pin turns on or off.

## 5. GPIO Pin Setup

The project used two GPIO pins.

- GPIO 23: LED 1
- GPIO 24: LED 2
- GND: connected to the short leg of each LED

Each LED was connected with a resistor in series to protect the LED and GPIO pin.

## 6. Circuit Connection

The LEDs were connected to Raspberry Pi GPIO pins through resistors.

<img width="3024" height="4032" alt="HW4_circuit" src="https://github.com/user-attachments/assets/e8d868b4-97c9-48c6-965d-b887497f9568" />


## 7. Flask Server

The Flask server was executed on Raspberry Pi.
<img width="1438" height="863" alt="HW4" src="https://github.com/user-attachments/assets/31c41b0a-1180-4089-909e-55f2bf53e5d2" />


## 8. Result


https://github.com/user-attachments/assets/9ca9888e-7ba2-4da0-88a5-f01e4f5afdc4
