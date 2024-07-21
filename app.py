import os
import time
import base64
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# Initialiser le modèle Google Generative AI (remplacez cette partie avec l'initialisation réelle)
from services.google.generative_ai import GoogleGenerativeModelInit
from prompt import prompt

model = GoogleGenerativeModelInit("gemini-1.5-pro")
response_html = model.generate_content([prompt])
html_content = response_html

# Chemin du fichier où vous voulez sauvegarder le contenu HTML
file_path = 'cv.html'

# Écrire le contenu dans le fichier HTML
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(html_content)

# Fonction pour convertir HTML en PDF
def convert_html_to_pdf(html_file_path, pdf_file_path):
    # Convertir le chemin en URL
    file_url = 'file://' + os.path.abspath(html_file_path)
    
    # Chemin vers chromedriver
    chrome_driver_path = '/usr/local/bin/chromedriver'
    
    # Créer une instance du navigateur Chrome avec les options nécessaires
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Mode headless
    options.add_argument('--disable-gpu')  # Nécessaire pour le mode headless sur certaines versions de Windows
    options.add_argument('--kiosk-printing')  # Pour imprimer sans affichage de boîte de dialogue
    
    # Initialiser le service ChromeDriver
    service = Service(executable_path=chrome_driver_path)
    
    # Créer l'instance du navigateur
    driver = webdriver.Chrome(service=service, options=options)
    
    # Ouvrir le fichier HTML dans Chrome
    driver.get(file_url)
    
    # Attendre que la page se charge
    time.sleep(3)
    
    # Utiliser l'API DevTools pour configurer les options d'impression et enregistrer en PDF
    params = {
        "landscape": False,
        "displayHeaderFooter": False,
        "printBackground": True,
        "preferCSSPageSize": True,
        "paperWidth": 8.27,
        "paperHeight": 11.69,
        "marginTop": 0,
        "marginBottom": 0,
        "marginLeft": 0,
        "marginRight": 0
    }
    
    # Activer DevTools et envoyer les commandes d'impression
    result = driver.execute_cdp_cmd("Page.printToPDF", params)
    
    # Sauvegarder le fichier PDF généré
    with open(pdf_file_path, "wb") as file:
        file.write(base64.b64decode(result['data']))
    
    # Fermer le navigateur
    driver.quit()

# Titre de l'application
st.title("Générateur de CV PDF")

# Afficher le contenu HTML
st.subheader("Aperçu du CV HTML")
st.markdown(html_content, unsafe_allow_html=True)

# Bouton pour convertir en PDF et télécharger
if st.button("Télécharger en PDF"):
    with st.spinner('Conversion en cours...'):
        pdf_path = "cv.pdf"
        convert_html_to_pdf(file_path, pdf_path)
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
            b64 = base64.b64encode(pdf_bytes).decode()
            href = f'<a href="data:application/octet-stream;base64,{b64}" download="cv.pdf">Cliquez ici pour télécharger votre CV PDF</a>'
            st.markdown(href, unsafe_allow_html=True)
        st.success('Conversion terminée!')

# Ajouter une barre de progression
with st.spinner('Génération du contenu HTML...'):
    time.sleep(2)
st.progress(100)
