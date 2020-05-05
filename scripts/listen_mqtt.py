import sqlite3
import os
import paho.mqtt.client as mqtt

dirname = os.path.dirname(__file__)
host          = "node02.myqtthub.com"
port          = 1883
clean_session = True
client_id     = "lyubentemp@tutanota.com"
user_name     = "fractalow"  
password      = "Pedal123!"
 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    client.subscribe("roombooker/test")
    client.subscribe("roombooker/topic")
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    if str(msg.payload) == "b'SQLITE-VERSION'":
        try:
            sqliteConnection = sqlite3.connect(os.path.join(dirname, '../roombooker/db.sqlite3'))
            cursor = sqliteConnection.cursor()
            print("[SQLITE] Database created and Successfully Connected to SQLite")

            sqlite_select_Query = "select sqlite_version();"
            cursor.execute(sqlite_select_Query)
            record = cursor.fetchall()
            print("[SQLITE] SQLite Database Version is: ", record)
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
