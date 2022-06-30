import pandas as pd
# import geopandas as gpd
# import matplotlib.pyplot as plt
import plotly_express as px
import streamlit as st
import plotly.subplots as sp

title = "Bilan"
sidebar_name = "Bilan"

def run():
    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif")
    st.title(title)
    st.markdown("---")
    
    # Texte de présentation
    st.subheader("SARIMAX")
    st.markdown("""
                l’étude montre que celui-ci n’est pas adapté à un signal complexe. Notamment, il ne prend en compte
                qu’une seule saisonnalité alors que les signaux de la réalité sont constitués d’une multitude de
                composantes (fréquences, amplitudes, tendance, etc). Le modèle semble donc incapable d’offrir une
                réponse satisfaisante, y compris lorsque on lui attribue des régresseurs exogènes.

                """)
    st.markdown("---")
    st.subheader("Regression linéaire")
    st.markdown("""
                la régression linéaire semble prometteuse mais à la condition que l’on puisse construire des variables
                explicatives de qualité. Celà passe notamment par la localisation des enregistrements météorologiques
                à l’endroit des sites de production. Le revers de cette modélisation est qu’elle s’appuie sur des
                variables explicatives qui doivent elles-mêmes être prédites.

                """)
            
    st.markdown("---")
    st.subheader("Deep learning")
    st.markdown("""
                Le travail entrepris ici n'offre pas de résultat satisfaisant. La suite de cette étude serait la
                recherche et la mise en œuvre de modèles de Deep Learning.

                """)
    

    # Filtres de sélection


    # Dataframe général contenant l'ensemble des données


    # Affichage
