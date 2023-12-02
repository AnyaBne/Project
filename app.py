import streamlit as st

# Exemple de liste de chansons
songs_list = ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5']

# Fonction pour générer des recommandations
def generate_recommendations(selected_songs):
    return [song for song in songs_list if song not in selected_songs][:3]

# Fonctions pour contrôler l'affichage des pages
def show_home_page():
    st.title('Welcome to the Music Recommendation Engine')
    user_id = st.text_input('Enter your ID:', key="user_id")
    if st.button('Login'):
        if user_id:
            st.session_state['page'] = 'recommendation'
            st.session_state['user_id'] = user_id
        else:
            st.error('Please enter a valid ID.')

def show_recommendation_page():
    st.title('Music Recommendation Engine')
    
    # Vérifier si l'utilisateur est défini, sinon retourner à la page d'accueil
    if 'user_id' not in st.session_state or not st.session_state['user_id']:
        st.session_state['page'] = 'home'
        return

    st.write(f"Welcome user {st.session_state['user_id']}.")

    if st.button('Back to Home'):
        st.session_state['page'] = 'home'
    selected_songs = st.multiselect('Select songs you like:', songs_list, key="selected_songs")
    if st.button('Recommend Songs'):
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

# Affichage des pages en fonction de l'état
if st.session_state['page'] == 'home':
    show_home_page()
elif st.session_state['page'] == 'recommendation':
    show_recommendation_page()
