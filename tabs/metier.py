import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly_express as px
import streamlit as st
# import plotly.subplots as sp

title = "Données métier"
sidebar_name = "Données métier"

def run():
    st.title(title)
    st.markdown("""
                Pour obtenir des variables explicatives cohérentes au niveau national, il convient de considérer les enregistrements
                météo au plus près des installations.
                Une sélection doit être opérée parmi les 40 stations en fonction de la variable à caractériser.
                """)
    st.markdown("---")

    # Carte de France
    carte = gpd.read_file('./geometry/regions.geojson')
    carte.replace(to_replace = ['Île-de-France', 'Centre-Val de Loire', 'Bourgogne-Franche-Comté',
                                'Normandie', 'Hauts-de-France', 'Grand Est', 'Pays de la Loire', 'Bretagne',
                                'Nouvelle-Aquitaine', 'Occitanie', 'Auvergne-Rhône-Alpes', "Provence-Alpes-Côte d'Azur"],
                value = ['IDF', 'CVDL', 'BFC', 'N', 'HF', 'GE', 'PDL', 'B', 'NlleA', 'O', 'AURA', 'PACA'],
                inplace = True)
    carte = carte[carte['nom'] != 'Corse']

    # Carte des stations
    station = pd.read_csv('./source/stations.csv', sep = ';')
    carte_sta = gpd.GeoDataFrame(station, geometry = gpd.points_from_xy(station['Longitude'], station['Latitude']), crs = 4326)
    
    # Carte des éoliennes
    eoliennes = gpd.read_file('./geometry/eoliennes.json')
    eoliennes.rename({'layer' : 'Regions'}, axis = 1, inplace = True)
    eoliennes.replace(to_replace = ['eolien_auvergne_rhone_alpes', 'eolien_bourgogne', 'eolien_bretagne',
                                    'eolien_centre', 'eolien_grand_est', 'eolien_hauts_de_france',
                                    'eolien_ile_de_france', 'eolien_normandie', 'eolien_nouvelle_aquitaine',
                                    'eolien_occitanie', 'eolien_paca', 'eolien_pays_de_la_loire'],
                      value = ['AURA', 'BFC', 'B', 'CVDL', 'GE', 'HF', 'IDF', 'N', 'NlleA', 'O', 'PACA', 'PDL'],
                      inplace = True)
    carte_eol = gpd.GeoDataFrame(eoliennes, geometry = 'geometry')
    carte_eol = carte_eol.to_crs(4326)

    # Datasets
    # energie = pd.read_csv('./source/energies_M.csv', sep = ';')
    # capacite = pd.read_csv('./source/capacites_M.csv', sep = ';')
    meteo = pd.read_csv('./source/meteo_M.csv', sep = ';')
    # balance = pd.read_csv('./source/balance_M.csv', sep = ';')
    # population = pd.read_csv('./source/population.csv', sep = ';')

    # Listes de colonnes
    energies = ['Consommation', 'Thermique', 'Nucleaire', 'Eolien', 'Solaire', 'Hydraulique', 'Pompage', 'Bioenergie', 'Production', 'Renouvelable', 'Balance']
    regions = ['FRANCE', 'AURA', 'B', 'BFC', 'CVDL', 'GE', 'HF', 'IDF', 'N', 'NlleA', 'O', 'PACA', 'PDL']
    capacites = ['Capa_Renouvelable', 'Capa_Hydraulique', 'Capa_Solaire', 'Capa_Eolienne'] # , 'Capa_Nucleaire', 'Capa_Thermique', 'Capa_Totale'
    charges = ['TCH_Nucleaire', 'TCH_Hydraulique', 'TCH_Solaire', 'TCH_Eolien']
    el_naturels = ['temperature', 'Vent', 'Humidite', 'Precipitations']
    region_names = ['France', 'Auverge Rhône Alpes', 'Bretagne', 'Bourgogne Franche Comté', 'Centre Val de Loire', 'Grand Est',
                    'Hauts de France', 'Ile de France', 'Normandie', 'Nouvelle Aquitaine', 'Occitanie', "Provence Alpes Côte d'Azur",
                    'Pays de Loire']

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
                        key='reg_L')
                        
    annee = st.selectbox(label = '',
                        options = range(2013, 2022, 1),
                        index = 8,
                        key='an_L')

    annee = annee - 2000
    region_code = regions[region_names.index(region)]

    # Dataframe général contenant l'ensemble des données

    carte_met = meteo[meteo['YY'] == annee]
    carte_met = carte_met.drop(['YYMM', 'MM'], axis = 1)
    carte_met = carte_met.groupby(['Regions', 'YY']).mean()
    carte_met.reset_index(inplace = True)

    carte_met = carte_met.merge(carte, left_on = 'Regions', right_on = 'nom')


    if region != 'France':
        carte_met = carte_met[carte_met['Regions']==region_code]
        carte_eol = carte_eol[carte_eol['Regions']==region_code]
        carte_sta = carte_sta[carte_sta['Regions']==region_code]
        map_eol = '#DCDCDC'
    else:
        map_eol = 'white'

    # Affichage
    fig1, ax = plt.subplots()
    plt.style.use('dark_background')
    carte_met = gpd.GeoDataFrame(carte_met, geometry = 'geometry', crs = 4326)
    carte_met.plot(column = 'Vent', cmap='PuRd', legend = True, ax = ax)
    carte_eol.plot(markersize = 3, color = map_eol, ax = ax)
    carte_sta.plot(markersize = 3, color = 'blue', ax = ax)
    plt.axis('off')
    plt.title('Vent', loc = 'left')
    st.pyplot(fig1)
