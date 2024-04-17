### Importation des librairies ###
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from scipy import stats
import joblib
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics

### Importation des dataframes ###

country_df_OWID_CO_CLEAN = pd.read_csv('datasets/country_df_OWID_CO_CLEAN.csv', sep=',')
df_temp_catnat_1950 = pd.read_csv('datasets/df_temp_catnat_1950.csv', sep=',')
df_temp_catnat_1950_month = pd.read_csv('datasets/df_temp_catnat_1950_month.csv', sep=',')
df_ML = pd.read_csv('datasets/df_temp_catnat_1950_month.csv', sep=',')
world_df_OWID_CO_CLEAN= pd.read_csv('datasets/world_df_OWID_CO_CLEAN.csv', sep=',')
df_global_annuel= pd.read_csv('datasets/df_global_annuel.csv', sep=',')
df_nord_hem_mean_annuel= pd.read_csv('datasets/df_nord_hem_mean_annuel.csv', sep=',')
df_sud_hem_mean_annuel= pd.read_csv('datasets/df_sud_hem_mean_annuel.csv', sep=',')
continent_df_OWID_CO_CLEAN= pd.read_csv('datasets/continent_df_OWID_CO_CLEAN.csv', sep=',')
EUROPE_country_df_OWID_CO_CLEAN = pd.read_csv('datasets/EUROPE_country_df_OWID_CO_CLEAN.csv', sep=',')
DF_NASA_EXEMPLE = pd.read_csv('datasets/DF_NASA_EXEMPLE.csv', sep=',')


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
  "<li>NETTOYAGE_DATA.ipynb"
  "<li>Code_Commun.ipynb"
  "<li>MachineLearning.ipynb"
  "</p>"
  "\n\n"
  , unsafe_allow_html=True)
  st.write("<p style='text-align: justify'>"
  "Nous avons utilisé le langage informatique <strong>Python</strong> et plusieurs librairies associées : <strong>Pandas</strong> et <strong>Numpy</strong> pour le traitement des données ; <strong>Matplotlib, Seaborn</strong> et <strong>Plotly</strong> pour la visualisation ; <strong>Scikit-Learn</strong> et <strong>Prophet</strong> pour le machine learning."
  "</p>"
  , unsafe_allow_html=True)





# Page Nettoyage des données
if page == pages[1] : 
  st.header("Nettoyage des données")
  st.write("<p style='text-align: justify'>"
  "Après analyse des données fournies, une première étape de nettoyage a été indispensable pour exploiter les jeux de données."
  "</p>"
  "\n\n"
  , unsafe_allow_html=True)
# Nettoyage DONNEE NASA 
#text
  st.subheader("1. Données de la NASA")
  st.write("<p style='text-align: justify'>"
  "Les données fournies par la NASA viennent de relevés de températures globaux, de l’hémisphère nord et de l’hémisphère sud. Ils comportent les variations de températures entre 2007 et 2016, calculées avec trois outils de mesures différents."
  "</p>"
  "\n\n"
  , unsafe_allow_html=True)
#text  
  st.write("<p style='text-align: justify'>"
  "Dans un premier temps, l'ensemble de données de la NASA a été divisé en plusieurs Datasets différents réparti en fonction de la temporalité et de la zone et des outils de mesures."
  "</p>"
  , unsafe_allow_html=True)
# affichage du dataframe
  st.dataframe(DF_NASA_EXEMPLE.head())
#text
  st.write("<p style='text-align: justify'>"
  "Après exploration des données à disposition avec diverses fonctions, nous avons pu constater que les Datasets contenaient peu de doublons, mais qu’ils contenaient des valeurs manquantes et beaucoup de caractères spéciaux."
  "<li>les caractères spéciaux ont donc été remplacés par des NaN. "
  "<li>Les lignes contenant des valeurs manquantes ont été supprimées. "
  "<li>les colonnes de type « object » ont été transformées en « float ». "
  "</p>"
  "\n\n"
  , unsafe_allow_html=True) 
  st.write("A noter que ces étapes de nettoyage ont été dupliquées sur l’ensemble des datasets."
  "</p>"
  "\n\n"
  "Par exemple:"
  , unsafe_allow_html=True) 
# affichage du code
  st.code('''
  # supprimer les caractere speciaux ***, en les transformant en NaN
  df_global_mean.replace('***', np.nan, inplace=True)

  # Supprimez les lignes contenant NaN
  df_global_mean.dropna(inplace=True)

  # transformer les colonnes object en float
  df_global_mean['Jan'] = df_global_mean['Jan'].astype(float)
  ''', language='python')
#text  
  st.write("<p style='text-align: justify'>"
  "Une fois les données nettoyées, des ensembles de données de travail ont ensuite été créés en fonction des relevés de température moyenne mensuelle, annuelle, saisonnière, par latitude, par hémisphère, par pays et des instruments de mesure (AIRSv6, AIRSv7, GHCNv4ERSSTv5)."
  "</p>"
  "\n\n"
  , unsafe_allow_html=True) 
  "\n\n"

	
