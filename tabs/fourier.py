import pandas as pd
# import geopandas as gpd
import matplotlib.pyplot as plt
import plotly_express as px
import streamlit as st
# import plotly.subplots as sp
import numpy as np
from scipy import fftpack

title = "Transformée de Fourier"
sidebar_name = "Transformée de Fourier"

def run():
    st.title(title)
    st.markdown('Décomposition du signal en somme de signaux différents (fréquence, amplitude).')
    st.markdown('Permet de simplifier le signal sans altérer le nombre de valeur (pas temporel)')

    balance = pd.read_csv('./source/balance.csv', sep = ';')

    # Listes de colonnes
    energies = ['Consommation', 'Thermique', 'Nucleaire', 'Eolien', 'Solaire', 'Hydraulique', 'Pompage', 'Bioenergie', 'Production', 'Renouvelable', 'Balance']
    regions = ['FRANCE', 'AURA', 'B', 'BFC', 'CVDL', 'GE', 'HF', 'IDF', 'N', 'NlleA', 'O', 'PACA', 'PDL']
    capacites = ['Capa_Renouvelable', 'Capa_Hydraulique', 'Capa_Solaire', 'Capa_Eolienne'] # , 'Capa_Nucleaire', 'Capa_Thermique', 'Capa_Totale'
    charges = ['TCH_Nucleaire', 'TCH_Hydraulique', 'TCH_Solaire', 'TCH_Eolien']
    el_naturels = ['temperature', 'Vent', 'Humidite', 'Precipitations']

    # Filtres de sélection
    st.markdown("---")
    st.markdown(
        """
        <style>
        [data-baseweb="select"] {
            margin-top: -50px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    filtre = st.select_slider(label = 'Valeur du filtre',
                              options = [100000, 300000, 500000, 700000, 900000, 1000000, 3000000, 5000000, 8000000],
                              value = 100000,
                              key='sel_F')

    # Construction des données
    fourier = balance['Balance']

    # Spectre du signal
    data = fourier.values

    spectre = fftpack.fft(data)
    frequences = fftpack.fftfreq(data.size)
    power = np.abs(spectre)
    balance['frequence'] = np.abs(frequences)
    balance['power'] = power
 
    # # Elimination du bruit
    spectre_filtre = spectre
    spectre_filtre[power < filtre] = 0
    balance['spectre_filtre'] = np.abs(spectre_filtre)

    # # Reconstitution du signal
    filtered_data = fftpack.ifft(spectre_filtre)
    balance['Signal filtré'] = filtered_data.real

    # Affichage
    fig1 = px.line(data_frame = balance, x = range(0, balance.shape[0]), y = ['Balance', 'Signal filtré'], height = 300)
    fig1.update_xaxes(tick0 = 0, dtick = 2920, gridcolor='grey', griddash='dash')
    fig1.update_xaxes(showticklabels = False, visible = False)
    fig1.update_yaxes(showgrid=False)
    fig1.update_layout(margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor="black")

    fig2 = px.line(data_frame = balance, x = 'frequence', y = ['power', 'spectre_filtre'], height = 300)
    fig2.update_xaxes(tick0 = 0, dtick = 2920, gridcolor='grey', griddash='dash')
    fig2.update_xaxes(showticklabels = False, visible = False)
    fig2.update_yaxes(showgrid=False)
    fig2.update_yaxes(range = [0,1e7])
    fig2.update_layout(margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor="black")

    st.plotly_chart(fig1)
    st.plotly_chart(fig2) 

