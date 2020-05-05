#!/usr/bin/env python

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from MQTTClient import MQTTClient
import time
from mfrc522 import SimpleMFRC522

mqttClient = MQTTClient('rfid', 'rfidsensor', 'rfid')
room = 400

reader = SimpleMFRC522()

def read_rfid():
    print('[RFID] Waiting for Input')

    try:      
               id,text = reader.read()
               print(id)
               print(text)
    finally:
              GPIO.cleanup()
    return id

while True:
    sensor_data = read_rfid()
    mqttClient.send("rbs/rfid-sensor", str(sensor_data)+','+str(room))
    time.sleep(1)
