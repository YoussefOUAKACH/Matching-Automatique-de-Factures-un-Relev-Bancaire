import streamlit as st
import pandas as pd
import os
from process_data import load_bank_statements, process_invoices, match_transactions_to_invoices
from report import generate_pdf_report

st.set_page_config(page_title="🔍 Matching Relevés / Factures", layout="wide")

st.title("📊 Application de Matching : Relevés Bancaires & Factures")
st.markdown("Cette application permet d'extraire les textes des factures et de faire le matching avec les transactions bancaires.")

# Upload du relevé bancaire
uploaded_file = st.file_uploader("📁 Dépose ton relevé bancaire (.csv)", type=["csv"], accept_multiple_files=True)

# Dossier des factures
folder_path = st.text_input("📂 Dossier contenant les factures (images JPG/PNG)", "C:\\Users\\HP\\Desktop\\dataset\\receipts")

if st.button("🚀 Lancer l'analyse"):
    if uploaded_file and folder_path:
        try:
            all_dataframes = []
            # Traiter chaque fichier CSV uploadé
            for file in uploaded_file:
                # Lire chaque fichier CSV avec pandas
                df = pd.read_csv(file)
                # Nettoyer et vérifier les colonnes
                cleaned_df = load_bank_statements(df)
                all_dataframes.append(cleaned_df)

            # Fusionner tous les relevés ensemble
            bank_data = pd.concat(all_dataframes, ignore_index=True)
            st.success(f"✅ {len(bank_data)} transactions chargées depuis {len(uploaded_file)} fichier(s).")

            # Traitement des factures
            invoices = process_invoices(folder_path)
            st.success(f"✅ {len(invoices)} factures traitées par OCR.")

            # Matching
            matches = match_transactions_to_invoices(bank_data, invoices)
            if matches:
                match_df = pd.DataFrame(matches, columns=["Date", "Montant", "Devise", "Vendeur", "Texte Facture", "Score de Similarité"])
                st.subheader("🔎 Résultat du Matching")
                st.dataframe(match_df)
            else:
                st.warning("⚠️ Aucun matching n'a pu être réalisé.")
        except Exception as e:
            st.error(f"❌ Une erreur est survenue : {e}")
    else:
        st.warning("⚠️ Merci de fournir au moins un fichier CSV et un dossier valide.")