### Nettoyage DONNEES OWID
  st.subheader("2. Données OWID")
#text
  st.write("<p style='text-align: justify'>"
  "Le Dataset OWID a également été importé puis a fait l’objet, comme précédemment, d’une analyse de données ainsi que d’un processus de nettoyage avec:"
  "<li>le remplacement des valeurs manquantes de la colonne iso_Code par “Autre”. (Les lignes ne contenant pas de code ISO correspondent à des régions ou des continents) "
  "<li>Le reste des données manquantes ont été remplacées par “0”."
  "</p>"
  "\n\n"  
  , unsafe_allow_html=True) 

# affichage du code
  st.code('''
   # remplacer les NAs
  df_OWID_CO_CLEAN = df_OWID_CO['iso_code'].fillna('AUTRE')
  df_OWID_CO_CLEAN = df_OWID_CO.fillna(0)
  ''', language='python')
#text	
  st.write("<p style='text-align: justify'>"
  "<li>Une nouvelle colonne qui reprend la somme des colonnes températures « temp_SUM » a été créée."
  "\n\n"
  "(A noter que les valeurs semblent correspondre à celles de la colonne « temperature_change_from_ghg », déjà présente dans le Dataset initial, mais sans certitude, nous avons préféré la créer par nous-mêmes.)"
  "</p>"
  , unsafe_allow_html=True) 
# affichage du code
  st.code('''
  # Créer la nouvelle colonne 'temp_SUM' avec la somme des colonnes temperatures = equivaut à la colonne 'temperature_change_from_ghg'
  df_OWID_CO_CLEAN['temp_SUM'] = df_OWID_CO_CLEAN[['temperature_change_from_ch4','temperature_change_from_co2','temperature_change_from_n2o']].sum(axis=1)
  ''', language='python')

#text
  st.write("<p style='text-align: justify'>"
  "Un nouveau Dataset contenant les latitudes et les longitudes des pays a été ajouté. Ce dernier a fait l’objet d’un nettoyage des données avec suppression des valeurs manquantes et des colonnes inutiles."
  "</p>"
  "\n\n"
  "Les lignes ont ensuite été filtrées par pays, par régions, par continents, par régions économiques et à l’échelle mondiale via la colonne « country » et stockées dans de nouveaux Datasets de travail."
  "</p>"
  "\n\n"
  , unsafe_allow_html=True)    
# affichage du dataframe
  st.dataframe(country_df_OWID_CO_CLEAN.head())


### Nettoyage DONNEES EMDAT
  st.subheader("3. Données EMDAT")
# text
  st.write("<p style='text-align: justify'>"
  "Enfin, nous avons importé le Dataset EMDAT recensant les catastrophes naturelles. Ce dernier a, lui aussi, fait l’objet d’une analyse de ses données pour être ensuite nettoyées. "
  "\n\n"
  , unsafe_allow_html=True) 
# affichage du dataframe 	
  st.dataframe(df_temp_catnat_1950.head())
  "\n\n"
# text	
  st.write("<p style='text-align: justify'>"
  "La présence de doublons et de valeurs manquantes a été vérifiée. Nous avons fait le choix de limiter le Dataset aux colonnes pertinentes, c’est-à-dire celles où les données manquantes sont peu nombreuses et permettront d’en tirer des analyses. A noter que certains noms de colonnes ont également été modifiés (afin d’en améliorer la lecture) et que les valeurs manquantes ont été remplacées par la médiane."
  "</p>"
  , unsafe_allow_html=True) 
# affichage du code
  st.code('''
  # LIMITATION du dataframe aux colonnes pertinentes, celles où les données manquantes sont peu nombreuses ET permettront des analyses
  df_EMDAT_CLEAN = df_emdat[["Disaster Group", "Disaster Subgroup", "Disaster Type", "Disaster Subtype", "ISO", "Country", "Subregion", "Region", "Start Year", "Total Deaths", "Total Affected", "Total Damage ('000 US$)"]]
  ''', language='python')
# text
  st.write("<p style='text-align: justify'>"
  "Des Datasets de travail ont ensuite été créés pour l’analyse, reprenant le nombre de catastrophes naturelles par année ainsi que la variation de température, le nombre total de morts, le nombre total de personnes affectées, le coût chiffré en milliers de dollars US induit, le nombre de catastrophes naturelles."
  "</p>" , unsafe_allow_html=True) 
# text
  st.write("<p style='text-align: justify'>"
  "Pour les modèles de Machine Learning, plusieurs dataset ont spécialement été créé, dont un seul sera présenté ici. Pour ce faire, le choix a été fait de supprimer les catastrophes pour lesquelles le mois n’est pas renseigné (nous gardons tout de même 98,4% des données initialement présentes dans le fichier des catastrophes naturelles dans le monde depuis 1950). "
  "</p>", unsafe_allow_html=True) 
  "\n\n"
