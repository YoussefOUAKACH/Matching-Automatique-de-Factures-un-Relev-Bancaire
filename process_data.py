import pandas as pd
import pytesseract
from PIL import Image
import os
from fuzzywuzzy import process
import streamlit as st


#  Chemin absolu de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HP\Desktop\dataset\tesseract\tesseract.exe'

# Lecture et parsing des relevés bancaires
def load_bank_statements(df):
    # Supprimer les espaces autour des noms de colonnes
    df.columns = df.columns.str.strip()

    # Vérifier les colonnes lues dans le fichier CSV pour le débogage
    st.write("Colonnes lues du fichier CSV :", df.columns)

    # Renommer les colonnes si nécessaire
    df = df.rename(columns={"date": "Date", "amount": "Montant", "currency": "Devise", "vendor": "Vendeur"})
    
    # Vérification des colonnes attendues
    expected_columns = {"Date", "Montant", "Devise", "Vendeur"}
    missing_columns = expected_columns - set(df.columns)
    
    if missing_columns:
        raise ValueError(f"Colonnes manquantes dans les relevés bancaires: {missing_columns}")

    return df


# Extraction de texte des factures
def extract_text_from_image(image_path):
    try:
        print(f"📄 Traitement de l'image : {image_path}")  
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"❌ Fichier introuvable : {image_path}")

        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        print(f"✅ Extraction terminée pour : {image_path}")  
        return text
    except Exception as e:
        print(f"⚠️ Erreur lors du traitement de l'image {image_path}: {e}")
        return ""

#Traitement des factures
def process_invoices(folder_path):
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"❌ Le dossier {folder_path} n'existe pas.")
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"❌ {folder_path} est un fichier, pas un dossier !")

    invoices = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".png")):
            filepath = os.path.join(folder_path, filename)
            text = extract_text_from_image(filepath)
            invoices[filename] = text

    if not invoices:
        print("⚠️ Aucune facture trouvée dans le dossier.")
    return invoices

#  Matching entre transactions et factures
def match_transactions_to_invoices(bank_data, invoices):
    if not invoices:
        print("⚠️ Aucune facture disponible pour le matching.")
        return []

    matches = []
    for index, row in bank_data.iterrows():
        try:
            transaction_info = f"{row['date']} {row['amount']} {row['currency']} {row['vendor']}"
            best_match_result = process.extractOne(transaction_info, list(invoices.values()))
            if best_match_result:
                best_match, score = best_match_result
                matches.append((row['date'], row['amount'], row['currency'], row['vendor'], best_match, score))
                print(f"🔄 Transaction {index+1}/{len(bank_data)} traitée.")
            else:
                print(f"⚠️ Aucun match trouvé pour la transaction : {transaction_info}")
        except Exception as e:
            print(f"⚠️ Erreur lors du matching de la ligne {index+1}: {e}")
            continue

    return matches
