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


def perguntas():
    st.title('Perguntas e respostas')
    with st.expander('1. Existe alguma falha ou oportunidade de melhoria na forma como os dados estão sendo registrados?'):
        st.markdown("""
            * Dados faltantes \n
            * falta de padrão nas respostas (f/Feminino, ranges de idade e tempo de casa...)
        """)

    with st.expander('2. Esses dados já proveem algum tipo de insight? Quais?'):
        st.markdown("""
            
        """)

    with st.expander('3. No curto prazo, queremos criar uma associação das estatísticas de algumas das respostas com recomendações práticas do que fazer para empresa. O quão difícil seria fazer isso? Qual seria o caminho?'):
        st.markdown("""
            
        """)

    with st.expander('4. Qual a estrutura ideal de banco de dados mais adequada para esse tipo de pesquisa e que permita, no futuro, aplicação de AI?'):
        st.markdown("""
            
        """)

    with st.expander('5. Quais as aplicações mais adequadas que devemos utilizar nesse est;agio para evitar retrabalho no futuro?'):
        st.markdown("""
            
        """)

    with st.expander('6. Que caminho você seguiria para criar um dashboard para utilização interna e externa com estes dados? Qual ferramenta utilizaria e como faria o desenvolvimento?'):
        st.markdown("""
            
        """)



######################################################################################################
# sidebar
######################################################################################################

telas = ['Dashboard', 'Perguntas']
c1,c2 = st.sidebar.columns([1,1])
tela_selecionada = st.sidebar.radio('Selecione uma opção', telas)

if __name__ == '__main__':
    if tela_selecionada == 'Perguntas':
        perguntas()

