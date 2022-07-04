import datetime
import streamlit as st
import pandas as pd
import time
import plotly.graph_objects as go
import plotly.figure_factory as ff
import scipy

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
    font-size: 16px;
}

h1{
    text-align: center;
}

div.block-container{
    padding-top: 1rem;
}

div.streamlit-expanderHeader{
    width: 100%;
    font-size: 22px;
    background-color: azure;
}
</style>""", unsafe_allow_html=True) #    font-weight: bold;


def perguntas():
    df = pd.read_csv('data.csv', sep=',' )

    st.title('Perguntas e respostas')
    with st.expander('1. Existe alguma falha ou oportunidade de melhoria na forma como os dados estão sendo registrados?'):
        st.markdown("""
            * Alguns campos possuem dados faltantes. Esses dados podem impactar a obtenção de insights valiosos e atrapalhar a utilização de modelos de machine learning (as linhas precisam ser deletadas ou preenchidas) \n
            * Há falta de padrão nas respostas em alguns campos como gender, home_time e age_group. Em alguns casos dá pra tratar manualmente a informação (caso do gender), nos outros o ideal é corrigir nos formulários \n
            * Há dados de tempo em que as respostas mudam de unidade (parte em meses e parte em anos)
        """)
        col1, col2 = st.columns([2,8])

        with col1:
            st.write('**Dados faltantes por colunas (em %):**')
            df_null = pd.DataFrame()
            df_null['Quantidade'] = df.isnull().sum()
            df_null = df_null[df_null['Quantidade'] > 0]
            df_null['%'] = (df_null['Quantidade'] / df.shape[0]) * 100
            df_null['%'] = df_null['%'].astype(int)
            st.dataframe(df_null)

        with col2:
            st.write('**Falta de padrão nas respostas:**')
            st.write(f'**Gender:** {df.gender.unique()}')
            st.write(f'**home_time:** {df.home_time.unique()}')
            st.write(f'**age_group:** {df.age_group.unique()}')
            st.write('Aqui temos ranges de idades diferentes, unidades diferentes e formas diferentes de passar a mesma informação (M e Masculino representando a mesma informação)')
            

    with st.expander('2. Esses dados já proveem algum tipo de insight? Quais?'):
        st.markdown("""
            Ao selecionar a opção dashboard, o usuário pode visualizar gráficos e informações que são relevantes para a empresa. \n
            **Gráficos:** \n
            * São do tipo histograma onde podemos ver a distribuição das respostas dos colaboradores para as questões levantadas divididas por pesquisa. Pelos critérios fornecidos,
            as empresas com melhor desempenho devem ter as respostas situadas nos valores 1 e 2 (mais a esquerda). \n
            **Resultado:** \n
            * Ótimo: 80% ou mais de respostas “concordo totalmente” e "concordo parcialmente". \n
            * Regular: entre 70% e 79% de respostas “concordo totalmente” "concordo parcialmente". \n
            * Péssimo: 69% ou menos de respostas “concordo totalmente" e "concordo parcialmente". \n
            **Análises:** \n
            * Engagement: As empresas A e C possuem maior engajamento (acima de 60% classificados como ótimo), já a empresa B possui 57% de avaliações como péssimo \n
            * Journey: Todas as empresas tiveram 50% ou mais de avaliações como péssimo \n
            * Culture: As empresas A e C foram avaliadas por mais de 60% dos funcionários ótimo, já a empresa B possui 72,2% de avaliações como péssimo \n
            * Attrition: A empresa A se destaca nesse ponto com 87,5% das avaliações como ótimo, a empresa C possui 47,1% e o destaque negativo fica por conta da empresa B onde mais de 60% avaliou como péssimo. \n
            **Considerações:** \n
            Essas informações vem de uma pequena amostra da base de dados e pode não refletir o comportamento geral das empresas. \n
            Os dados foram filtrados por empresa e por tipo de pesquisa, mas pode ser extendido para o gênero, cargo, líder, etc. São vários campos que podem ser filtrados e agrupados para gerar ainda mais insights. \n
        """)

    with st.expander('3. No curto prazo, queremos criar uma associação das estatísticas de algumas das respostas com recomendações práticas do que fazer para empresa. O quão difícil seria fazer isso? Qual seria o caminho?'):
        st.markdown("""
            Enxergo como uma possibilidade o seguinte caminho: \n
            * Coletar mais dados (quantidade e qualidade são importantes) \n
            * Identificar padrões nas respostas, monitorar as avaliações dos colaboradores no tempo, se elas tem melhorado ou não e capturar as red flags (exemplo: avaliações muito ruins) \n
            * Identificando esses casos, teremos que tomar ações coerentes com a regra de negócio da companhia (exemplo: ter alguma reunião com o colaborador ou com o líder) e traçar ações para tratar a questão
            Por exemplo, profissional pontuou muito baixo no tema "Risco de perda de talentos", são várias as possíveis causas para essa pontuação (o líder, salário, carga horária...)  \n
            * Gerar dados sobre essas ações e os resultados obtidos \n
            * Com esses dados dos resultados começar a gerar sugestões de ações para a empresa \n
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


