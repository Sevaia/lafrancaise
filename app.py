import streamlit as st
import streamlit.components.v1 as components

# Page title
st.set_page_config(
    page_title="Accès PBI",  # Titre de la page
    page_icon="📊",  # Icône affichée dans l'onglet du navigateur
    layout="wide"  # Mise en page étendue
)

# Load your HTML file
with open("popup.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Display HTML
components.html(html_content, height=800, scrolling=True)

