import streamlit as st

# Exemple de liste de chansons
songs_list = ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5']

# Fonction pour générer des recommandations
def generate_recommendations(selected_songs):
    # Implémentez votre logique ici
    recommended_songs = [song for song in songs_list if song not in selected_songs]
    return recommended_songs[:3]  # Retourne les 3 premières recommandations

# Gestion de l'état de la page
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Fonction pour changer de page
def go_to_recommendation():
    st.session_state.page = 'recommendation'

def go_to_home():
    st.session_state.page = 'home'

# Page d'accueil avec connexion
if st.session_state.page == 'home':
    st.title('Welcome to the Music Recommendation Engine')
    
    # Champ de saisie pour l'ID de l'utilisateur
    user_id = st.text_input('Enter your ID:', '')

    # Bouton de connexion
    if st.button('Login'):
        if user_id:
            go_to_recommendation()
        else:
            st.warning('Please enter a valid ID.')

# Page de recommandation
elif st.session_state.page == 'recommendation':
    st.title('Music Recommendation Engine')

    # Bouton pour retourner à la page d'accueil
    if st.button('Back to Home'):
        go_to_home()

    # Menu déroulant pour sélectionner plusieurs chansons
    selected_songs = st.multiselect('Select songs you like:', songs_list)

    # Bouton pour obtenir des recommandations
    if st.button('Recommend Songs'):
        if selected_songs:
            recommendations = generate_recommendations(selected_songs)
            st.write('Recommended Songs for you:')
            for song in recommendations:
                st.write(song)
        else:
            st.write('Please select at least one song.')
