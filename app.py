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
world_df_OWID_CO_CLEAN= pd.read_csv('datasets/world_df_OWID_CO_CLEAN.csv', sep=',')

### Header ###
st.image('images/iceberg.jpg', use_column_width=True)
st.markdown(
"<h2 style='text-align: center'>"
"<strong>Le changement climatique</strong>"
"<br><span style='font-size: smaller'>et les catastrophes naturelles</span>"
"</h2>"
, unsafe_allow_html=True)

### Menu latéral et création des pages ###
st.sidebar.title("Changement climatique & catastrophes naturelles")
st.sidebar.subheader("Sommaire")
pages=["Présentation du projet", "Nettoyage des données", "Visualisations", "Prédictions", "Conclusion et perspectives"]
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
# Page Présentation du projet
if page == pages[0] : 
  st.header("Présentation du projet")
  st.markdown("<h3>1. Objectifs du projet</h3>"
	"<p style='text-align: justify'>"
	"Plusieurs objectifs ont été fixés dans le cadre de ce projet :"
  "<ul>"
  "<li>constater le réchauffement climatique mondial et régional ;</li>"
  "<li>montrer les liens entre la hausse des températures et certains indicateurs de l'activité humaine (gaz à effet de serre, PIB, etc.) ;</li>"
  "<li>démontrer des corrélations entre l’évolution des variations de températures et les catastrophes naturelles.</li>"
  "</ul>"
  "</p>"
  , unsafe_allow_html=True)
  st.markdown("<h3>2. Données utilisées</h3>"
	"<p style='text-align: justify'>"
	"Plusieurs jeux de données téléchargeables librement ont été utilisés :"
  "<ul>"
  "<li>8 fichiers correspondant à des relevés de températures effectués par la <a href='https://data.giss.nasa.gov/gistemp/'>Nasa</a> dans le monde ou dans certaines régions du globe, et ce sur une période allant de 1880 à nos jours. 144 lignes et 19 colonnes sont dénombrées dans le principal fichier ;</li>"
  "<li>1 dataset <a href='https://github.com/owid/co2-data/'>Our World In Data (OWID)</a> portant sur les gaz à effet de serre de 1750 à nos jours. Ce dataset comporte 50 598 lignes et 79 colonnes ;</li>"
  "<li>1 tableau <a href='https://emdat.be/'>EMDAT</a> recensant les catastrophes naturelles de 1950 à aujourd'hui, produit par le CRED au sein de l'Université de Louvain. 14 679 lignes et 46 colonnes sont comptabilisées dans ce tableau.</li>"
  "</ul>"
  "</p>"
  , unsafe_allow_html=True)
  st.markdown("<h3>3. Méthodes et outils de travail</h3>"
	"<p style='text-align: justify'>"
	"Les différents fichiers de notre projet ont été importés et stockés dans un dossier partagé sur Google Drive, ce qui a facilité le travail d'équipe. "
  "</p>"
  "\n\n"
  "<p style='text-align: justify'>"
  "Le code a quant à lui été réalisé sur la plateforme Google Colab, ce qui a permis à l’ensemble du groupe de travailler de manière collaborative sur le projet avec la création de plusieurs notebooks, dont un notebook dédié au nettoyage des données et un notebook axé sur les visualisations et le machine learning."
  "</p>"
  "\n\n"
  "<p style='text-align: justify'>"
  "Nous avons utilisé le langage informatique <strong>Python</strong> et plusieurs librairies associées : <strong>Pandas</strong> et <strong>Numpy</strong> pour le traitement des données ; <strong>Matplotlib, Seaborn</strong> et <strong>Plotly</strong> pour la visualisation ; <strong>Scikit-Learn</strong> et <strong>Prophet</strong> pour le machine learning."
  "</p>"
  , unsafe_allow_html=True)

# Page Nettoyage des données
if page == pages[1] : 
  st.header("Nettoyage des données")
  st.write("<p style='text-align: justify'>"
  "Texte 1"
  "</p>"
  "\n\n"
  "<p style='text-align: justify'>"
  "Texte 2"
  "</p>"
  , unsafe_allow_html=True)

  st.dataframe(country_df_OWID_CO_CLEAN.head())


