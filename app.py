import streamlit as st
import pandas as pd

# Charger le dataset
data = pd.read_csv('song_dataset.csv')

# Extraire les IDs uniques des utilisateurs
unique_user_ids = data['user'].unique()

# Initialisation des états de session
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# Fonction pour afficher la page d'accueil
def show_home_page():
    st.title('Welcome to the Music Recommendation Engine')
    user_id = st.text_input('Enter your ID:', key="user_id_input")
    if st.button('Login', key='login_button'):
        if user_id in unique_user_ids:
            st.session_state.current_page = 'recommendation'
        else:
            st.error('ID doesn\'t exist. Please try again.')

# Fonction pour afficher la page de recommandation
def show_recommendation_page():
    st.title('Music Recommendation Engine')
    if st.button('Back to Home', key='back_home_button'):
        st.session_state.current_page = 'home'

# Affichage des pages en fonction de l'état
if st.session_state.current_page == 'home':
    show_home_page()
elif st.session_state.current_page == 'recommendation':
    show_recommendation_page()
