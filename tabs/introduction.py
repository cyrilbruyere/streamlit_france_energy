import pandas as pd
# import geopandas as gpd
# import matplotlib.pyplot as plt
import plotly_express as px
import streamlit as st
import plotly.subplots as sp

title = "Introduction"
sidebar_name = "Introduction"

def run():
    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif")
    st.title(title)
    st.markdown("---")
    
    # Texte de présentation
    st.subheader('Notion de balance')
    st.markdown("""
                L'objectif est la prédiction du risque de rupture d'énergie. Elle se produit lorsque la production est insuffisante
                pour répondre au besoin défini par la consommation.

                On appelle balance, la différence entre la production et la consommation.

                L'enjeu est donc la détection des balances négatives permettant les décisions de type :

                1. Import d'énergie

                2. Développement de nouvelles capacités de production

                """)
    st.markdown("---")

    # Datasets
    energie = pd.read_csv('./source/energies_M.csv', sep = ';')
    # capacite = pd.read_csv('./source/capacites_M.csv', sep = ';')
    # meteo = pd.read_csv('./source/meteo_M.csv', sep = ';')
    balance = pd.read_csv('./source/balance_M.csv', sep = ';')
    # population = pd.read_csv('./source/population.csv', sep = ';')

    # Listes de colonnes
    regions = ['FRANCE', 'AURA', 'B', 'BFC', 'CVDL', 'GE', 'HF', 'IDF', 'N', 'NlleA', 'O', 'PACA', 'PDL']
    capacites = ['Capa_Totale', 'Capa_Renouvelable', 'Capa_Nucleaire', 'Capa_Thermique', 'Capa_Hydraulique', 'Capa_Solaire', 'Capa_Eolienne']
    charges = ['TCH_Nucleaire', 'TCH_Hydraulique', 'TCH_Solaire', 'TCH_Eolien'] # 'TCH_Total', 'TCH_Thermique', 'TCH_Renouvelable', 
    el_naturels = ['temperature', 'Vent', 'Humidite', 'Precipitations']

    # Filtres de sélection
    st.markdown(
        """
        <style>
        [data-baseweb="select"] {
            margin-top: -50px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    annee = st.selectbox(label  = '',
                        options = ['All years', 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
                        index = 0,
                        key='an_Intro')

    # Dataframe général contenant l'ensemble des données
    energie_FR = energie.drop(['Regions'], axis = 1)
    energie_FR = energie_FR.groupby(['YY', 'YYMM']).sum()
    energie_FR.reset_index(inplace = True)

    if annee == 'All years':
        graf_energie = energie_FR
        graf_balance = balance
        nticks = 10
    else:
        annee = annee - 2000
        graf_energie = energie_FR[energie_FR['YY'] == annee]
        graf_balance = balance[balance['YY'] == annee]
        nticks = 12

    # Affichage
    fig1 = px.line(data_frame = graf_energie, x = 'YYMM', y = ['Production', 'Consommation'])
    fig2 = px.scatter(data_frame = graf_balance, x = 'YYMM', y = ['balance'])

    figure1_traces = []
    figure2_traces = []
    for trace in range(len(fig1["data"])):
        figure1_traces.append(fig1["data"][trace])
    for trace in range(len(fig2["data"])):
        figure2_traces.append(fig2["data"][trace])

    #Create a 1x2 subplot
    this_figure = sp.make_subplots(rows=2, cols=1, shared_xaxes=True) 

    # Get the Express fig broken down as traces and add the traces to the proper plot within in the subplot
    for traces in figure1_traces:
        this_figure.append_trace(traces, row=1, col=1)
    for traces in figure2_traces:
        this_figure.append_trace(traces, row=2, col=1)

    this_figure.update_xaxes(type='category')
    this_figure.update_xaxes(nticks = nticks, gridcolor='grey', griddash='dash')
    this_figure.update_xaxes(showgrid=False)
    this_figure.update_yaxes(showgrid=False)
    this_figure.update_layout(margin=dict(l=0, r=0, t=20, b=0))#, paper_bgcolor="LightSteelBlue")

    st.plotly_chart(this_figure)

    st.markdown("1. Consommation cyclique : très forte l'hiver avec un rebond au coeur de l'été")
    st.markdown('2. Production = réponse à la consommation mais de moins en moins stable')
    st.markdown("3. Lissage mensuel ne permet pas d'identifier les balances négatives")
    st.markdown('4. Balances négatives de plus en plus fréquentes et importantes')
