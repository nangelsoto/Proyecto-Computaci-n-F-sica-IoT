import streamlit as st
import paho.mqtt.client as paho

# Título de la aplicación
st.title("Control de Temperatura")

# Slider para seleccionar la temperatura
temperatura = st.slider("Selecciona la temperatura (°C)", min_value=0, max_value=100, value=25)

# Botón para enviar la temperatura seleccionada
if st.button("Enviar Temperatura"):
    # Conexión MQTT
    mqtt_server = "broker.mqttdashboard.com"
    mqtt_topic = "NataliaTemperatura"
    
    # Envío del mensaje
    publish.single(mqtt_topic, temperatura, hostname=mqtt_server)

    # Confirmación de envío
    st.success(f"Temperatura {temperatura} enviada correctamente.")
