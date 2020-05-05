import sqlite3
import os
from datetime import datetime
import paho.mqtt.client as mqtt

dirname = os.path.dirname(__file__)
host          = "node02.myqtthub.com"
port          = 1883
clean_session = True
client_id     = "server"
user_name     = "web-server"  
password      = "server"
 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    client.subscribe("rbs/temp-sensor")
    client.subscribe("rbs/rfid-sensor")
    client.subscribe("rbs/movement-sensor")
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if str(msg.topic) == "rbs/rfid-sensor":
        if str(msg.payload) != "b'Success'" and str(msg.payload) != "b'Failure'":
            data = str(msg.payload)[2:-1].split(',')
            try:
                sqliteConnection = sqlite3.connect(os.path.join(dirname, '../roombooker/db.sqlite3'))
                cursor = sqliteConnection.cursor()
                print("[SQLITE] Successfully Connected to SQLite")

                cursor.execute("select id from users_profile where rfid=?",  (data[0],))
                record = cursor.fetchone()

                cursor.execute("select calendarevent_id from users_profile_events where profile_id=?",  record)
                record = cursor.fetchone()

                cursor.execute("select start, end from fullcalendar_calendarevent where id=? and room=?",  (record[0], data[1]))
                record = cursor.fetchone()

                now = datetime.now()

                if now >= datetime.strptime(record[0], "%Y-%m-%d %H:%M:%S") and now < datetime.strptime(record[1], "%Y-%m-%d %H:%M:%S"):
                    client.publish('rbs/rfid-sensor', 'Success')
                else:
                    client.publish('rbs/rfid-sensor', 'Failure')

                cursor.close()

            except sqlite3.Error as error:
                print("[SQLITE] Error while connecting to sqlite", error)
            finally:
                if (sqliteConnection):
                    sqliteConnection.close()
                    print("[SQLITE] The SQLite connection is closed")

    if str(msg.payload) == "b'test'":
        print("Received message #2, do something else")
 
client = mqtt.Client (client_id = client_id, clean_session = clean_session)
client.username_pw_set (user_name, password)

client.on_connect = on_connect
client.on_message = on_message
 
client.connect(host, port, keepalive = 60)
 
client.loop_forever()
