import paho.mqtt.publish as publish

class MQTTClient:

    _host          = "node02.myqtthub.com"
    _port          = 1883
    _clean_session = True
    _client_id     = ""
    _user_name     = ""  
    _password      = ""

    def __init__(self, client_id, user_name, password): 
        self._client_id = client_id 
        self._user_name = user_name 
        self._password = password 

    def on_publish(client,userdata,result):
        # Might write something useful here
        pass

    def send(topic, payload, qos=2, retain=False):
        publish.single(topic, payload, qos=, retain=retain, hostname = host, client_id = client_id, auth = {'username': user_name, 'password': password});
