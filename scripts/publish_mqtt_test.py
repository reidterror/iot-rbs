# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

host          = "node02.myqtthub.com"
port          = 1883
clean_session = True
client_id     = "laptop"
user_name     = "frctl"  
password      = "Pedal123!"

def on_publish(client,userdata,result):
    print(result)
    pass

ret = publish.single("roombooker/topic", 'SQLITE-VERSION', qos=2, retain=False, hostname = host, client_id = client_id, auth = {'username': user_name, 'password': password});

publish.single("roombooker/test", "test", qos=2, retain=False, hostname = host, client_id = client_id, auth = {'username': user_name, 'password': password});
