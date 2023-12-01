import streamlit as st

# Exemple de liste de chansons
songs_list = ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5']

# Fonction pour générer des recommandations
def generate_recommendations(selected_songs):
    # Implémentez votre logique ici
    # Cette fonction est simplifiée pour l'exemple
    recommended_songs = [song for song in songs_list if song not in selected_songs]
    return recommended_songs[:3]  # Retourne les 3 premières recommandations

# Définition d'une clé pour le bouton de la page d'accueil pour forcer la re-renderisation
login_button_key = 'login_button'
home_button_key = 'home_button'

# Page d'accueil avec connexion
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

if st.session_state['page'] == 'home':
    st.title('Welcome to the Music Recommendation Engine')
    user_id = st.text_input('Enter your ID:', key="user_id")
    if st.button('Login', key=login_button_key):
        if user_id:
            st.session_state['page'] = 'recommendation'
        else:
            st.error('Please enter a valid ID.')

# Page de recommandation
elif st.session_state['page'] == 'recommendation':
    st.title('Music Recommendation Engine')

    # Bouton pour retourner à la page d'accueil
    if st.button('Back to Home', key=home_button_key):
        st.session_state['page'] = 'home'

    # Menu déroulant pour sélectionner plusieurs chansons
    selected_songs = st.multiselect('Select songs you like:', songs_list, key="selected_songs")
    
    # Bouton pour obtenir des recommandations
    if st.button('Recommend Songs'):
        if selected_songs:
            recommendations = generate_recommendations(selected_songs)
            st.subheader('Recommended Songs for you:')
            for song in recommendations:
                st.write(song)
        else:
            st.warning('Please select at least one song.')
