#!/usr/bin/python3
import MLX90614
import paho.mqtt.publish as publish
import time
import json
import time

MQTT_SERVER = "tower.finstafl.net"
# MQTT_SERVER = "10.1.1.25"
MQTT_PATH = "CloudSensor/temperatures"
MQTT_CLIENT = "CloudSensor"
DELAY = 30

sensor = MLX90614.MLX90614()

def doLoop():

    run = True
    while run:
        ambTemp = str(round( sensor.get_amb_temp() ))
        objTemp = str(round( sensor.get_obj_temp() ))

        # msg = '{' + """ambient:""" + ambTemp + ',' + """object:""" + objTemp + '}'
        msg = {
            "ambient": ambTemp,
            "object":  objTemp
        }

        try:
            publish.single( topic = MQTT_PATH, payload = json.dumps(msg),
    			hostname = MQTT_SERVER, client_id=MQTT_CLIENT, 
    			auth = {'username':"mqtt",'password':"digidic2" } )
            print (time.strftime("%c"), ambTemp, objTemp)
            time.sleep( DELAY )
        except ConnectionRefusedError:
            logging.info("ConnectionRefusedError")
doLoop()
