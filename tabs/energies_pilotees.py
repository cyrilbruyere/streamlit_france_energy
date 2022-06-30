import pandas as pd
# import geopandas as gpd
import matplotlib.pyplot as plt
import plotly_express as px
import streamlit as st
import plotly.subplots as sp
import darkdetect

title = "Energies pilotées"
sidebar_name = "Energies pilotées"

def run():
    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif")
    st.title(title)
    st.markdown("---")
    
    # Texte de présentation
    st.markdown("""
                Les énergies nucléaires et thermiques sont pilotées par l'homme qui approvisionne des matières premières et décide
                de produire. L'énergie hydraulique peut également être considérée comme étant pilotée par l'homme.
                Aussi, étant donnée les cycles de maintenance et les périodes de fortes sollicitations connues, on peut considérer que le
                cycle d'utilisation de ces capacités de production au niveau national est stable et répétable.
                Nous pouvons donc définir un schéma moyen utilisable en entrée de nos modèles de données.

                """)
    st.markdown("---")

    # Listes de colonnes
    regions = ['FRANCE', 'AURA', 'B', 'BFC', 'CVDL', 'GE', 'HF', 'IDF', 'N', 'NlleA', 'O', 'PACA', 'PDL']
    capacites = ['Capa_Totale', 'Capa_Renouvelable', 'Capa_Nucleaire', 'Capa_Thermique', 'Capa_Hydraulique', 'Capa_Solaire', 'Capa_Eolienne']
    charges = ['TCH_Nucleaire', 'TCH_Hydraulique', 'TCH_Solaire', 'TCH_Eolien'] # 'TCH_Total', 'TCH_Thermique', 'TCH_Renouvelable', 
    el_naturels = ['temperature', 'Vent', 'Humidite', 'Precipitations']

    # Filtres de sélection


    # Dataframe général contenant l'ensemble des données
    nucleaire = pd.read_csv('./source/nucleaire.csv', sep = ';')
    thermique = pd.read_csv('./source/thermique.csv', sep = ';')

    # Affichage
    fig1 = px.line(data_frame = nucleaire, x = range(0, nucleaire.shape[0]), y = ['Nucléaire', 'Avg_nucleaire'], height = 300)
    plt.style.use("dark_background" if darkdetect.theme() == "Dark" else 'seaborn-whitegrid')
    fig1.update_xaxes(tick0 = 0, dtick = 2920, gridcolor='grey', griddash='dash')
    fig1.update_xaxes(showticklabels = False, visible = False)
    fig1.update_yaxes(showgrid=False)
    fig1.update_layout(margin=dict(l=0, r=0, t=0, b=0))

    fig2 = px.line(data_frame = thermique, x = range(0, thermique.shape[0]), y = ['Thermique', 'Avg_thermique'], height = 300)
    plt.style.use("dark_background" if darkdetect.theme() == "Dark" else 'seaborn-whitegrid')
    fig2.update_xaxes(tick0 = 0, dtick = 2920, gridcolor='grey', griddash='dash')
    fig2.update_xaxes(showticklabels = False, visible = False)
    fig2.update_yaxes(showgrid=False)
    fig2.update_layout(margin=dict(l=0, r=0, t=0, b=0))

    st.plotly_chart(fig1)
    st.plotly_chart(fig2) 