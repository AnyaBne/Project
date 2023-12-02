import streamlit as st
import pandas as pd

# Charger le dataset (assurez-vous que le chemin est correct)
data = pd.read_csv('song_dataset.csv')

# Extraire les IDs uniques des utilisateurs
unique_user_ids = data['user'].unique()

# Exemple de liste de chansons
songs_list = ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5']

# Fonction pour générer des recommandations
def generate_recommendations(selected_songs):
    return [song for song in songs_list if song not in selected_songs][:3]

# Initialisation de l'état de la session
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# Fonction pour afficher la page d'accueil
def show_home_page():
    st.title('Welcome to the Music Recommendation Engine')
    user_id = st.text_input('Enter your ID:', key="user_id_input")
    login_pressed = st.button('Login', key='login_button')
    if login_pressed:
        if user_id in unique_user_ids:
            st.session_state['page'] = 'recommendation'
        else:
            st.error('ID doesn\'t exist. Please try again.')

# Fonction pour afficher la page de recommandation
def show_recommendation_page():
    st.title('Music Recommendation Engine')
    back_pressed = st.button('Back to Home', key='back_home_button')
    if back_pressed:
        st.session_state['page'] = 'home'
    else:
        selected_songs = st.multiselect('Select songs you like:', songs_list, key="selected_songs_multiselect")
        recommend_pressed = st.button('Recommend Songs', key='recommend_button')
        if recommend_pressed:
            if selected_songs:
                recommendations = generate_recommendations(selected_songs)
                st.subheader('Recommended Songs for you:')
                for song in recommendations:
                    st.write(song)
            else:
                st.warning('Please select at least one song.')

# Affichage des pages en fonction de l'état
if st.session_state['page'] == 'home':
    show_home_page()
elif st.session_state['page'] == 'recommendation':
    show_recommendation_page()
