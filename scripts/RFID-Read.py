#!/usr/bin/env python

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import MQTTClient
import time
from mfrc522 import SimpleMFRC522

mqttClient = MQTTClient('rfid', 'rfidsensor', 'rfid')

reader = SimpleMFRC522()

def read_rfid():
    try:      
               id,text = reader.read()
               print(id)
               print(text)
    finally:
               GPIO.cleanup()
    return id

while True:
    sensor_data = read_rfid()
    mqttClient.send("rbs/rfid-sensor", str(sensor_data))
    time.sleep(1)
