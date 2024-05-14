import streamlit as st
import paho.mqtt.client as mqtt

# Configuración de MQTT
MQTT_SERVER = "broker.mqttdashboard.com"
MQTT_PORT = 1883
MQTT_TOPIC_DATA = "NataliaSensor"
MQTT_TOPIC_CONTROL = "NataliaActuador"

def on_message(client, userdata, message):
    # Procesa los mensajes recibidos
    payload = message.payload.decode("utf-8")
    # Aquí puedes procesar y mostrar los datos recibidos en Streamlit

def send_control_command(command):
    # Envía comandos de control al ESP32
    client.publish(MQTT_TOPIC_CONTROL, command)

# Configurar el cliente MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_SERVER, MQTT_PORT)
client.subscribe(MQTT_TOPIC_DATA)

# Iniciar el bucle de MQTT
client.loop_start()

# Aquí puedes crear tu interfaz de usuario con Streamlit
# Por ejemplo, botones para enviar comandos al ESP32

# Ejemplo de botón para enviar un comando al ESP32
if st.button("Encender LED"):
    send_control_command("ON_LED")

# Ejemplo de visualización de datos recibidos
# Aquí podrías mostrar gráficos, tablas, etc.
