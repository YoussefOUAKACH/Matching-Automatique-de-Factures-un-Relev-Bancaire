from fpdf import FPDF
import streamlit as st  

def generate_pdf_report(bank_data, matches, file_name="rapport.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Titre du rapport
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Rapport de Matching : Relevé Bancaire et Factures", ln=True, align="C")
    pdf.ln(10)

    # Résumé des données
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Nombre de transactions bancaires : {len(bank_data)}", ln=True)
    pdf.cell(200, 10, txt=f"Nombre de factures traitées : {len(matches)}", ln=True)
    pdf.ln(10)

    # Détails du matching
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Détails du Matching :", ln=True)
    pdf.set_font("Arial", size=10)

    if matches:
        for match in matches:
            pdf.cell(200, 10, txt=f"Date: {match[0]} | Montant: {match[1]} {match[2]} | Vendeur: {match[3]}", ln=True)
            pdf.cell(200, 10, txt=f"Facture correspondante : {match[4]} (Score: {match[5]})", ln=True)
            pdf.ln(5)
    else:
        pdf.cell(200, 10, txt="Aucun matching trouvé.", ln=True)

    # Statistiques
    pdf.ln(10)
    unmatched_transactions = [m for m in matches if m[5] < 60]
    pdf.cell(200, 10, txt=f"Nombre de transactions sans correspondance forte : {len(unmatched_transactions)}", ln=True)
    
    
    pdf.output(file_name)
    print(f"Rapport PDF généré : {file_name}")


if __name__ == "__main__":
    
    bank_data = pd.DataFrame(...)  
    matches = [...]  
    generate_pdf_report(bank_data, matches)
def download_report(file_name):
    with open(file_name, "r") as f:
        content = f.read()
    
    st.download_button(
        label="Télécharger le rapport",
        data=content,
        file_name=file_name,
        mime="text/plain"
    )
if __name__ == "__main__":
    generate_pdf_report(bank_data, matches)
    download_report("rapport.txt") 