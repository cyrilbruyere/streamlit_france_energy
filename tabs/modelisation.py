import pandas as pd
# import geopandas as gpd
# import matplotlib.pyplot as plt
import plotly_express as px
import streamlit as st
import plotly.subplots as sp

title = "Modélisation"
sidebar_name = "Modélisation"

def run():
    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif")
    st.title(title)
    st.markdown("---")
    
    # Texte de présentation
    st.subheader("Objectif de prédiction de la balance")
    st.markdown("""
                1. Prédiction directe 
                
                2. Prédiction indirecte

                La prédiction indirecte consiste à reconstituer la balance à partir de la prédiction de
                la consommation et les composantes de la production.

                """)
    st.markdown('') 
    st.markdown("---")
    st.subheader('Modèles utilisés')
    st.markdown("""
                1. SARIMAX (régression sur les éléments précédents, moyenne mobile et régresseurs exogènes)

                2. Régression linéaire, nécessitant des variables explicatives
                
                """)
    st.markdown('') 
    st.markdown("---")
    st.subheader('Régresseurs éxogènes et variables explicatives')
    st.markdown("""
                1. Caractéristiques métérologiques (vent, pluie, température, etc)
                
                2. Production d'énergie pilotée par l'homme (nucléaire, thermique, hydraulique)
                """)

    # Filtres de sélection


    # Dataframe général contenant l'ensemble des données


    # Affichage
