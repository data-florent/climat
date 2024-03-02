import streamlit as st
#import pandas as pd
#import numpy as np

### Importation des dataframes

df = "à définir"

### Header
image_iceberg = Image.open('images/iceberg.jpg')
st.image(image_iceberg, use_column_width=True, width=500)
st.markdown(
"<h2 style='text-align: center'>"
"<strong>Le changement climatique</strong>"
"<br><span style='font-size: smaller'>et les catastrophes naturelles</span>"
"</h2>"
, unsafe_allow_html=True)


st.sidebar.title("Sommaire")
pages=["Présentation du projet", "DataVizualization", "Modélisation"]
page=st.sidebar.radio("Aller vers", pages)

if page == pages[0] : 
  st.write("### Présentation du projet")

if page == pages[1] : 
  st.write("### DataVizualization")

if page == pages[2] : 
  st.write("### Modélisation")