import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
# import plotly_express as px
import streamlit as st
# import plotly.subplots as sp
import darkdetect

title = "Météo et énergies"
sidebar_name = "Météo et énergies"

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
    meteo = pd.read_csv('./source/meteo_M.csv', sep = ';')
    # balance = pd.read_csv('./source/balance_M.csv', sep = ';')
    population = pd.read_csv('./source/population.csv', sep = ';')

    # Listes de colonnes
    energies = ['Consommation', 'Thermique', 'Nucleaire', 'Eolien', 'Solaire', 'Hydraulique', 'Pompage', 'Bioenergie', 'Production', 'Renouvelable', 'Balance']
    regions = ['FRANCE', 'AURA', 'B', 'BFC', 'CVDL', 'GE', 'HF', 'IDF', 'N', 'NlleA', 'O', 'PACA', 'PDL']
    capacites = ['Capa_Renouvelable', 'Capa_Hydraulique', 'Capa_Solaire', 'Capa_Eolienne'] # , 'Capa_Nucleaire', 'Capa_Thermique', 'Capa_Totale'
    charges = ['TCH_Nucleaire', 'TCH_Hydraulique', 'TCH_Solaire', 'TCH_Eolien']
    el_naturels = ['temperature', 'Vent', 'Humidite', 'Precipitations']

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
    annee = st.selectbox(label = '',
                        options = range(2013, 2022, 1),
                        index = 8,
                        key='an_ME')

    filiere = st.selectbox(label = '',
                        options = ['Consommation', 'Hydraulique', 'Eolien', 'Solaire'],
                        index = 0,
                        key='en_ME')

    annee = annee - 2000

    # Dataframe général contenant l'ensemble des données
    carte_gen = energie[energie['YY'] == annee]
    carte_gen.drop(['YYMM', 'MM'], axis = 1, inplace = True)
    carte_gen = carte_gen.groupby(['Regions', 'YY']).mean()
    carte_gen.reset_index(inplace = True)

    carte_met = meteo[meteo['YY'] == annee]
    # Temperature de l'hiver uniquement
    carte_met.loc[carte_met['MM'].isin([4, 5, 6, 7, 8, 9, 10]), 'Temperature'] = 0

    carte_met = carte_met.drop(['YYMM', 'MM'], axis = 1)
    carte_met = carte_met.groupby(['Regions', 'YY']).mean()
    carte_met.reset_index(inplace = True)

    carte_cap = capacite[capacite['YY'] == annee]
    carte_cap = carte_cap.drop(['YYMM', 'MM'], axis = 1)
    carte_cap = carte_cap.groupby(['Regions', 'YY']).mean()
    carte_cap.reset_index(inplace = True)

    carte_pop = population

    carte_gen = carte_gen.merge(carte_met, left_on = 'Regions', right_on = 'Regions')
    carte_gen = carte_gen.merge(carte_cap, left_on = 'Regions', right_on = 'Regions')
    carte_gen = carte_gen.merge(carte_pop, left_on = 'Regions', right_on = 'Regions')
    carte_gen = carte_gen.merge(carte, left_on = 'Regions', right_on = 'nom')

    # carte_gen['Chauffage'] = carte_gen['Population'] / carte_gen['Temperature']

    if filiere == 'Consommation':
        liaison = 'Temperature'
        localisation = 'Population'
        map_col = 'PuRd_r'
        display_text = """
                       Nous avons vu que la consommation était liée à la température (chauffage en hiver).
                       Nous observons qu'elle est également fortement corrélée à la population. La notion de quantité de chauffage
                       est sous-jacente, combinaison de température faible et nombre d'habitations à chauffer.
                       """
    elif filiere == 'Hydraulique':
        liaison = 'Precipitations'
        localisation = 'Capa_Hydraulique'
        map_col = 'PuRd'
        display_text = """
                       La production d'énergie dépent de la localisation des installations, principalement dans les régions où
                       il y a du relief, permettant la construction de barrages notamment.
                       En revanche, certaines régions n'ayant pas ou peu de capacité de production, bénéficie de fortes quantités
                       de précipitations. C'est un potentiel non exploité car probablement difficile à exploiter.
                       """
    elif filiere == 'Eolien':
        liaison = 'Vent'
        localisation = 'Capa_Eolien'
        map_col = 'PuRd'
        display_text ="""
                       La construction des éoliennes, plus récente et certainement plus objet à critique tant elles impactent
                       le paysage visuel, apparait avec des contradictions.
                       Les régions les plus venteuses ne sont pas celles qui ont le plus d'éoliennes et vis-versa.
                       """
    elif filiere == 'Solaire':
        liaison = 'Humidite'
        localisation = 'Capa_Solaire'
        map_col = 'plasma'
        display_text = """
                       La production d'énergie solaire est quant à elle totalement cohérente. Les installations les plus nombreuses sont
                       dans les régions où l'ensoleillement est le plus important.
                       On peut imaginer que la qualité de ces investissements vient du fait que l'installation des panneaux solaires est
                       à la charge et au bénéfice des particuliers.
                       """

    # Affichage
    st.markdown(display_text)

    fig1, ax = plt.subplots()
    plt.style.use("dark_background" if darkdetect.theme() == "Dark" else 'seaborn-whitegrid')
    carte_gen = gpd.GeoDataFrame(carte_gen, geometry = 'geometry', crs = 4326)
    carte_gen.plot(column = filiere, cmap='BuGn', legend = True, ax = ax)
    plt.axis('off')
    plt.title(filiere + ' (énergie)', loc = 'left', color = '#10b8dd')
    st.pyplot(fig1)

    fig2, ax = plt.subplots()
    plt.style.use("dark_background" if darkdetect.theme() == "Dark" else 'seaborn-whitegrid')
    carte_gen = gpd.GeoDataFrame(carte_gen, geometry = 'geometry', crs = 4326)
    carte_gen.plot(column = localisation, cmap='PuBu', legend = True, ax = ax)
    plt.axis('off')
    plt.title(localisation, loc = 'left', color = '#10b8dd')
    st.pyplot(fig2)

    fig3, ax = plt.subplots()
    plt.style.use("dark_background" if darkdetect.theme() == "Dark" else 'seaborn-whitegrid')
    carte_gen = gpd.GeoDataFrame(carte_gen, geometry = 'geometry', crs = 4326)
    carte_gen.plot(column = liaison, cmap=map_col, legend = True, ax = ax)
    plt.axis('off')
    plt.title(liaison, loc = 'left', color = '#10b8dd')
    st.pyplot(fig3)

    # if filiere == 'Consommation':
    #     fig4, ax = plt.subplots()
    #     plt.style.use('dark_background')
    #     carte_gen = gpd.GeoDataFrame(carte_gen, geometry = 'geometry', crs = 4326)
    #     carte_gen.plot(column = 'Chauffage', cmap='PuRd', legend = True, ax = ax)
    #     plt.axis('off')
    #     plt.title('Chauffage', loc = 'left')
    #     st.pyplot(fig4)


