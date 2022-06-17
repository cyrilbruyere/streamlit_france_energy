import pandas as pd
# import geopandas as gpd
# import matplotlib.pyplot as plt
import plotly_express as px
import streamlit as st
import plotly.subplots as sp

title = "Normalisation"
sidebar_name = "Normalisation"

def run():
    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif")
    st.title(title)
    st.markdown("---")
    
    # Texte de présentation
    st.markdown("""
                Les énergies renouvelables, notamment les filières solaire et éolienne, sont en plein expansion.
                Aussi, afin d'alimenter nos modèles avec des données qui ne sont pas influencées par ces développements,
                nous avons privilégié l'utilisation d'une variable reconstruite à partir de l'évolution des capacités de production
                (source : Wikipédia).
                Nos modèles fonctionnent ainsi sur le taux de charge (production / capacité) qui lui est répétable et homogène dans
                le temps.

                """)
    st.markdown("---")

    # Filtres de sélection


    # Dataframe général contenant l'ensemble des données
    eolien = pd.read_csv('./source/eolien.csv', sep = ';')


    # Affichage
    fig1 = px.line(data_frame = eolien, x = range(0, eolien.shape[0]), y = ['Eolien', 'Capa_eol'], height = 300)
    fig1.update_xaxes(tick0 = 0, dtick = 2920, gridcolor='grey', griddash='dash')
    fig1.update_xaxes(showticklabels = False, visible = False)
    fig1.update_yaxes(showgrid=False)
    fig1.update_layout(margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor="black")

    fig2 = px.line(data_frame = eolien, x = range(0, eolien.shape[0]), y = ['TCH_eol'], height = 300)
    fig2.update_xaxes(tick0 = 0, dtick = 2920, gridcolor='grey', griddash='dash')
    fig2.update_xaxes(showticklabels = False, visible = False)
    fig2.update_yaxes(showgrid=False)
    fig2.update_layout(margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor="black")

    st.plotly_chart(fig1)
    st.plotly_chart(fig2) 