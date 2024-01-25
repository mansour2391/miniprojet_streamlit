import streamlit as st 
import pandas as pd ##Exploration de données
import plotly.express as px

def mains(): 
    st.subheader('les Donnees scraper sur beautifulsoup4 ')
    
    #### Partie A : Exploration de notre Dataset
    customers=pd.read_csv('healthcare-dataset-stroke-data.csv')

    st.sidebar.write("----")
    st.sidebar.title('GROUPE 1 : MANSOUR SOW - ALIOU BA ')
    st.sidebar.write("----")
    st.title('Projet Scraping avec  Streamlit en Licence 2_DIT ')
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)
    taches=['1. Exploration de données', '2. Représentations graphiques']
    choix=st.sidebar.selectbox('Selectionner une activité:', taches)
    st.subheader(choix)
    st.write("-----")
    if choix=='1. Exploration de données':
        affichages =['Afficher le dataset', 'Afficher les colonnes', 'Afficher Les variables', 'Le type des variables', 'Faire un summarise des données']
        affichage_select = st.sidebar.selectbox('Selectionner un affichage:', affichages)






mais()