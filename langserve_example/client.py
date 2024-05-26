import requests
import streamlit as st


def get_gemini_response(ip):
    response = requests.post("https://localhost:8000/askgemma/invoke",
                             json={'input': {'query': ip}}, verify=False)
    return response.json()['output']['content']


st.title("Langserve Demo")
input_text = st.text_input("Enter your query")

if input_text:
    st.write(get_gemini_response(input_text))

