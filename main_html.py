import os
import time
import base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from services.google.generative_ai import GoogleGenerativeModelInit
from prompt import prompt

# Initialiser le modèle Google Generative AI
model = GoogleGenerativeModelInit("gemini-1.5-pro")

# Générer le contenu HTML
response_html = model.generate_content([prompt])

# Contenu HTML généré
html_content = response_html

# Chemin du fichier où vous voulez sauvegarder le contenu
file_path = 'cv.html'

# Écrire le contenu dans le fichier
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(html_content)



#Chemin vers le fichier HTML
file_path = 'cv.html'

#Convertir le chemin en URL
file_url = 'file://' + os.path.abspath(file_path)

#Chemin vers chromedriver
chrome_driver_path = '/usr/local/bin/chromedriver'

#Créer une instance du navigateur Chrome avec les options nécessaires
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Mode headless
options.add_argument('--disable-gpu')  # Nécessaire pour le mode headless sur certaines versions de Windows
options.add_argument('--kiosk-printing')  # Pour imprimer sans affichage de boîte de dialogue

#Initialiser le service ChromeDriver
service = Service(executable_path=chrome_driver_path)

#Créer l'instance du navigateur
driver = webdriver.Chrome(service=service, options=options)

#Ouvrir le fichier HTML dans Chrome
driver.get(file_url)

#Attendre que la page se charge
time.sleep(3)

#Utiliser l'API DevTools pour configurer les options d'impression et enregistrer en PDF
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

#Activer DevTools et envoyer les commandes d'impression
result = driver.execute_cdp_cmd("Page.printToPDF", params)

#Sauvegarder le fichier PDF généré
with open("cv.pdf", "wb") as file:
    file.write(base64.b64decode(result['data']))

#Fermer le navigateur
driver.quit()

