#Gerenciará todas as operações relacionadas ao MQTT, como conectar ao broker, publicar mensagens e lidar com certificados.

# TODO: Define the MQTT client setup, publishing, and subscription logic.

import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_publish(client, userdata, mid):
    print("Message Published.")

def publish_model(json_data):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish

    # Configure TLS connection with appropriate cert files
    client.tls_set(certfile="path/to/cert.pem", keyfile="path/to/key.key")

    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    # Publish the data to the appropriate topic
    client.publish("mindsphere/topic/path", json_data)
    client.disconnect()
