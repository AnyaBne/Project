import streamlit as st
import pandas as pd

# Charger le dataset
data = pd.read_csv('song_dataset.csv')

# Extraire les IDs uniques des utilisateurs
unique_user_ids = data['user'].unique()

# Exemple de liste de chansons
songs_list = ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5']

# Fonction pour générer des recommandations
def generate_recommendations(selected_songs):
    return [song for song in songs_list if song not in selected_songs][:3]

# Fonction pour afficher la page d'accueil
def show_home_page():
    st.title('Welcome to the Music Recommendation Engine')
    user_id = st.text_input('Enter your ID:', key="user_id_input")
    if st.button('Login', key='login_button'):
        if user_id in unique_user_ids:
            st.session_state['page'] = 'recommendation'
            st.session_state['user_id'] = user_id  # Stocker l'ID de l'utilisateur dans l'état de la session
        else:
            st.error('ID doesn\'t exist. Please try again.')

# Fonction pour afficher la page de recommandation
def show_recommendation_page():
    st.title('Music Recommendation Engine')

    # Afficher le message de bienvenue avec l'ID de l'utilisateur
    st.write(f"Welcome user {st.session_state.get('user_id', '')}.")

    if st.button('Back to Home', key='back_home_button'):
        st.session_state['page'] = 'home'
    selected_songs = st.multiselect('Select songs you like:', songs_list, key="selected_songs_multiselect")
    if st.button('Recommend Songs', key='recommend_button'):
        if selected_songs:
            recommendations = generate_recommendations(selected_songs)
            st.subheader('Recommended Songs for you:')
            for song in recommendations:
                st.write(song)
        else:
            st.warning('Please select at least one song.')

# Initialisation de l'état de la session
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'
if 'user_id' not in st.session_state:
    st.session_state['user_id'] = ''

# Affichage des pages en fonction de l'état
if st.session_state['page'] == 'home':
    show_home_page()
elif st.session_state['page'] == 'recommendation':
    show_recommendation_page()
