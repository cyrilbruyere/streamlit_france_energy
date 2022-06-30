import pandas as pd
# import geopandas as gpd
# import matplotlib.pyplot as plt
import plotly_express as px
import streamlit as st
import plotly.subplots as sp

title = "Interprétation"
sidebar_name = "Interprétation"

def run():
    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif")
    st.title(title)
    st.markdown("---")
    
    # Texte de présentation
    st.subheader("SARIMAX")
    st.markdown("""
                Le modèle SARIMAX est insensible à la qualité des variables exogènes, le résultat avec des
                courbes sinusoïdales étant équivalent au résultat avec des données métiers liées

                """)
    st.markdown('') 
    st.markdown("---")
    st.subheader("Données éxogènes")
    st.markdown("""
                Filtrer les données exogènes n’apporte pas d’amélioration, que ce soit pour le modèle
                SARIMAX ou la régression linéaire. Cependant, il n’y a pas de dégradation notable non plus,
                notamment pour la régression linéaire, ce qui signifie que cette réduction de dimension est
                pertinente et que l’information principale est conservée.
                
                """)
    st.markdown('') 
    st.markdown("---")
    st.subheader("Transformée de Fourier")
    st.markdown("""
                Filtrer le signal d’entrée à prédire n’apporte pas non plus d’amélioration significative. Le signal
                reste trop complexe pour une exploitation efficace par le modèle SARIMAX

                """)
    st.markdown("---")
    st.subheader("Lissage des données")
    st.markdown("""
                Lisser les données en augmentant le pas temporel est l’amélioration la plus significative de la
                performance des modèles
                """)

    # Filtres de sélection


    # Dataframe général contenant l'ensemble des données


    # Affichage
