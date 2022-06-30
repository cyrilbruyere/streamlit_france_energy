import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly_express as px
import streamlit as st
import darkdetect
# import plotly.subplots as sp
from PIL import Image

title = "Energie renouvelable"
sidebar_name = "Energie Renouvelable"

def run():
    st.title(title)
    
    # Carte de France
    carte = gpd.read_file('./geometry/regions.geojson')
    carte.replace(to_replace = ['Île-de-France', 'Centre-Val de Loire', 'Bourgogne-Franche-Comté',
                                'Normandie', 'Hauts-de-France', 'Grand Est', 'Pays de la Loire', 'Bretagne',
                                'Nouvelle-Aquitaine', 'Occitanie', 'Auvergne-Rhône-Alpes', "Provence-Alpes-Côte d'Azur"],
                value = ['IDF', 'CVDL', 'BFC', 'N', 'HF', 'GE', 'PDL', 'B', 'NlleA', 'O', 'AURA', 'PACA'],
                inplace = True)
    carte = carte[carte['nom'] != 'Corse']

    # Datasets
    energie = pd.read_csv('./source/energies_M.csv', sep = ';')
    capacite = pd.read_csv('./source/capacites_M.csv', sep = ';')
    # meteo = pd.read_csv('./source/meteo_M.csv', sep = ';')
    # balance = pd.read_csv('./source/balance_M.csv', sep = ';')
    # population = pd.read_csv('./source/population.csv', sep = ';')

    # Listes de colonnes
    energies = ['Hydraulique', 'Eolien', 'Solaire'] # 'Renouvelable', 'Consommation', 'Thermique', 'Nucleaire', 'Pompage', 'Bioenergie', 'Production', 'Balance'
    regions = ['FRANCE', 'AURA', 'B', 'BFC', 'CVDL', 'GE', 'HF', 'IDF', 'N', 'NlleA', 'O', 'PACA', 'PDL']
    capacites = ['Capa_Hydraulique', 'Capa_Eolien', 'Capa_Solaire'] # 'Capa_Renouvelable', 'Capa_Totale', 'Capa_Nucleaire', 'Capa_Thermique'
    charges = ['TCH_Hydraulique', 'TCH_Eolien', 'TCH_Solaire'] # 'TCH_Renouvelable', 'TCH_Total', 'TCH_Thermique', 'TCH_Nucleaire', 
    el_naturels = ['temperature', 'Vent', 'Humidite', 'Precipitations']
    region_names = ['France', 'Auverge Rhône Alpes', 'Bretagne', 'Bourgogne Franche Comté', 'Centre Val de Loire', 'Grand Est',
                    'Hauts de France', 'Ile de France', 'Normandie', 'Nouvelle Aquitaine', 'Occitanie', "Provence Alpes Côte d'Azur",
                    'Pays de Loire']

    
    # Image
    img = Image.open("./assets/production.png") 
    st.image(img, width=500)
    
    # Filtres de sélection
    st.markdown(
        """
        <style>
        [data-baseweb="select"] {
            margin-top: -40px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    region = st.selectbox(label = '',
                        options = region_names,
                        index = 0,
                        key='reg_ER')

    annee = st.selectbox(label = '',
                        options = range(2013, 2022, 1),
                        index = 8,
                        key='an_ER')

    filiere = st.selectbox(label = '',
                        options = energies,
                        index = 2,
                        key='en_ER')

    annee = annee - 2000
    region_code = regions[region_names.index(region)]

    capa_filiere = ['Capa_Thermique']
    capa_filiere.append('Capa_' + filiere)
    TCH_filiere = 'TCH_' + filiere

    # Dataframe général contenant l'ensemble des données
    if region == 'France':
        graf_capa = capacite.drop(['Regions'], axis = 1)
        graf_capa = graf_capa.groupby(['YYMM']).sum()
        graf_capa.reset_index(inplace = True)
    else:
        graf_capa = capacite[capacite['Regions'] == region_code]

    carte_tch = capacite[capacite['YY'] == annee]
    carte_tch.drop(['YYMM', 'MM'], axis = 1, inplace = True)
    carte_tch = carte_tch.groupby(['Regions', 'YY']).mean()
    carte_tch.reset_index(inplace = True)

    energie_tch = energie[energie['YY'] == annee]
    energie_tch.drop(['YYMM', 'MM'], axis = 1, inplace = True)
    energie_tch = energie_tch.groupby(['Regions', 'YY']).mean()
    energie_tch.reset_index(inplace = True)

    carte_tch = carte_tch.merge(energie_tch, left_on = 'Regions', right_on = 'Regions')
    carte_tch['TCH_Total'] = carte_tch['Production'] / (carte_tch['Capa_Totale'] + 1) / 1000 * 100
    carte_tch['TCH_Renouvelable'] = carte_tch['Renouvelable'] / (carte_tch['Capa_Renouvelable'] + 1) / 1000 * 100
    carte_tch['TCH_Nucleaire'] = carte_tch['Nucleaire'] / (carte_tch['Capa_Nucleaire'] + 1) / 1000 * 100
    carte_tch['TCH_Thermique'] = carte_tch['Thermique'] / (carte_tch['Capa_Thermique'] + 1) / 1000 * 100
    carte_tch['TCH_Hydraulique'] = carte_tch['Hydraulique'] / (carte_tch['Capa_Hydraulique'] + 1) / 1000 * 100
    carte_tch['TCH_Eolien'] = carte_tch['Eolien'] / (carte_tch['Capa_Eolien'] + 1) / 1000 * 100
    carte_tch['TCH_Solaire'] = carte_tch['Solaire'] / (carte_tch['Capa_Solaire'] + 1) / 1000 * 100

    carte_tch = carte_tch.merge(carte, left_on = 'Regions', right_on = 'nom')
    carte_tch = carte_tch[[TCH_filiere, 'geometry']]

    # Affichage
    fig1 = px.line(data_frame = graf_capa, x = 'YYMM', y = capa_filiere, height = 300)
    fig1.update_xaxes(type='category')
    fig1.update_xaxes(nticks = 9, gridcolor='grey', griddash='dash')
    fig1.update_yaxes(showgrid=False)
    fig1.update_layout(margin=dict(l=20, r=20, t=20, b=20),
                    paper_bgcolor="black" if darkdetect.theme() == "Dark" else "white")
    st.plotly_chart(fig1)

    fig2, ax = plt.subplots()
    plt.style.use("dark_background" if darkdetect.theme() == "Dark" else 'seaborn-whitegrid')
    carte_tch = gpd.GeoDataFrame(carte_tch, geometry = 'geometry', crs = 4326)
    carte_tch.plot(column = TCH_filiere, cmap='PuRd', legend = True, ax = ax)
    plt.axis('off')
    plt.title('Taux de charge', loc = 'left', color = '#10b8dd')
    st.pyplot(fig2)

    st.markdown("---")
    st.markdown("""
                1. Développement des sources renouvelable pour remplacer les énergies fossiles (charbon, ...)
                2. Plus de capacité mais efficacité réduite, 20 à 60% (contre 90% pour les énergies pilotées)

                """)