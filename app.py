import datetime
import streamlit as st
import pandas as pd
import time
import plotly.graph_objects as go

######################################################################################################
				#Configuraaaes da pagina
######################################################################################################

st.set_page_config(
    page_title="Alarmes Control Tower",
	layout="wide",
    initial_sidebar_state="collapsed",
)

m = st.markdown("""
<style>
div.stButton > button:first-child{
    width: 100%;
    font-size: 18px;
}

label.css-qrbaxs{
    font-size: 18px;
}

p{
    font-size: 18px;
}

h1{
    text-align: center;
}

div.block-container{
    padding-top: 1rem;
}

div.streamlit-expanderHeader{
    width: 100%;
    font-size: 18px;
}
</style>""", unsafe_allow_html=True) #    font-weight: bold;

# Ajustando fuso
tz = pytz.timezone('America/Bahia')

######################################################################################################
# sidebar
######################################################################################################

telas = ['Alarmes', 'Parâmetros']
c1,c2 = st.sidebar.columns([1,1])
tela_selecionada = st.sidebar.radio('Selecione a tela', telas)
