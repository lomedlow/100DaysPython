import streamlit as st

def app():
    st.title("Brand Name Generator")

    # Entrées utilisateur
    city = st.text_input("City you grew up in:")
    petname = st.text_input("Your pet's name:")

    # Générer le nom de la marque
    if st.button("Generate Brand Name"):
        if city and petname:
            brand_name = f"{city} {petname}"
            st.success(f"Your brand name could be: {brand_name}")
        else:
            st.error("Please enter both the city and your pet's name.")
