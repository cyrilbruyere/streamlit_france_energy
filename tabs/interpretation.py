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
                courbes sinusoïdales étant équivalent au résultat avec des données métier corrélées.

                """)
    st.markdown("---")
    st.subheader("Lissage des données")
    st.markdown("""
                Lisser les données en augmentant le pas temporel est l’amélioration la plus significative de la
                performance du modèle SARIMAX. Cependant, il ne permet pas de répondre à la problématique car il
                implique une perte d'information trop importante.
                """)
    st.markdown("---")
    st.subheader("Transformée de Fourier")
    st.markdown("""
                Filtrer le signal d’entrée à prédire n’apporte pas d’amélioration significative. Le signal
                reste trop complexe pour une exploitation efficace par le modèle SARIMAX. Il permet en revanche de
                s'affranchir du paramètre exogène pour l'obtention d'un résultat et a l'avantage de conserver
                l'information permettant de répondre au problème.

                """)
    st.markdown("---")
    st.subheader("Données éxogènes")
    st.markdown("""
                Les données exogènes métier nécessitant un travail important de collecte et de traitement n’apportent pas
                d’amélioration pour le modèle SARIMAX.
                Cependant, elles s'avèrent très utiles pour augmenter significativement la performance en utilisant un
                modèle de régression linéaire.
                
                """)
    

    # Filtres de sélection


    # Dataframe général contenant l'ensemble des données


    # Affichage
