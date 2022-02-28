#!/usr/bin/python3
import MLX90614
import paho.mqtt.client as mqtt
import time


MQTT_SERVER = "tower.finstafl.net"
MQTT_PATH = "sensor/"
MQTT_CLIENT = "CloudSensor"
DELAY = 30

sensor = MLX90614.MLX90614()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    run = True
    while run:
        ambTemp = str(round( sensor.get_amb_temp() ))
        objTemp = str(round( sensor.get_obj_temp() ))

        client.publish( MQTT_PATH + "ambient/" + ambTemp )
        client.publish( MQTT_PATH + "object/" + objTemp )
        print( "published...." )

        time.sleep( DELAY )


client = mqtt.Client( client_id = MQTT_CLIENT, protocol = mqtt.MQTTv31 )
client.username_pw_set("mqtt","digidic2")
client.on_connect = on_connect
client.connect( MQTT_SERVER, 1883, 60)



