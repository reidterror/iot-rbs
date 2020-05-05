import RPi.GPIO as GPIO
import time
import subprocess
import MQTTClient

Pin = 11
mqttClient = MQTTClient('movement', 'movementsensor', 'movement')

def read_movement():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Pin, GPIO.IN)        
    while True:
        i=GPIO.input(Pin
    )
        if i==0:                 
            print("Not Sensing Motion",i)
            time.sleep(0.1)
            return 0
        elif i==1:              
            print("Motion Detected",i)
            time.sleep(0.1)
            return 1

while True:
    sensor_data = read_movement()
    mqttClient.send("rbs/movement-sensor", str(sensor_data))
    time.sleep(2)