# text
  st.write("<p style='text-align: justify'>"
  "A noter que les valeurs manquantes ont été remplacées par des 0 (pas de catastrophe naturelle). Également, les lignes les plus récentes (2022 et 2023) ont été supprimées car il fallait que l’intégralité des informations soit disponible (température, nombre de catastrophes mensuelles, CO2 et population)."
  "</p>", unsafe_allow_html=True) 
  "\n\n"
# affichage du code
  st.code('''
  # Changement du nom de la colonne 'Start Year' en 'Year'
  df_EMDAT_CLEAN = df_EMDAT_CLEAN.rename({'Start Year':'Year'}, axis=1)
  # CHOIX DE LA MEDIANE POUR REMPLACER LES VALEURS MANQUANTES DANS LES 3 VARIABLES TOTAL AFFECTED, TOTAL DEATHS ET TOTAL DAMAGE
  df_EMDAT_CLEAN = df_EMDAT_CLEAN.fillna(df_EMDAT_CLEAN.median())
  ''', language='python')
# text
  st.write("<p style='text-align: justify'>"
  "Il contient par année, le mois, la variation de température, le nombre de catastrophes mensuelles, la population, les émissions de CO2 en millions de tonnes, le cumul des émissions de CO2 en millions de tonnes."
  "</p>", unsafe_allow_html=True) 
  "\n\n"
  "\n\n"

### CONCLUSION
  st.subheader("Conclusion")
  st.write("<p style='text-align: justify'>"
  "Les datasets nouvellement créés sont sauvegardés sur notre drive commun, dans un dossier intitulé “DATASETS_CLEAN”, pour être utilisés par tous dans des feuilles de code séparées (essentiellement la feuille “Code_Commun”, mais aussi des feuilles individuelles permettant à chacun de pratiquer et d’expérimenter de son côté)."
  "\n\n"
  "</p>"
  , unsafe_allow_html=True) 







# Page Visualisations
# Liste des pages

if page == pages[2] : 
  st.header("Visualisations")
  viz1 = "Evolutions du climat"
  viz2 = "Rôle des activités humaines"
  viz3 = "Catastrophes naturelles"
  dataviz_page = st.radio("", (viz1, viz2, viz3))
  
  # Sous-page Evolutions du climat
  if dataviz_page == viz1:
    st.subheader("Evolutions du climat")
  
    st.markdown("<h3>1. Evolution de la température moyenne de la Terre</h3>"
    , unsafe_allow_html=True)

    fig = plt.figure(figsize =(15,8))
    sns.lineplot(x=df_global_annuel["Year"], y=df_global_annuel["J-D"], data=df_global_annuel, color = '#5a86ad', label="Global")
    plt.ylabel("Index de Variation de Température")
    plt.xlabel("Années")
    plt.title("Evolution des températures terrestres globales")
    st.pyplot(fig, use_container_width=True)

    st.markdown(
    "<p style='text-align: justify'>"
    "Les températures semblent globalement stables jusque dans les années 1940, puis un pic d'augmentation se dessine entre les années 1940 et 1950. A partir de cette période, les températures augmentent de manière constante."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "Une des causes de ce réchauffement global est dûe aux activités humaines. Ainsi, les émissions de GES (gaz à effet de serre), entre autres, ont augmenté au cours du XXe siècle et conservent la même tendance au XXIe siècle. Ceci participe au réchauffement global planétaire. A noter que ce réchauffement n'est pas uniforme et peut varier entre les régions et les hémisphères."
    "</p>"
    , unsafe_allow_html=True)

    fig = plt.figure(figsize =(15,8))
    sns.lineplot(x=df_nord_hem_mean_annuel["Year"], y=df_nord_hem_mean_annuel["J-D"], data=df_nord_hem_mean_annuel, color= '#ff81c0', label="Hémisphère Nord")
    sns.lineplot(x=df_sud_hem_mean_annuel["Year"], y=df_sud_hem_mean_annuel["J-D"], data=df_sud_hem_mean_annuel, color = '#53fca1', label="Hémisphère Sud")
    plt.ylabel("Index de Variation de Température")
    plt.xlabel("Années")
    plt.title("Evolution des températures terrestre de l'hémisphère Nord et l'hémisphère Sud")
    st.pyplot(fig, use_container_width=True)

    st.markdown(
    "<p style='text-align: justify'>"
    "L'augmentation des températures est plus importante aujourd'hui dans l'hémisphère nord que dans l’hémisphère sud. Il s’avère qu’au XXe siècle, les variations de températures étaient assez similaires partout sur le globe."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "C'est à partir de la fin du XXe siècle que l'hémisphère nord dépasse l'hémisphère sud en termes d’augmentation de températures. Ce dépassement correspond également à une augmentation de plus en plus forte des températures dans l'hémisphère nord."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "En outre, l'hémisphère sud semble démarrer son ascension dans les années 1940, soit 20 ans après l'hémisphère nord."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "Il pourrait y avoir plusieurs explications à cette différence entre nord et sud : "
    "<ul>"
    "<li>les activités humaines sont plus condensées sur l'hémisphère nord ;</li>"
    "<li>la proportion de terres émergées est plus importante au nord ;</li>"
    "<li>les terres se réchauffent et refroidissent plus rapidement que l'eau, ce qui peut influencer les différences de température entre les deux hémisphères.</li>"
    "</ul>"
    "</p>"
    , unsafe_allow_html=True)

    st.markdown("<h3>Heatmap mettant en évidence les corrélations</h3>"
    , unsafe_allow_html=True)

