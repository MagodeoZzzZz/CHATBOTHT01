import streamlit as st
import requests
import json

# PON TU API KEY ENTRE COMILLAS
API_KEY = "AIzaSyDkvMT-2Tj12K6KAoL7clfVxFVQbAyv79w"  # Reemplaza con tu clave real

# URL con la API Key incluida
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# Función para hacer la consulta a Gemini
def responder_pregunta(pregunta):
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": pregunta}]}]}
    
    response = requests.post(URL, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        respuesta_json = response.json()
        try:
            respuesta_texto = respuesta_json["candidates"][0]["content"]["parts"][0]["text"]
            return respuesta_texto
        except (KeyError, IndexError):
            return "Error al procesar la respuesta de la API."
    else:
        return f"Error {response.status_code}: {response.text}"

# Título y descripción
st.title("Chef IA - Tu Asistente de Cocina 👩‍🍳")
st.write("¡Hola! ¿Qué receta o consejos necesitas hoy?🧐")

# Entrada del usuario (caja de texto)
pregunta = st.text_input("Escribe tu pregunta 👀:")

# Botón para enviar la pregunta
if st.button("Obtener respuesta"):
    if pregunta:
        respuesta = responder_pregunta(pregunta)
        st.write(f"**🤖Chef IA dice:** {respuesta}")
    else:
        st.write("Por favor, ingresa una pregunta.")


# Sidebar con título y descripción
st.sidebar.title("Chef IA 🤖")
st.sidebar.write("¡Bienvenido a Chef IA! Soy tu asistente personal de cocina, listo para ayudarte a descubrir nuevas recetas, consejos útiles de cocina y tiempos de cocción. ¿Estás buscando una receta en particular, necesitas saber cuánto tiempo se cocina tu plato favorito o quizás los ingredientes necesarios para tu comida? ¡Solo pregúntame y te ayudaré a crear la receta perfecta!")

