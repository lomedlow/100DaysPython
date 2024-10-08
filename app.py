import streamlit as st
import pages.day1.app as Day1App  # Import du projet Day 1
import pages.day2.app as Day2App  # Import du projet Day 2

# Appliquer des styles pour le titre sans animation et avec une couleur rouge orangé
st.markdown(
    """
    <style>
    .title {
        color: #FF4500;  
        font-size: 3em;
    
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Afficher le titre sans animation, avec la couleur rouge orangé
st.markdown('<h1 class="title">100 Days of Python Projects</h1>', unsafe_allow_html=True)

# Lire les paramètres d'URL (query parameters)
query_params = st.experimental_get_query_params()
selected_project = query_params.get("project", ["Home"])[0]

# Barre latérale pour navigation
st.sidebar.title("Choose a project")

# Utiliser le selectbox pour naviguer
page = st.sidebar.selectbox(
    "Choose a project",
    ["Home", "Day 1: Brand Name Generator", "Day 2: Tip Calculator"],
    index=["Home", "Day 1: Brand Name Generator", "Day 2: Tip Calculator"].index(
        "Day 1: Brand Name Generator" if selected_project == "Day1" else
        "Day 2: Tip Calculator" if selected_project == "Day2" else "Home"
    )
)

# Mettre à jour l'URL en fonction de la sélection du menu
def update_url(project_name):
    st.experimental_set_query_params(project=project_name)

# Synchroniser l'URL et le projet sélectionné
if page == "Home":
    update_url("Home")
    st.write("Welcome to the 100 Days of Python Projects! Choose a project from the sidebar.")
elif page == "Day 1: Brand Name Generator":
    update_url("Day1")
    Day1App.app()  # Exécute le projet Day 1
elif page == "Day 2: Tip Calculator":
    update_url("Day2")
    Day2App.app()  # Exécute le projet Day 2
