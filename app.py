import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#import plotly.express as px

df = "à définir"

st.title("Projet data sur le changement climatique et les catastrophes naturelles")
st.sidebar.title("Sommaire")
pages=["Exploration", "DataVizualization", "Modélisation"]
page=st.sidebar.radio("Aller vers", pages)

if page == pages[0] : 
  st.write("### Introduction")

if page == pages[1] : 
  st.write("### DataVizualization")

if page == pages[2] : 
  st.write("### Modélisation")