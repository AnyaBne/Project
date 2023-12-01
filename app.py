import streamlit as st

# Exemple de liste de chansons
songs_list = ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5']

# Fonction pour générer des recommandations
def generate_recommendations(selected_songs):
    # Implémentez votre logique ici
    recommended_songs = [song for song in songs_list if song not in selected_songs]
    return recommended_songs[:3]  # Retourne les 3 premières recommandations

# Initialisation de l'état de la page
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Fonction pour changer l'état de la page
def set_page_state(page):
    st.session_state.page = page

# Page d'accueil avec connexion
if st.session_state.page == 'home':
    st.title('Welcome to the Music Recommendation Engine')
    
    # Champ de saisie pour l'ID de l'utilisateur
    user_id = st.text_input('Enter your ID:', '')

    # Bouton de connexion
    login_button = st.button('Login')

    # Vérification de l'ID et mise à jour de l'état de la page
    if login_button:
        if user_id:
            set_page_state('recommendation')
        else:
            st.warning('Please enter a valid ID.')

# Page de recommandation
elif st.session_state.page == 'recommendation':
    st.title('Music Recommendation Engine')

    # Menu déroulant pour sélectionner plusieurs chansons
    selected_songs = st.multiselect('Select songs you like:', songs_list)

    # Bouton pour obtenir des recommandations
    recommend_button = st.button('Recommend Songs')
    
    # Bouton pour retourner à la page d'accueil
    back_button = st.button('Back to Home')

    # Affichage des recommandations si demandé
    if recommend_button:
        if selected_songs:
            recommendations = generate_recommendations(selected_songs)
            st.subheader('Recommended Songs for you:')
            for song in recommendations:
                st.write(song)
        else:
            st.warning('Please select at least one song.')

    # Changement de page si le bouton "Back to Home" est pressé
    if back_button:
        set_page_state('home')
