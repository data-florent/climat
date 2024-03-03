### Importation des librairies ###
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

### Importation des dataframes ###

country_df_OWID_CO_CLEAN = pd.read_csv('datasets/country_df_OWID_CO_CLEAN.csv', sep=',')
df_temp_catnat_1950 = pd.read_csv('datasets/df_temp_catnat_1950.csv', sep=',')
df_temp_catnat_1950_month = pd.read_csv('datasets/df_temp_catnat_1950_month.csv', sep=',')

### Header ###
st.image('images/iceberg.jpg', use_column_width=True)
st.markdown(
"<h2 style='text-align: center'>"
"<strong>Le changement climatique</strong>"
"<br><span style='font-size: smaller'>et les catastrophes naturelles</span>"
"</h2>"
, unsafe_allow_html=True)

### Menu latéral et création des pages ###
st.sidebar.image('images/earth.png', width=160)
st.sidebar.title("Changement climatique & catastrophes naturelles")
st.sidebar.subheader("Sommaire")
pages=["Présentation du projet", "Nettoyage des données", "Visualisations", "Modélisation"]
page=st.sidebar.radio("",pages)
st.sidebar.info(
"Auteurs du projet :"
" [Laura](https://www.linkedin.com/), "
"[Marion](https://www.linkedin.com/), "
"[Florent](https://www.linkedin.com/), "
"[Romain](https://www.linkedin.com/)"
"\n\n"
"Projet réalisé dans le cadre de la formation [DataScientest](https://datascientest.com/) de Data Analyst, promotion Septembre 2023 - Avril 2024"
"\n\n"
"Données :"
"\n"
"[NASA](https://data.giss.nasa.gov/gistemp/), "
"[OWID](https://github.com/owid/co2-data), "
"[EMDAT](https://www.emdat.be/)"
)

### Contenu des pages ###
if page == pages[0] : 
  st.write("### Présentation du projet")

if page == pages[1] : 
  st.write("### Nettoyage des données")

if page == pages[2] : 
  st.header("Visualisations")
  viz1 = "Evolutions du climat"
  viz2 = "Emissions de gaz à effet de serre"
  viz3 = "Catastrophes naturelles"
  dataviz_page = st.radio("", (viz1, viz2, viz3))
  
  #Evolutions du climat
  if dataviz_page == viz1:
    st.subheader("Evolutions du climat")
  
  #Emissions de gaz à effet de serre
  if dataviz_page == viz2:
    st.dataframe(country_df_OWID_CO_CLEAN.head())
    sorted_country_df_OWID_CO_CLEAN = country_df_OWID_CO_CLEAN.sort_values(by=['year'], ascending=True)
    sorted_country_df_OWID_CO_CLEAN = sorted_country_df_OWID_CO_CLEAN.loc[sorted_country_df_OWID_CO_CLEAN['year']>=1851]
    fig = px.choropleth(sorted_country_df_OWID_CO_CLEAN,
                    locationmode='country names', locations='country',
                    color='share_of_temperature_change_from_ghg',
                    color_continuous_scale=px.colors.sequential.Bluered,
                    range_color=[0,15], # permet de garder la même échelle pour toutes les années
                    hover_name='country', projection='natural earth', animation_frame='year',
                    title='Part (en %) de contribution au réchauffement climatique, basée sur les émissions de GES')
    st.plotly_chart(fig, use_container_width=True)

  #Catastrophes naturelles
  if dataviz_page == viz3:
    st.write("Catastrophes naturelles")

if page == pages[3] : 
  st.write("### Modélisation")