# HEATMAP
#calcule la matrice de correlation	  
    cor = country_df_OWID_CO_CLEAN[["temp_SUM",'co2',"primary_energy_consumption",'gdp','population']].corr()
#creation de la heatmap
    fig, ax = plt.subplots(figsize = (6,6))
    sns.heatmap(cor, annot = True, ax = ax, cmap = "Reds")
#amelioration de la lisibilité
    ax.set_xticklabels(['Variation de Température', 'CO2', 'Consommation énergie', 'PIB', 'Population'], rotation=45, ha='right')
    ax.set_yticklabels(['Variation de Température', 'CO2', 'Consommation énergie', 'PIB', 'Population'], rotation=0, va='center')
    fig.patch.set_facecolor('#b0c7d1')

#affiche
    st.pyplot(fig, use_container_width=True)

    st.markdown(
    "<p style='text-align: justify'>"
    "Le changement de la température moyenne à la surface du globe (en °C) causé par l'activité humaine semble être fortement corrélé avec les émissions totales de dioxyde de carbone (Co2)."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "On remarque aussi un lien clair entre la consommation d'énergie primaire et le PIB d'un pays. En effet, plus un pays est riche et développé, plus il consomme d'énergie, et donc plus il produit du dioxyde de carbone. De ce fait, sa responsabilité dans le changement global de la température terrestre s'accroît."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "A l’inverse, la population ne semble pas être corrélée de manière significative avec les autres facteurs."
    "</p>"
    , unsafe_allow_html=True)

    st.markdown("<h3>2. Les différentes régions et l'évolution de la température</h3>"
    , unsafe_allow_html=True)

# FIG VARIATION DE LA TEMPERTURE MOYENNE WORLD WIDE
    continent_df_OWID_CO_CLEAN = continent_df_OWID_CO_CLEAN[continent_df_OWID_CO_CLEAN['regions'] != 'World']
    fig = px.line(continent_df_OWID_CO_CLEAN,
        x='year',
        y='temp_SUM',
        color='regions',
        labels={'temp_SUM': 'Évolution de la température', 'year': 'Année'},
        title='Variation de la température moyenne à la surface du globe (en °C)',
    )
    fig.update_layout(
        xaxis=dict(title='Année'),
        yaxis=dict(title='Évolution de la température'),
        width=800,
        height=600,
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
    "<p style='text-align: justify'>"
    "Ce graphique montre que l’Asie est en tête au niveau de l'évolution de la température, suivie par l'Amérique du Nord et par l'Europe."
    "</p>"
    , unsafe_allow_html=True)

