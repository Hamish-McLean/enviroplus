import paho.mqtt.client as mqtt

MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"
 
def on_connect(client, userdata, flags, rc):
    ''' The callback for when the client receives a CONNACK response from the server.'''
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_PATH) # Renews subscriptions if connection lost.
 
def on_message(client, userdata, msg):
    '''The callback for when a PUBLISH message is received from the server.'''
    print(msg.topic+" "+str(msg.payload))
    # more callbacks, etc
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
