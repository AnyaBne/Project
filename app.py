import streamlit as st
import pandas as pd

# Charger le dataset
data = pd.read_csv('song_dataset.csv')

# Extraire les IDs uniques des utilisateurs
unique_user_ids = data['user'].unique()

# Exemple de liste de chansons
songs_list = ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5']

# Initialisation des états de session pour les actions de boutons
if 'action' not in st.session_state:
    st.session_state.action = ''

# Fonction pour générer des recommandations
def generate_recommendations(selected_songs):
    return [song for song in songs_list if song not in selected_songs][:3]

# Page d'accueil
st.title('Welcome to the Music Recommendation Engine')
if st.session_state.action == '' or st.session_state.action == 'back_to_home':
    user_id = st.text_input('Enter your ID:', key="user_id_input")
    if st.button('Login'):
        if user_id in unique_user_ids:
            st.session_state.action = 'login_success'
        else:
            st.error('ID doesn\'t exist. Please try again.')

# Page de recommandation
if st.session_state.action == 'login_success':
    if st.button('Back to Home'):
        st.session_state.action = 'back_to_home'
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
