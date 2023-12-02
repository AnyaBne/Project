import streamlit as st
import pandas as pd

# Charger le dataset
data = pd.read_csv('song_dataset.csv')

# Extraire les IDs uniques des utilisateurs
unique_user_ids = data['user'].unique()

# Initialisation des variables d'état
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'user_id' not in st.session_state:
    st.session_state.user_id = ''

# Exemple de liste de chansons
songs_list = ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5']

# Fonction pour générer des recommandations
def generate_recommendations(selected_songs):
    return [song for song in songs_list if song not in selected_songs][:3]

# Affichage de la page d'accueil
def show_home_page():
    st.title('Welcome to the Music Recommendation Engine')
    user_id = st.text_input('Enter your ID:', key="user_id_input")
    if st.button('Login'):
        if user_id in unique_user_ids:
            st.session_state.page = 'recommendation'
            st.session_state.user_id = user_id
        else:
            st.error('ID doesn\'t exist. Please try again.')

# Affichage de la page de recommandation
def show_recommendation_page():
    st.title('Music Recommendation Engine')
    st.write(f"Welcome {st.session_state.user_id}")
    if st.button('Back to Home'):
        st.session_state.page = 'home'
    else:
        selected_songs = st.multiselect('Select songs you like:', songs_list, key="selected_songs_multiselect")
        if st.button('Recommend Songs'):
            if selected_songs:
                recommendations = generate_recommendations(selected_songs)
                st.subheader('Recommended Songs for you:')
                for song in recommendations:
                    st.write(song)
            else:
                st.warning('Please select at least one song.')

# Contrôle de flux principal
if st.session_state.page == 'home':
    show_home_page()
elif st.session_state.page == 'recommendation':
    show_recommendation_page()
