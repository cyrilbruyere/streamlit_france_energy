import pandas as pd
# import geopandas as gpd
import matplotlib.pyplot as plt
import plotly_express as px
import streamlit as st
import plotly.subplots as sp
import datetime as dt
import darkdetect

title = "Résultats"
sidebar_name = "Résultats"

def run():
    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif")
    st.title(title)
    st.markdown("---")
    
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
    resultat = st.selectbox(label ='',
                            options = ['Prédiction directe', 'Prédictions directe et indirecte'],
                            index = 0,
                            key = 'pred_R')

    # Dataframe général contenant l'ensemble des données
    if resultat == 'Prédiction directe':
        predictions = pd.read_csv('./results/predictions_directe.csv', sep = ';')
        predictions['Dates'] = pd.to_datetime(predictions['Dates'], dayfirst = True)
        erreur = pd.read_csv('./results/erreur_directe.csv', sep = ';')
        colonnes = ['Reel', 'Pred (sinus)', 'Pred (metier)', 'Pred_TF ()', 'Pred_TF (metier)', 'RL Pred (metier)']
        display_text = """
                       La prédiction directe consiste vulgairement à s'appuyer sur les productions les plus importantes
                       et les plus prévisibles pour tenter de prédire le risque de balance négative, en faisant abstraction
                       des filières les plus aléatoires, notamment l'éolien qui est la source d'énergie la plus imprévisible.

                       """
    else:
        predictions = pd.read_csv('./results/predictions_indirecte.csv', sep = ';')
        predictions['Dates'] = pd.to_datetime(predictions['Dates'], dayfirst = True)
        erreur = pd.read_csv('./results/erreur_indirecte.csv', sep = ';')
        colonnes = ['Reel', 'Pred indirecte', 'Pred LR directe']
        display_text = """
                       La prédiction directe qui s'affranchit des variables instables, notamment de la filière éolienne,
                       est plus proche en moyenne de la réalité. Ce résultat n'est pas forcément satisfaisant car nous
                       recherchons des pics négatifs nécessitant une prise de décision pour éviter la rupture d'approvisionnement
                       des utilisateurs en énergie.
                       """
    
    # Texte de présentation
    st.subheader(resultat)
    st.markdown(display_text)
    st.markdown("---")

    # Affichage
    fig1 = px.line(data_frame = predictions, x = 'Dates', y = colonnes, height = 450)
    plt.style.use("dark_background" if darkdetect.theme() == "Dark" else 'seaborn-whitegrid')
    fig1.update_xaxes(tickangle=90, tickvals=["2020-03-17", "2020-05-03", "2021-01-01"], gridcolor='grey', griddash='dash')
    fig1.update_xaxes(showticklabels = True, visible = True)
    fig1.update_yaxes(showgrid=False)
    fig1.update_layout(margin=dict(l=0, r=0, t=0, b=0))

    fig2 = px.bar(data_frame = erreur, x = 'mean', y = 'Erreur', text_auto = True, height = 200)
    plt.style.use("dark_background" if darkdetect.theme() == "Dark" else 'seaborn-whitegrid')
    fig2.update_xaxes(showgrid=False)
    fig2.update_xaxes(showticklabels = False, visible = False)
    fig2.update_yaxes(showgrid=False)
    fig2.update_layout(margin=dict(l=0, r=135, t=0, b=0), yaxis={'categoryorder':'category ascending'})

    st.plotly_chart(fig1)
    st.plotly_chart(fig2) 