# Page Visualisations
if page == pages[2] : 
  st.header("Visualisations")
  viz1 = "Evolutions du climat"
  viz2 = "Rôle des activités humaines"
  viz3 = "Catastrophes naturelles"
  dataviz_page = st.radio("", (viz1, viz2, viz3))
  
  # Sous-page Evolutions du climat
  if dataviz_page == viz1:
    st.subheader("Evolutions du climat")
  
  # Sous-page Rôle des activités humaines
  if dataviz_page == viz2:
    st.subheader("Rôle des activités humaines")
    
    fig = px.line(world_df_OWID_CO_CLEAN,
    x='year',
    y='co2',
    labels={'co2': 'Evolution du co2', 'year': 'Année'},
    title='Evolution des émissions de dioxyde de carbone à la surface du globe (en millions de tonnes)',)
    fig.update_layout(
    xaxis=dict(title='Année'),
    yaxis=dict(title='Évolution des émissions de CO2 '),
    )
    st.plotly_chart(fig, use_container_width=True)
    
    fig = px.line(country_df_OWID_CO_CLEAN,
    x='year',
    y='co2',
    color='country',
    labels={'temp_SUM': 'Évolution de la température', 'year': 'Année'},
    title='Evolution des émissions de dioxyde de carbone par pays (en millions de tonnes)',)
    fig.update_layout(
    xaxis=dict(title='Année'),
    yaxis=dict(title='Évolution des émissions de CO2'),
    )
    st.plotly_chart(fig, use_container_width=True)

    df_repartition = world_df_OWID_CO_CLEAN[world_df_OWID_CO_CLEAN.year >= 2000]
    df_repartition.rename(columns={"cement_co2": "Ciment", "coal_co2": "Charbon", "flaring_co2": "Torchage", "gas_co2": "Gaz", "oil_co2": "Pétrole"}, inplace=True)
    st.dataframe(df_repartition.head())
    #plot = sns.barplot(data = df_repartition, y=['Ciment', 'Charbon', 'Torchage', 'Gaz', 'Pétrole'], x='year', stacked=True, linewidth=15)
    #plt.title("Répartition de l'origine des gaz à effet de serre entre 2000 et 2021")
    #plt.xlabel("Années")
    #plt.ylabel("Emissions en millions de tonnes")
    #st.pyplot(plot.get_figure())
    fig = plt.figure()
    sns.barplot(x=df_repartition['year'], y=df_repartition['Ciment'])
    st.pyplot(fig)

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

  # Sous-page Catastrophes naturelles
  if dataviz_page == viz3:
    st.subheader("Catastrophes naturelles")
    st.write("texte")

# Page Prédictions
if page == pages[3] : 
  st.header("Prédictions")
  pred1 = "Catastrophes naturelles"
  pred2 = "Températures"
  pred_page = st.radio("", (pred1, pred2))
  
  # Sous-page Catastrophes naturelles
  if pred_page == pred1:
    st.subheader("Catastrophes naturelles")
  
  # Sous-page Températures
  if pred_page == pred2:
    st.subheader("Températures")

# Page Conclusion et perspectives
if page == pages[4] : 
  st.header("Conclusion et perspectives")
  st.write("<p style='text-align: justify'>"
"Ce projet nous aura permis de visualiser par nous-mêmes les différentes composantes du réchauffement climatique. Nous avons notamment utilisé les librairies Pandas, Matplotlib, Seaborn et Plotly. Nous avons aussi choisi d’élargir le sujet, ou plus précisément de traiter la notion de dérèglement climatique en utilisant un jeu de données complémentaires, celles des catastrophes naturelles."
"</p>"
"\n\n"
"<p style='text-align: justify'>"
"Lors de la phase de Machine Learning, nous avons été confrontés aux limites des outils à notre disposition, compte tenu notamment du caractère temporel des données à traiter. Néanmoins, nous sommes parvenus à de premiers résultats, mais aussi à une prise de conscience des limites de nos modèles. Le réchauffement climatique est une problématique complexe et multifactorielle."
"</p>"
"\n\n"
"<p style='text-align: justify'>"
"D’autres modèles de Machine Learning plus complexes auraient peut-être pu nous permettre d’aboutir à des prédictions plus précises. Nous pensons notamment aux modèles ARIMA/SARIMA/SARIMAX, des modèles dédiés à l’étude des séries de données temporelles."
"</p>"
, unsafe_allow_html=True)