def data_treatement() -> pd.DataFrame:
    df = pd.read_csv('data.csv', sep=',' )

    # df['answer'] = df['value'].map({1: 'Concordo totalmente',
    #                                 2: 'Concordo parcialmente',
    #                                 3: 'Não concordo nem discordo',
    #                                 4: 'Discordo parcialmente',
    #                                 5: 'Discordo totalmente',
    #                                 0: 'Não se aplica'})
    
    df['count'] = 1
    df.loc[(df['value'] == 1) | (df['value'] == 2) ,'answer'] = 1
    df.loc[(df['value'] != 1) & (df['value'] != 2) ,'answer'] = 0

    df.company_id = df['company_id'].str.replace('95dfed2b-32aa-46f1-935a-5c6356327bd6', 'Empresa A')
    df.company_id = df['company_id'].str.replace('95dfed2b-3371-42b3-8d58-b25285353bd4', 'Empresa B')
    df.company_id = df['company_id'].str.replace('95dfed2b-33fe-4765-965e-0177bb4a65aa', 'Empresa C')
    return df


def dashboard(df: pd.DataFrame) -> None:
    st.title('Dashboard')
    col1, col2, col3, col4 = st.columns(4)

    modo_vis = col1.selectbox('Modo de visualização:', ['Survey', 'Empresa'])

    if modo_vis == 'Survey':
        st.write('teste')
        empresa_survey = col2.selectbox('Survey:', list(df.survey.unique()))

        df_empresa_a = df[(df.survey == empresa_survey) & (df.company_id == 'Empresa A')]
        df_empresa_b = df[(df.survey == empresa_survey) & (df.company_id == 'Empresa B')]
        df_empresa_c = df[(df.survey == empresa_survey) & (df.company_id == 'Empresa C')]

        emp_a, emp_b, emp_c, legenda = st.columns(4)

        with emp_a:
            fig = go.Figure(data=[go.Histogram(x=df_empresa_a.value, histnorm='percent')])
            fig.update_layout(barmode='stack',
                #width=440, 
                height=250,
                margin=dict(b=5,	t=35,	l=0,	r=0),
                title='Empresa A',
                font=dict(size=15))

            fig.update_traces(textposition='inside', textfont_color='rgb(255,255,255)', textfont_size=20) #marker_color='rgb(55,83,109)',
            fig.update_yaxes(range = [0, 100])
            emp_a.plotly_chart(fig, use_container_width=True)

            df_analise_a = df_empresa_a[['employee', 'count', 'answer']].groupby(['employee']).sum()
            df_analise_a['percent'] = (df_analise_a['answer'] / df_analise_a['count']) * 100
            st.subheader('Avaliação dos funcionários')

            otimo = str(round(((df_analise_a.loc[df_analise_a['percent'] >= 80, 'percent'].shape[0])/df_analise_a.shape[0] * 100), 1)) + '%'
            st.write(f"**Ótimo:** {otimo}")

            regular = str(round(((df_analise_a.loc[(df_analise_a['percent'] < 80) & (df_analise_a['percent'] >= 70), 'percent'].shape[0])/df_analise_a.shape[0] * 100), 1)) + '%'
            st.write(f"**Regular:** {regular}")

            ruim = str(round(((df_analise_a.loc[df_analise_a['percent'] < 70, 'percent'].shape[0])/df_analise_a.shape[0] * 100), 1)) + '%'
            st.write(f"**Ruim:** {ruim}")

        with emp_b:
            fig = go.Figure(data=[go.Histogram(x=df_empresa_b.value, histnorm='percent')])
            fig.update_layout(barmode='stack',
                #width=440, 
                height=250,
                margin=dict(b=5,	t=35,	l=0,	r=0),
                title='Empresa B',
                font=dict(size=15))

            fig.update_traces(textposition='inside', textfont_color='rgb(255,255,255)', textfont_size=20) #marker_color='rgb(55,83,109)',
            fig.update_yaxes(range = [0, 100])
            emp_b.plotly_chart(fig, use_container_width=True)

            df_analise_b = df_empresa_b[['employee', 'count', 'answer']].groupby(['employee']).sum()
            df_analise_b['percent'] = (df_analise_b['answer'] / df_analise_b['count']) * 100
            st.subheader('Avaliação dos funcionários')

            otimo = str(round(((df_analise_b.loc[df_analise_b['percent'] >= 80, 'percent'].shape[0])/df_analise_b.shape[0] * 100), 1)) + '%'
            st.write(f"**Ótimo:** {otimo}")

            regular = str(round(((df_analise_b.loc[(df_analise_b['percent'] < 80) & (df_analise_b['percent'] >= 70), 'percent'].shape[0])/df_analise_b.shape[0] * 100), 1)) + '%'
            st.write(f"**Regular:** {regular}")

            ruim = str(round(((df_analise_b.loc[df_analise_b['percent'] < 70, 'percent'].shape[0])/df_analise_b.shape[0] * 100), 1)) + '%'
            st.write(f"**Ruim:** {ruim}")

        with emp_c:
            fig = go.Figure(data=[go.Histogram(x=df_empresa_c.value, histnorm='percent')])
            fig.update_layout(barmode='stack',
                #width=440, 
                height=250,
                margin=dict(b=5,	t=35,	l=0,	r=0),
                title='Empresa C',
                font=dict(size=15))

            fig.update_traces(textposition='inside', textfont_color='rgb(255,255,255)', textfont_size=20) #marker_color='rgb(55,83,109)',
            fig.update_yaxes(range = [0, 100])
            emp_c.plotly_chart(fig, use_container_width=True)

            df_analise_c = df_empresa_c[['employee', 'count', 'answer']].groupby(['employee']).sum()
            df_analise_c['percent'] = (df_analise_c['answer'] / df_analise_c['count']) * 100
            st.subheader('Avaliação dos funcionários')

            otimo = str(round(((df_analise_c.loc[df_analise_c['percent'] >= 80, 'percent'].shape[0])/df_analise_c.shape[0] * 100), 1)) + '%'
            st.write(f"**Ótimo:** {otimo}")

            regular = str(round(((df_analise_c.loc[(df_analise_c['percent'] < 80) & (df_analise_c['percent'] >= 70), 'percent'].shape[0])/df_analise_c.shape[0] * 100), 1)) + '%'
            st.write(f"**Regular:** {regular}")

            ruim = str(round(((df_analise_c.loc[df_analise_c['percent'] < 70, 'percent'].shape[0])/df_analise_c.shape[0] * 100), 1)) + '%'
            st.write(f"**Ruim:** {ruim}")

        legenda.write('''
**Legenda das respostas:** \n
1: 'Concordo totalmente' \n
2: 'Concordo parcialmente'\n
3: 'Não concordo nem discordo'\n
4: 'Discordo parcialmente'\n
5: 'Discordo totalmente'\n
0: 'Não se aplica'\n''')


