import streamlit as st

# Exemple de liste de chansons
songs_list = ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5']

# Fonction pour générer des recommandations
def generate_recommendations(selected_songs):
    # Implémentez votre logique ici
    # Cette fonction est simplifiée pour l'exemple
    return [song for song in songs_list if song not in selected_songs][:3]

# Fonction pour afficher la page d'accueil
def show_home_page():
    st.title('Welcome to the Music Recommendation Engine')
    user_id = st.text_input('Enter your ID:', key="user_id_input")
    if st.button('Login', key='login_button'):
        if user_id:
            st.session_state['page'] = 'recommendation'
            st.experimental_rerun()
        else:
            st.error('Please enter a valid ID.')

# Fonction pour afficher la page de recommandation
def show_recommendation_page():
    st.title('Music Recommendation Engine')
    if st.button('Back to Home', key='back_home_button'):
        st.session_state['page'] = 'home'
        st.experimental_rerun()
    selected_songs = st.multiselect('Select songs you like:', songs_list, key="selected_songs_multiselect")
    if st.button('Recommend Songs', key='recommend_button'):
        if selected_songs:
            recommendations = generate_recommendations(selected_songs)
            st.subheader('Recommended Songs for you:')
            for song in recommendations:
                st.write(song)
        else:
            st.warning('Please select at least one song.')

# Affichage des pages en fonction de l'état
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

if st.session_state['page'] == 'home':
    show_home_page()
elif st.session_state['page'] == 'recommendation':
    show_recommendation_page()
