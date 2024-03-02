import streamlit as st
#import pandas as pd
#import numpy as np

df = "à définir"

st.title("Projet data sur le changement climatique et les catastrophes naturelles")
st.sidebar.title("Sommaire")
pages=["Présentation du projet", "DataVizualization", "Modélisation"]
page=st.sidebar.radio("Aller vers", pages)

if page == pages[0] : 
  st.write("### Présentation du projet")

if page == pages[1] : 
  st.write("### DataVizualization")

if page == pages[2] : 
  st.write("### Modélisation")