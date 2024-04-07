### Importation des librairies ###
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from scipy import stats
from joblib import load

### Importation des dataframes ###

country_df_OWID_CO_CLEAN = pd.read_csv('datasets/country_df_OWID_CO_CLEAN.csv', sep=',')
df_temp_catnat_1950 = pd.read_csv('datasets/df_temp_catnat_1950.csv', sep=',')
df_temp_catnat_1950_month = pd.read_csv('datasets/df_temp_catnat_1950_month.csv', sep=',')
world_df_OWID_CO_CLEAN= pd.read_csv('datasets/world_df_OWID_CO_CLEAN.csv', sep=',')
df_global_annuel= pd.read_csv('datasets/df_global_annuel.csv', sep=',')
df_nord_hem_mean_annuel= pd.read_csv('datasets/df_nord_hem_mean_annuel.csv', sep=',')
df_sud_hem_mean_annuel= pd.read_csv('datasets/df_sud_hem_mean_annuel.csv', sep=',')
continent_df_OWID_CO_CLEAN= pd.read_csv('datasets/continent_df_OWID_CO_CLEAN.csv', sep=',')
EUROPE_country_df_OWID_CO_CLEAN= pd.read_csv('datasets/EUROPE_country_df_OWID_CO_CLEAN.csv', sep=',')

### Chargement des modèles de machine learning ###

model_1 = joblib.load('./model_1.joblib')

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

    cor = country_df_OWID_CO_CLEAN[["temp_SUM",'co2',"primary_energy_consumption",'gdp','population']].corr()
    fig, ax = plt.subplots(figsize = (10,10))
    sns.heatmap(cor, annot = True, ax = ax, cmap = "coolwarm")
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
        width=800,
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
    fig.update_layout(width=1000, height=800)
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
