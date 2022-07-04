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
    df = pd.read_csv('data.csv', sep=',', encoding='latin1', )
    st.title('Perguntas e respostas')
    with st.expander('1. Existe alguma falha ou oportunidade de melhoria na forma como os dados estão sendo registrados?'):
        st.markdown("""
            * Alguns campos possuem dados faltantes impactando na análise dados e atrapalhando a utilização de modelos de machine learning (as linhas precisam ser deletadas ou preenchidas) \n
            * Há fálta de padrão nas respostas em alguns campos como gender, home_time e age_group. Em alguns casos dá pra tratar manualmente a informação (caso do gender), nos outros o ideal é corrigir nos formulários \n
            * Há dados de tempo em que as respostas mudam de unidade (parte em meses e parte em anos)
        """)
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write('Dados faltantes por colunas:')
            df_null = pd.DataFrame()
            df_null['Quantidade'] = df.isnull().sum()
            df_null = df_null[df_null['Quantidade'] > 0]
            df_null['%'] = (df_null['Quantidade'] / df.shape[0]) * 100
            df_null['%'] = df_null['%'].astype(int)
            st.dataframe(df_null)

    with st.expander('2. Esses dados já proveem algum tipo de insight? Quais?'):
        st.markdown("""
            * Dashboard
        """)

    with st.expander('3. No curto prazo, queremos criar uma associação das estatísticas de algumas das respostas com recomendações práticas do que fazer para empresa. O quão difícil seria fazer isso? Qual seria o caminho?'):
        st.markdown("""
            
        """)

    with st.expander('4. Qual a estrutura ideal de banco de dados mais adequada para esse tipo de pesquisa e que permita, no futuro, aplicação de AI?'):
        st.markdown("""
            A escolha do banco depende muito do tipo de uso que daremos para os dados, há algumas perguntas importantes a serem respondidas, como: \n
            * Quem vai consumir esses dados? \n
            * Qual será a finalidade desses dados? \n
            \n
            Deixando um pouco essas lacunas de lado, podemos utilizar bancos de dados relacionais como PostgreSQL, MySQL entre outros. Neles podemos criar diversas tabelas de dados, inclusive separando por estágios, 
            como dados brutos (no formato que são coletados), dados processados (remoção de dados faltantes, tratamento de variáveis catgóricas) e dados analíticos (dados já formatados para uma dashboard).
        """)

    with st.expander('5. Quais as aplicações mais adequadas que devemos utilizar nesse estágio para evitar retrabalho no futuro?'):
        st.markdown("""
            Há diversas ferramentas que podem ser utilizadas e a definição delas depende bastante do contexto do que queremos entregar. Questões como onde iremos hospedar as aplicações (cloud ou on-premise) e o custo impactam diretamente nessa decisão.\n
            Apesar dessas icógnitas, há alguns pontos que podem ser considerados previamente, por exemplo utilizar Python como liguagem de programação por possuir vasta gama de bibliotecas voltadas para dados. Pode-se também se utlizar o Airflow para
            orquestar as aplicações, tendo em vista que pode rodar local ou na nuvem. Essa combinação de ferramentas já nos permite resolver uma grande gama de problemas relacionados a dados como a coleta, tratamento, análise estatística e 
            aplicação de modelos de machine learning.
        """)

    with st.expander('6. Que caminho você seguiria para criar um dashboard para utilização interna e externa com estes dados? Qual ferramenta utilizaria e como faria o desenvolvimento?'):
        st.markdown("""
            Hoje tenho mais prática no uso do Streamlit (framework Python que estou utilizando para essa aplicação), mas também já utilizei outras ferramentas como o Grafana. \n
            \n
            
        """)


def data_treatement():
    pass

######################################################################################################
# sidebar
######################################################################################################

telas = ['Dashboard', 'Perguntas']
c1,c2 = st.sidebar.columns([1,1])
tela_selecionada = st.sidebar.radio('Selecione uma opção', telas)

if __name__ == '__main__':
    if tela_selecionada == 'Perguntas':
        perguntas()