# FIG VARIATION DE LA TEMPERTURE MOYENNE EUROPE
    fig = px.line(EUROPE_country_df_OWID_CO_CLEAN,
        x='year',
        y='temp_SUM',
        color='country',
        labels={'temp_SUM': 'Évolution de la température', 'year': 'Année'},
        title="Variation de la température moyenne à la surface du globe (en °C) pour les pays d'Europe",
    )
    fig.update_layout(
        xaxis=dict(title='Année'),
        yaxis=dict(title='Évolution de la température '),
        width=600,
        height=600,
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
    "<p style='text-align: justify'>"
    "En Europe, nous constatons que l'Allemagne est en tête en ce qui concerne l'augmentation des températures dûes aux gaz à effet de serre. Elle est suivie par la France, la Pologne et l'Italie."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "Cela peut notamment s’expliquer par le fait que l’Allemagne est l’un des pays les plus riches du continent et que le charbon occupe une place importante dans son mix énergétique."
    "</p>"
   , unsafe_allow_html=True)

    sorted_country_df_OWID_CO_CLEAN = country_df_OWID_CO_CLEAN.sort_values(by=['year'], ascending=True)
    sorted_country_df_OWID_CO_CLEAN = sorted_country_df_OWID_CO_CLEAN.loc[sorted_country_df_OWID_CO_CLEAN['year']>=1851]
    custom_color_scale = ["#60a35a", "#FFA500", "#c72222"]
    fig = px.choropleth(sorted_country_df_OWID_CO_CLEAN,
                        locationmode='ISO-3', locations='iso_code',
                        color='temp_SUM',
                        range_color=[0, 0.1],
                        color_continuous_scale=custom_color_scale,
                        hover_name='country', projection='natural earth', animation_frame='year',
                        title='Variation de la température due aux gaz à effet de serre')
    fig.update_layout(width=1100, height=520)
    fig.update_coloraxes(colorbar_title='Variation de la Temperature')
    fig.update_layout(updatemenus=[dict(type='buttons', showactive=False,
                                      buttons=[dict(label='Play',
                                                    method='animate',
                                                    args=[None, dict(frame=dict(duration=30, redraw=True), fromcurrent=True)]),
                                              dict(label='Pause',
                                                    method='animate',
                                                    args=[[None], dict(frame=dict(duration=0, redraw=True), mode='immediate', transition=dict(duration=0))])])])
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
    "<p style='text-align: justify'>"
    "Cette représentation graphique permet de voir les variations de température à l’échelle mondiale par année depuis 1851. A noter que les résultats viennent confirmer les données constatées dans les précédentes courbes."
    "</p>"
    , unsafe_allow_html=True)

    

# Sous-page Rôle des activités humaines
  if dataviz_page == viz2:
    st.subheader("Rôle des activités humaines")
    
    st.markdown("<h3>1. Evolution des émissions de CO2 à l'échelle mondiale et par pays</h3>"
    "<p style='text-align: justify'>"
    "Les activités humaines ont un impact important sur le réchauffement climatique. En effet, la combustion des énergies fossiles, l'utilisation des engrais dans le cadre de l'agriculture, mais également les transports et l'industrie sont source d'émissions de GES qui viennent perturber l'équilibre climatique."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "On ne présente plus le co2, principal gaz à effet de serre persistant et qui constitue un indicateur de contexte majeur concernant l'enjeu du changement climatique."
    "</p>"
    , unsafe_allow_html=True)

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
    
    st.markdown(
    "<p style='text-align: justify'>"
    "Ce graphique nous montre une certaine stabilité des émissions de dioxyde de carbone à l'échelle mondiale entre 1750 et 1875. Ces dernières étaient alors proches de 0."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "C'est à partir des années 1875 qu'on observe une augmentation des émissions avec l'ouverture du premier âge industriel pour atteindre 5 milliards de tonnes en 1950. A partir de cette date, la courbe est éloquente et la croissance des émissions est exponentielle : elle culminera à 37 milliards de tonnes en 2021. Il convient de noter une relative accalmie en 2020 (-2 milliards de tonnes versus 2019) qui s'explique par la pandémie de COVID-19. Toutefois, le niveau de 2019 sera rattrapé dès 2021."
    "</p>"
    , unsafe_allow_html=True)

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

    st.markdown(
    "<p style='text-align: justify'>"
    "Ce graphique nous montre comment ont évolué les émissions de dioxyde de carbone de 1750 à nos jours et ceci à travers le monde."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "On constate une légère hausse des émissions de CO2 de l'Angleterre, premier pays à avoir connu sa révolution industrielle, dès les années 1850. L’Angleterre est dépassée par les Etats-Unis à partir des années 1900 qui connaissent alors une envolée vertigineuse jusque dans les années 2005 où une baisse s'opère alors jusqu'en 2020 où les émissions retrouvent leur niveau des années 1990."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "Sur la même période, la Chine récupère la première place avec des émissions de gaz à effet de serre qui augmentent de manière exponentielle pour arriver de nos jours à 12M de tonnes, soit deux fois plus que les Etats-Unis. L'Inde se place en troisième position avec 2,7M de tonnes."
    "</p>"
    , unsafe_allow_html=True)

    st.markdown("<h3>2. Répartition de l'origine des GES (gaz à effet de serre)</h3>"
    , unsafe_allow_html=True)

    df_repartition = world_df_OWID_CO_CLEAN[world_df_OWID_CO_CLEAN.year >= 2000]
    df_repartition.rename(columns={"cement_co2": "Ciment", "coal_co2": "Charbon", "flaring_co2": "Torchage", "gas_co2": "Gaz", "oil_co2": "Pétrole"}, inplace=True) 
    graph = df_repartition[['year', 'Ciment', 'Charbon', 'Torchage', 'Gaz', 'Pétrole']].plot.barh(
    x='year',
    title="Répartition de l'origine des gaz à effet de serre entre 2000 et 2021",
    ylabel="Années",
    xlabel="Emissions en millions de tonnes",
    stacked=True).figure
    st.pyplot(graph, use_container_width=True)

    st.markdown(
    "<p style='text-align: justify'>"
    "Nous constatons que la source la plus importante d’émissions de GES est incontestablement le charbon, suivi de près par le pétrole. Le gaz arrive en troisième position et ne représente que la moitié des émissions liées au pétrole. Arrivent enfin le ciment et le torchage, qui ne constituent qu’une très faible partie des émissions."
    "</p>"
    , unsafe_allow_html=True)

    st.markdown("<h3>3. Contribution des pays au réchauffement climatique</h3>"
    , unsafe_allow_html=True)

