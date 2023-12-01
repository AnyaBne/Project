import streamlit as st

st.title('Hello Everybodyy')
st.write('Hellooooooooo.')

# Exemple de liste de chansons (remplacez ceci par votre propre liste ou base de données)
songs_list = ['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5']

# Fonction pour générer des recommandations (à implémenter selon votre logique)
def generate_recommendations(selected_songs):
    # Ici, implémentez votre logique pour générer des recommandations
    # Pour l'instant, cela renvoie simplement une liste de chansons non sélectionnées
    recommended_songs = [song for song in songs_list if song not in selected_songs]
    return recommended_songs[:3]  # Retourne les 3 premières recommandations

# Interface utilisateur
st.title('Music Recommendation Engine')

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
