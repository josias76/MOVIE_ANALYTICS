import streamlit as st

# Interface utilisateur avec Streamlit
st.set_page_config(
    layout="wide",
    page_title=" Data Analysis MovieLens",
    page_icon="🎬"  # Emoji Unicode directement
)

# Conteneur pour aligner les éléments horizontalement
col1, col2, col3 = st.columns([1, 4, 1])

# Colonne gauche : Image
with col1:
    st.image(
    "https://raw.githubusercontent.com/josias76/MOVIE_ANALYTICS/main/streamlit_app/images/data.jpeg",
    width=80,
    use_container_width=False,
)

# Colonne centrale : Titre
with col2:
    st.markdown(
        """
        <h1 style='text-align: center; margin-bottom: 0;'>Exploration des Données MovieLens</h1>
        """,
        unsafe_allow_html=True,
    )

# Colonne droite : Nom et lien LinkedIn
with col3:
    st.markdown(
        """
        <div style='text-align: right;'>
            <a href="https://www.linkedin.com/in/josias-nteme-95757721a/" target="_blank" style='text-decoration: none; color: #0077b5;'>
                <strong>Josias Nteme</strong>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write(" ")
st.write(" ")

# Titre
st.markdown("# **Phase 1 : Développeur Python & Architecte API**")
# Afficher l'image séparément
st.image("https://raw.githubusercontent.com/josias76/MOVIE_ANALYTICS/main/streamlit_app/images/architecture2.png", use_container_width=True)

st.markdown(
        """
        <a href="https://github.com/josias76/PROJET_MOVIES" target="_blank">
            <button style="background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                📦 Cliquer pour voir le Code de la Phase 1
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

st.write(" ")
st.write(" ")
st.write(" ")


# Titre
st.markdown("# **Phase 2 : Data Analyst - Exploration et Visualisation**")
# Afficher l'image séparément
st.image("https://raw.githubusercontent.com/josias76/MOVIE_ANALYTICS/main/streamlit_app/images/architecturephase.png", use_container_width=True)

st.markdown(
        """
        <a href="https://github.com/josias76/MOVIE_ANALYTICS" target="_blank">
            <button style="background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 16px;">
                📊 Cliquer pour voir le Code de la Phase 2
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )





