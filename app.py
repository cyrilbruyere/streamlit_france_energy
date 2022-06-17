from collections import OrderedDict
import streamlit as st
from config import config
from tabs import introduction, energie_renouvelable, meteo_et_energies, modelisation, optimisation, fourier, metier, normalisation, energies_pilotees, resultats, interpretation, bilan

st.set_page_config(
    page_title=config.TITLE,
    page_icon="https://datascientest.com/wp-content/uploads/2020/03/cropped-favicon-datascientest-1-32x32.png"
)

with open("./assets/style.css", "r") as f:
    style = f.read()

st.markdown(f"<style>{style}</style>", unsafe_allow_html=True)

TABS = OrderedDict(
    [
        (introduction.sidebar_name, introduction),
        (energie_renouvelable.sidebar_name, energie_renouvelable),
        (meteo_et_energies.sidebar_name, meteo_et_energies),
        (modelisation.sidebar_name, modelisation),
        (optimisation.sidebar_name, optimisation),
        (fourier.sidebar_name, fourier),
        (metier.sidebar_name, metier),
        (normalisation.sidebar_name, normalisation),
        (energies_pilotees.sidebar_name, energies_pilotees),
        (resultats.sidebar_name, resultats),
        (interpretation.sidebar_name, interpretation),
        (bilan.sidebar_name, bilan)
    ]
)

def run():
    st.sidebar.image(
        "https://dst-studio-template.s3.eu-west-3.amazonaws.com/logo-datascientest.png",
        width=200
    )
    st.sidebar.markdown(f"## {config.TITLE}")
    tab_name = st.sidebar.radio("", list(TABS.keys()), 0)
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"## {config.PROMOTION}")

    st.sidebar.markdown("### Team members:")
    for member in config.TEAM_MEMBERS:
        st.sidebar.markdown(member.sidebar_markdown(), unsafe_allow_html=True)

    tab = TABS[tab_name]

    tab.run()

if __name__ == "__main__":
    run()
