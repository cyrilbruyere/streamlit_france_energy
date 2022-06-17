import pandas as pd
# import geopandas as gpd
# import matplotlib.pyplot as plt
import plotly_express as px
import streamlit as st
import plotly.subplots as sp

title = "Recherche d'optimisations"
sidebar_name = "Recherche d'optimisations"

def run():
    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif")
    st.title(title)
    st.markdown("---")
    
    # Texte de présentation
    st.subheader("Objectif et moyens disponibles")
    st.markdown("""
                L'objectif est de détecter les balances négatives. Nous disposons d'un jeu de données très précis avec un pas
                temporel de 30 minutes.

                Malheureusement, SARIMAX n'a pas été en mesure de traiter la finesse de ces données et nous avons dû explorer
                différentes possibilités pour tenter d'obtenir un résultat satisfaisant au regard de l'objectif fixé.

                """)
    st.markdown('') 
    st.markdown("---")
    st.subheader("Lissage des données")
    st.markdown("""
                1. Données météorologiques disponibles avec un pas de 3h

                2. Lissage mensuel non satisfaisant car supprimant l'information des balances négatives dans le jeu de données.
                
                """)
    st.markdown('') 
    st.markdown("---")
    st.subheader("Réduction des données")
    st.markdown("""
                Utilisation de la transformation de Fourier pour réduire la quantité d'information présente dans le signal
                tout en conservant les caractéristiques principales.

                """)
    st.markdown("---")
    st.subheader("Sélection des variables explicatives")
    st.markdown("""
                1. SYNOP : données météorologiques (visualisation et choix des variables)

                2. Constitution de bases de données sur les capacités de production (source : Wikipédia)

                """)

    # Filtres de sélection


    # Dataframe général contenant l'ensemble des données


    # Affichage
