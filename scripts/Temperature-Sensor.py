import RPi.GPIO as io 
import time
import subprocess
import MQTTClient
from sense_hat import SenseHat

sense = SenseHat()
mqttClient = MQTTClient('temp', 'tempsensor', 'temp')

def read_temp():
    temp_c = sense.get_temperature()
    cpu_temp = subprocess.check_output("vcgencmd measure_temp", shell=True)
    array = str(cpu_temp).split("=")
    array2 = array[1].split("'")

    cpu_tempc = float(array2[0])
    cpu_tempc = float("{0:.2f}".format(cpu_tempc))

    temp_calibrated_c = round(temp_c - ((cpu_tempc - temp_c)))

    print(temp_calibrated_c)
    return temp_calibrated_c

while True:
    sensor_data = read_temp()
    mqttClient.send("rbs/temp-sensor", str(sensor_data))
    time.sleep(60)
