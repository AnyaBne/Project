import streamlit as st

st.title('Hello Everybodyy')
st.write('Hellooooooooo.')

import streamlit as st

# Exemple de liste de chansons (vous pouvez remplacer cela par votre propre liste ou base de données)
songs_list = ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5']

# Fonction pour générer des recommandations (à implémenter selon votre logique)
def generate_recommendations(selected_song):
    # Ici, implémentez votre logique pour générer des recommandations
    # Actuellement, cela renvoie simplement une liste de chansons
    return ['Recommended Song 1', 'Recommended Song 2', 'Recommended Song 3']

# Interface utilisateur
st.title('Music Recommendation Engine')

# Menu déroulant pour sélectionner une chanson
selected_song = st.selectbox('Select a song you like:', songs_list)

# Bouton pour obtenir des recommandations
if st.button('Recommend Songs'):
    recommendations = generate_recommendations(selected_song)
    st.write('Recommended Songs for you:')
    for song in recommendations:
        st.write(song)

