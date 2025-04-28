import streamlit as st
import requests

BASE_URL = "https://parallelum.com.br/fipe/api/v1/carros"

st.title("Consulta FIPE Simples 🚗")

marcas = requests.get(f"{BASE_URL}/marcas").json()
marca = st.selectbox("Escolha a marca", marcas, format_func=lambda x: x["nome"])

if marca:
    modelos = requests.get(f"{BASE_URL}/marcas/{marca['codigo']}/modelos").json()
    modelo = st.selectbox("Escolha o modelo", modelos["modelos"], format_func=lambda x: x["nome"])

    if modelo:
        anos = requests.get(f"{BASE_URL}/marcas/{marca['codigo']}/modelos/{modelo['codigo']}/anos").json()
        ano = st.selectbox("Escolha o ano", anos, format_func=lambda x: x["nome"])

  
        if ano:
            url = f"{BASE_URL}/marcas/{marca['codigo']}/modelos/{modelo['codigo']}/anos/{ano['codigo']}"
            resposta = requests.get(url).json()
            st.subheader("Resultado:")
            st.write("Modelo:", resposta["Modelo"])
            st.write("Ano:", resposta["AnoModelo"])
            st.write("Combustível:", resposta["Combustivel"])
            st.write("Valor FIPE:", resposta["Valor"])