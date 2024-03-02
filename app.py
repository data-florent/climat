### Importation des librairies ###
import streamlit as st

### Importation des dataframes ###

df = "à définir"

### Header ###
st.image('images/iceberg.jpg', use_column_width=True, width=640)
st.markdown(
"<h2 style='text-align: center'>"
"<strong>Le changement climatique</strong>"
"<br><span style='font-size: smaller'>et les catastrophes naturelles</span>"
"</h2>"
, unsafe_allow_html=True)

### Menu latéral et création des pages ###
st.sidebar.title("Changement climatique & catastrophes naturelles")
pages=["Présentation du projet", "DataVizualization", "Modélisation"]
page=st.sidebar.radio("Sommaire",pages)
st.sidebar.info(
"Auteurs du projet :"
"\n\n"
"Laura "
"[linkedIn](https://www.linkedin.com/) "
"\n\n"
"Marion "
"[linkedIn](https://www.linkedin.com/) "
"\n\n"
"Florent "
"[linkedIn](https://www.linkedin.com/)"
"\n\n"
"Romain "
"[linkedIn](https://www.linkedin.com/)"
"\n\n"
"Projet fil rouge Data Analyst avril 2024, "
"[DataScientest](https://datascientest.com/)"
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
  st.write("### DataVizualization")

if page == pages[2] : 
  st.write("### Modélisation")