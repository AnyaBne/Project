import streamlit as st
import pandas as pd
import requests
import joblib
from io import BytesIO

# Charger le dataset
data = pd.read_csv('song_dataset.csv')

@st.cache
def load_model_from_gdrive(url):
    response = requests.get(url)
    model_stream = BytesIO(response.content)
    model = joblib.load(model_stream)
    return model

# Remplacez par votre lien de téléchargement direct
model_url = "https://drive.google.com/file/d/1eyXrYRk2PGi8qIeDeTzYEvXvy2iZ3kYe/view?usp=drive_link"  
model = load_model_from_gdrive(model_url)


# Extraire les IDs uniques des utilisateurs
unique_user_ids = data['user'].unique()

# Fonction pour obtenir des recommandations basées sur le modèle
def get_recommendations(user_id, n=10):
    # Récupération des chansons écoutées par l'utilisateur
    listened_songs = df[df['user'] == user_id]['song'].unique()
    
    # Création d'une liste de toutes les chansons que l'utilisateur n'a pas encore écoutées
    all_songs = df[~df['song'].isin(listened_songs)]['song'].unique()
    
    # Prédiction des notes pour les chansons non écoutées
    predictions = []
    for song in all_songs:
        predictions.append((song, algo.predict(user_id, song).est))
    
    # Tri des chansons en fonction des notes prédites et sélection des 'n' meilleures
    predictions.sort(key=lambda x: x[1], reverse=True)
    
    # Obtention des titres de chansons
    recommended_song_ids = [song for song, _ in predictions[:n]]
    recommended_songs = df[df['song'].isin(recommended_song_ids)][['song', 'title']].drop_duplicates().head(n)
    
    return recommended_songs

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
def show_recommendation_page(model):
    st.title('Music Recommendation Engine')
    st.write(f"Welcome user {st.session_state.get('user_id', '')}.")

    # Affichage des chansons recommandées
    if 'user_id' in st.session_state and st.session_state['user_id']:
        user_id = st.session_state['user_id']
        recommended_songs = get_recommendations(user_id, model)
        st.subheader('Recommended Songs for you:')
        for song in recommended_songs:
            st.write(song)

    if st.button('Back to Home', key='back_home_button'):
        st.session_state['page'] = 'home'

# Initialisation de l'état de la session
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'
if 'user_id' not in st.session_state:
    st.session_state['user_id'] = ''

# Affichage des pages en fonction de l'état
if st.session_state['page'] == 'home':
    show_home_page()
elif st.session_state['page'] == 'recommendation':
    show_recommendation_page(model)
