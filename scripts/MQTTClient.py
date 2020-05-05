import paho.mqtt.publish as publish

class MQTTClient:
    def __init__(self, client_id, user_name, password): 
        self._host = "node02.myqtthub.com"
        self._port = 1883
        self._clean_session = True
        self._client_id = client_id 
        self._user_name = user_name 
        self._password = password 

    def on_publish(client,userdata,result):
        # Might write something useful here
        pass

    def send(self, topic, payload, qos=2, retain=False):
        publish.single(topic, payload, qos = qos, retain = retain, hostname = self._host, client_id = self._client_id, auth = {'username': self._user_name, 'password': self._password});