# figure map
    sorted_country_df_OWID_CO_CLEAN = country_df_OWID_CO_CLEAN.sort_values(by=['year'], ascending=True)
    sorted_country_df_OWID_CO_CLEAN = sorted_country_df_OWID_CO_CLEAN.loc[sorted_country_df_OWID_CO_CLEAN['year']>=1851]
    
    fig = px.choropleth(sorted_country_df_OWID_CO_CLEAN,
                    locationmode='country names', locations='country',
                    color='share_of_temperature_change_from_ghg',
                    color_continuous_scale=px.colors.sequential.Bluered,
                    range_color=[0,15], # permet de garder la même échelle pour toutes les années
                    hover_name='country', projection='natural earth', animation_frame='year',
                    title='Part (en %) de contribution au réchauffement climatique, basée sur les émissions de GES')
    fig.update_coloraxes(colorbar_title='Variation due aux GES')
    fig.update_layout(width=1100, height=520)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
    "<p style='text-align: justify'>"
    "Les Etats-Unis s'imposent comme le premier pays contributeur au réchauffement climatique dès 1851."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "Des pays comme la Russie, le Brésil, l'Inde et la Chine deviennent également des contributeurs importants après la seconde guerre mondiale. La Chine en particulier est le pays dont la progression est la plus spectaculaire."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "Enfin, certaines régions du monde contribuent peu au réchauffement climatique, notamment l'Afrique."
    "</p>"
    , unsafe_allow_html=True)

    st.markdown("<h3>4. Emissions de GES par individu selon les pays</h3>"
    , unsafe_allow_html=True)

    sorted_country_df_OWID_CO_CLEAN = sorted_country_df_OWID_CO_CLEAN.loc[(sorted_country_df_OWID_CO_CLEAN['year']>=1990)&(sorted_country_df_OWID_CO_CLEAN['year']<=2019)]
    fig = px.choropleth(sorted_country_df_OWID_CO_CLEAN,
                    locationmode='country names', locations='country',
                    color='ghg_per_capita',
                    color_continuous_scale=px.colors.sequential.Bluered,
                    range_color=[0,25], # permet de garder la même échelle pour toutes les années
                    hover_name='country', projection='natural earth', animation_frame='year',
                    title='Emissions de GES par individu selon les pays')
    fig.update_coloraxes(colorbar_title='GES par habitant')
    fig.update_layout(width=1100, height=520)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(
    "<p style='text-align: justify'>"
    "Chaque citoyen du monde n'émet pas la même quantité de GES. Les personnes qui émettent le plus de GES proviennent le plus souvent de pays riches (Canada, Australie, Etats-Unis, etc.) et/ou de pays dont l'économie est basée sur les énergies fossiles (Vénézuela, Libye, Turkménistan, etc.)."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "A l'inverse, chaque citoyen indien émet très peu de GES. Cela pourrait s'expliquer par la pauvreté et le faible niveau de vie en Inde, et donc par la faible consommation d'énergie rapportée au nombre d'habitants de ce pays."
    "</p>"
    , unsafe_allow_html=True)

  # Sous-page Catastrophes naturelles
  if dataviz_page == viz3:
    st.subheader("Catastrophes naturelles")

    fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharey=True)
    plt.setp(axes, ylabel='label')
    fig.suptitle("Variables en fonction de l'évolution de la température moyenne annuelle de 1950 à 2022 (période de référence: 1951-1980)")

    # Nombre de catastrophes naturelles
    sns.regplot(ax=axes[0,0], data=df_temp_catnat_1950, x="Nombre", y="J-D")
    axes[0,0].set_ylabel('Evolution de la température en °C vs période de référence')
    axes[0,0].set_xlabel('Nombre annuel de catastrophes naturelles')
    axes[0,0].set_title('Nombre de catastrophes')

    # Dégâts
    sns.regplot(ax=axes[0,1], data=df_temp_catnat_1950, x="Total Damage ('000 US$)", y="J-D")
    axes[0,1].set_ylabel('')
    axes[0,1].set_xlabel('Montant annuel des dégâts en k$')
    axes[0,1].set_title('Montant des dégâts')

    # Personnes affectées
    sns.regplot(ax=axes[1,0], data=df_temp_catnat_1950, x="Total Affected", y="J-D")
    axes[1,0].set_ylabel('Evolution de la température en °C vs période de référence')
    axes[1,0].set_xlabel('Nombre annuel de personnes affectées')
    axes[1,0].set_title('Personnes affectées')

    # Décès
    sns.regplot(ax=axes[1,1], data=df_temp_catnat_1950, x="Total Deaths", y="J-D")
    axes[1,1].set_ylabel('')
    axes[1,1].set_xlabel('Nombre annuel de décès')
    axes[1,1].set_title('Décès');

    st.pyplot(fig, use_container_width=True)

    st.markdown(
    "<p style='text-align: justify'>"
    "Il semble y avoir une corrélation forte entre l'évolution annuelle moyenne de la température (par rapport à la période de référence) et le nombre de catastrophes naturelles enregistrées. Ainsi, plus une année est chaude, et plus elle compte de catastrophes naturelles."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "Il semble également y avoir une corrélation entre l'évolution annuelle moyenne de la température et le coût des dégâts. Cependant, il convient de noter qu'un nombre important d'années entre 1950 et 2022 se caractérise à la fois par une variation quasi-nulle de la température et par un coût climatique très faible."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "La même analyse peut être exposée pour le lien entre l'évolution annuelle moyenne de la température et le nombre annuel de personnes affectées par les catastrophes naturelles. Néanmoins, les points du nuage s'écartent davantage de la droite que dans le cas précédent. La corrélation semble ainsi un peu moins marquée."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "Enfin, il semble ne pas exister de corrélation entre l'évolution annuelle moyenne de la température et le nombre annuel de décès liés aux catastrophes naturelles. En effet, la quasi-totalité des points du nuage se concentre en bas à gauche de la figure. Cela traduit le fait que seules quelques rares années présentent un bilan humain lourd ; peu de morts sont à déplorer dans la quasi-totalité des années."
    "</p>"
    "\n\n"
    "<h3>Tests statistiques</h3>"
    "<p style='text-align: justify'>"
    "Nous avons utilisé le test de Pearson pour déterminer le niveau de corrélation entre la variable température et chacune des quatre variables précédemment affichées dans les graphiques. Pour chacune des trois premières variables (nombre de catastrophes ; coût matériel des catastrophes ; nombre de personnes affectées), la p-valeur est inférieure à 0.05, donc on rejette H0 (x et y pas corrélées) et on accepte H1 (x et y corrélées). Il existe ainsi une corrélation positive entre les variables."
    "</p>"
    , unsafe_allow_html=True)

    # Utilisation du test statistique de Pearson
    x= df_temp_catnat_1950['J-D']
    y= df_temp_catnat_1950['Nombre']
    st.write("Exemple du test de Pearson entre la température et le nombre de catastrophes naturelles :", stats.pearsonr(x,y))

    st.markdown(
    "<p style='text-align: justify'>"
    "A l’inverse, pour la quatrième variable (nombre de décès), la p-valeur est supérieure à 0.05, donc l'hypothèse H0 (x et y pas corrélées) n'est pas rejetée. On ne retient donc pas de corrélation entre les deux variables température / nombre de décès."
    "</p>"
    , unsafe_allow_html=True)

    # Utilisation du test statistique de Pearson
    x= df_temp_catnat_1950['J-D']
    y= df_temp_catnat_1950['Total Deaths']
    st.write("Test de Pearson entre la température et le nombre de décès :", stats.pearsonr(x,y))

