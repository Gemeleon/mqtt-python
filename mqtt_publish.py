import paho.mqtt.client as mqtt
import time
import ssl
import sys

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("ERPX")
topic = "ERPX/ERPY/FACTURAX"

timestamp = 1571652685.0
erpx = "Igarle_98734jhkdfighjed"
erpy = "Proconsi_oasdguikjh34"
factura = "s987gsdofij34kjhkldfgl"


client.connect(mqttBroker)

while True:
    payload="{"
    payload+="\"Timestamp\": "+str(timestamp); payload+=", ";
    payload+="\"ERPX\": "+str(erpx); payload+=", ";
    payload+="\"ERPY\": "+str(erpy); payload+=", ";
    payload+="\"FACTURAX\": "+str(factura); payload+=", ";
    payload+="}"
    client.publish(topic, payload)
    print("Just published " + str(payload) + " to Topic TEMPERATURE")
    time.sleep(1)