def introducao():
    st.title('Introdução')
    st.subheader('Apresentação')
    st.write('Me chamo Mario Carvalho e sou um apaixonado por tecnologia e dados. Comecei minha trajetória no mercado de trabalho como engenheiro de controle e automação e desde 2020 utilizo Python e dados para gerar valor.\n')
    st.subheader('Objetivo')
    st.write('Este pequeno projeto foi desenvolvido para um teste técnico e tem como objetivo extrair insights dos dados fornecidos e responder questões relevantes para a vaga em questão.')
    st.subheader('Como funciona?')
    st.markdown("""
    O projeto foi dividido em duas partes: \n
    * Dashboard: Onde é possível visualizar os dados fornecidos e extrair alguns insights. Há muitas opções de análise a serem exploradas e eu escolhi o caminho de avaliar como estão as avaliações das 
empresas considerando os temas dos questionários. Então coloquei filros para os temas e plo histogramas para comparar as empresas e logo abaixo como elas estão pontuando (ótimo, regular ou péssimo) em relação aos temas. \n
    * Perguntas: São respondidas as perguntas enviadas pela empresa.
    """)

######################################################################################################
# sidebar
######################################################################################################

telas = ['Introdução', 'Dashboard', 'Perguntas']
c1,c2 = st.sidebar.columns([1,1])
tela_selecionada = st.sidebar.radio('Menu', telas)

if __name__ == '__main__':
    if tela_selecionada == 'Introdução':
        introducao()

    if tela_selecionada == 'Perguntas':
        perguntas()

    if tela_selecionada == 'Dashboard':
        df = data_treatement()
        dashboard(df)