# Page Prédictions
if page == pages[3] : 
  st.header("Prédictions")
  pred1 = "Catastrophes naturelles"
  pred2 = "Températures"
  pred_page = st.radio("", (pred1, pred2))
  
  # Sous-page Catastrophes naturelles
  if pred_page == pred1:
    st.subheader("Catastrophes naturelles")
  
    st.markdown("<h3>1. Introduction</h3>"
    "<p style='text-align: justify'>"
    "L'objectif principal de cette analyse est de développer un modèle de prédiction capable d'estimer le nombre de catastrophes naturelles sur une période donnée. Pour ce faire nous avons utilisé des données provenant du dataset EMDAT recensant les catastrophes naturelles."
    "</p>"
    "\n\n"
    , unsafe_allow_html=True)

    st.markdown("<h3>2. Traitement des données</h3>"
    "<p style='text-align: justify'>"
    "L'objectif principal de cette analyse est de développer un modèle de prédiction capable d'estimer le nombre de catastrophes naturelles sur une période donnée.  Les données sont triées chronologiquement et nettoyées pour être appliquées au modèle Prophet (librairie qui permet la prévision des données de séries temporelles en tenant compte notamment des variations saisonnières)."
    "</p>"
    "\n\n"
    , unsafe_allow_html=True)

    st.markdown("<h3>3. Modélisation</h3>"
    "<p style='text-align: justify'>"
    "Le modèle Prophet est entraîné sur une période de 17 ans (2005-2021) et utilisé pour faire des prédictions sur les 5 années suivantes (2022-2026)."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "Sur le graphique, les points noirs représentent les vraies valeurs (nombres mensuels de catastrophes naturelles). La ligne bleu foncé représente la prédiction du modèle."
    "</p>"
    , unsafe_allow_html=True)

    df_ML = df_ML.sort_values(['Year', 'Month'], ascending=True).reset_index()
    df_ML_P = df_ML[['Year', 'Month', 'Nombre']]
    df_ML_P['Day'] = 1
    ds = pd.to_datetime(df_ML_P[["Year", "Month", "Day"]])
    df_ML_P['ds'] = ds
    df_ML_P['y'] = df_ML_P['Nombre']
    df_ML_P = df_ML_P[['ds', 'y']]
    model = Prophet(interval_width=0.95)
    model.fit(df_ML_P.iloc[660:])
    future_dates = model.make_future_dataframe(periods=60, freq='MS')
    forecast = model.predict(future_dates)
    #model.plot(forecast, uncertainty=True)

    fig = plt.figure(figsize =(15,8))
    sns.lineplot(x=forecast["ds"], y=forecast["yhat"], data=forecast, color= 'blue', label="Prédictions")
    sns.lineplot(x=df_ML_P.iloc[660:]["ds"], y=df_ML_P.iloc[660:]["y"], data=df_ML_P.iloc[660:], color= 'black', marker='o', linestyle='', label="Vraies valeurs")
    plt.ylabel("Nombre de catastrophes naturelles")
    plt.xlabel("Années")
    plt.title("Nombre de catastrophes naturelles")
    st.pyplot(fig, use_container_width=True)

    st.markdown(
    "<p style='text-align: justify'>"
    "Par souci de lisibilité, nous utilisons la librairie Plotly Express pour représenter uniquement la dernière partie de la courbe, qui porte sur les prédictions de la période 2022 à 2026."
    "</p>"
    "\n\n"
    , unsafe_allow_html=True)

    fig = px.line(forecast.iloc[-60:],
    x='ds',
    y='yhat',
    labels={'ds': 'Mois', 'yhat': 'Nombre de catastrophes'},
    title='Prédiction du nombre de catastrophes naturelles (2022-2026)',)
    fig.update_layout(
    xaxis=dict(title='Année'),
    yaxis=dict(title='Nombre de catastrophes naturelles '),
    width=1000,
    height=500,)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("<h3>Performance du modèle</h3>"
    "<p style='text-align: justify'>"
    "La performance du modèle est évaluée en utilisant des techniques de validation croisée. Les prédictions sont comparées aux vraies valeurs sur des périodes spécifiques et différentes métriques de performance sont calculées."
    "</p>"
    "\n\n"
    "<p style='text-align: justify'>"
    "L’écart entre les valeurs prédites et les valeurs réelles est évalué par les métriques telles que la MAPE (Mean Absolute Percentage Error), moyenne des écarts en valeur absolue par rapport aux valeurs observées. "
    "</p>"
    , unsafe_allow_html=True)

    df_cv = cross_validation(model, initial='3650 days', period='180 days', horizon = '1825 days')
    df_pm = performance_metrics(df_cv)
    st.dataframe(df_pm.head())
    st.dataframe(df_pm.tail())
    st.markdown('<br><strong>Choix de la métrique</strong><br>', unsafe_allow_html=True)
    metrique = st.selectbox('Sélectionnez la métrique :', ('mse', 'rmse', 'mae', 'mape', 'mdape', 'smape', 'coverage'))

    fig = plt.figure(figsize =(15,8))
    sns.lineplot(x=df_pm.index, y=df_pm[metrique], data=df_pm, color= 'blue')
    plt.ylabel(metrique)
    plt.xlabel("Horizon (days)")
    plt.xticks([0,24,72,120,168,216], [181,364,729,1094,1460,1825])
    plt.title(metrique)
    st.pyplot(fig, use_container_width=True)

    st.markdown(
    "<p style='text-align: justify'>"
    "Pour la MAPE, on peut observer que l'écart entre les vraies valeurs et les prédictions est d'environ 25 % pour les 2 premières années, puis d'environ 35 % pour les 3 années suivantes."
    "</p>"
    "\n\n"
    , unsafe_allow_html=True)

    st.markdown("<h3>4. Conclusion</h3>"
    "<p style='text-align: justify'>"
    "En conclusion, ce modèle présente des performances acceptables. Son processus de modélisation aboutit à un modèle de prédiction capable d'estimer le nombre de catastrophes naturelles sur une période donnée. Le modèle a toutefois tendance à fournir une plage étroite de valeurs : nous constatons qu’un nombre significatif de points noirs (correspondant aux valeurs réelles) se trouve très au-dessus ou très en dessous de la courbe de prédictions de Prophet."
    "</p>"
    , unsafe_allow_html=True)

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
