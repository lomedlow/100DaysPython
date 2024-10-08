import streamlit as st

def app():
    st.title("Tip Calculator")

    # Entrée pour la facture totale
    bill = st.number_input("What was the total bill? $", min_value=0.0, step=0.01)

    # Sélection du pourcentage du pourboire
    tip = st.slider("What percentage tip would you like to give?", 0, 100, 15)

    # Nombre de personnes pour partager la facture
    people = st.number_input("How many people to split the bill?", min_value=1, step=1)

    # Calculer le montant par personne lorsque l'utilisateur appuie sur le bouton
    if st.button("Calculate"):
        if people > 0:
            tip_total = tip / 100 * bill
            total_to_pay = bill + tip_total
            bill_per_person = total_to_pay / people
            final_amount = round(bill_per_person, 2)
            # Afficher le montant final que chaque personne doit payer
            st.success(f"Each person should pay: ${final_amount}")
        else:
            st.error("The number of people must be greater than 0.")
