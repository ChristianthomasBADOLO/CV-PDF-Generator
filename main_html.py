# import json
# import pdfkit
# from services.google.generative_ai import GoogleGenerativeModelInit

# # Charger le fichier JSON
# with open('cv_badolo.json', 'r', encoding='utf-8') as json_file:
#     cv_data = json.load(json_file)

# prompt = f"""
# Utilise les informations suivantes du CV en format JSON pour créer un CV en HTML qui tient sur une seule page. Organise les informations de manière compacte en utilisant une mise en page efficace. Voici les données JSON :

# {json.dumps(cv_data, indent=2)}

# Le CV doit être structuré de manière compacte en utilisant les sections suivantes :

# 1. En-tête
# 2. PROFIL
# 3. EXPERIENCES
# 4. EDUCATION
# 5. COMPÉTENCES (LANGUES, HUMAN SKILLS, HARD SKILLS)
# 6. PORTFOLIO
# 7. CONTACTS
# 8. CENTRES D'INTÉRÊTS

# Si tu trouves d'autres sections dans le JSON, ajoute-les également.

# Voici un exemple de mise en page en HTML :

# <!DOCTYPE html>
# <html lang="en">
# <head>
# <meta charset="UTF-8">
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
# <title>CV</title>
# <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
# <style>
#   body {{
#     font-family: Arial, sans-serif;
#     font-size: 16px;
#   }}
#   .container {{
#     padding: 5px;
#   }}
#   .header {{
#     margin-bottom: 5px;
#   }}
#   .profile {{
#     margin-bottom: 5px;
#     width: 100%;
#   }}
#   h2 {{
#     font-size: 18px;
#     margin-top: 5px;
#   }}
#   ul {{
#     padding-left: 5px;
#     list-style-type: disc;
#   }}
#   .profile-item {{
#     margin-bottom: 10px;
#   }}
# </style>
# </head>
# <body>

# <div class="container">
#   <!-- En-tête -->
#   <div class="header">
#     <h1>Jean Badolo</h1>
#     <hr>
#   </div>

#   <!-- Profil -->
#   <div class="profile">
#     <h2>PROFIL</h2>
#     <div class="row">
#       <div class="col-md-6 profile-item">
#         <p>Développeur Full Stack avec 5 ans d'expérience dans le développement web, spécialisé en Python et JavaScript.</p>
#       </div>
#       <div class="col-md-6 profile-item">
#         <!-- Ajoutez des informations supplémentaires ici si nécessaire -->
#       </div>
#     </div>
#     <hr>
#   </div>

#   <!-- Sections en colonnes -->
#   <div class="row">
#     <div class="col-md-6">
#       <!-- Expériences -->
#       <h2>EXPERIENCES</h2>
#       <ul>
#         <li>Développeur Web chez XYZ - Jan 2018 à Présent</li>
#         <li>Stagiaire Développeur chez ABC - Juin 2016 à Déc 2017</li>
#       </ul>

#       <!-- Section Supplémentaire -->
#       <h2>SECTION SUPPLÉMENTAIRE</h2>
#       <ul>
#         <li>Certificat en Gestion de Projet - Coursera</li>
#         <li>Bénévole pour l'association Code pour Tous</li>
#       </ul>
#     </div>

#     <div class="col-md-6">
#       <!-- Éducation -->
#       <h2>EDUCATION</h2>
#       <ul>
#         <li>Master en Informatique - Université de Technologie - 2015</li>
#         <li>Licence en Informatique - Université de Sciences - 2013</li>
#       </ul>

#       <!-- Compétences -->
#       <h2>COMPÉTENCES</h2>
#       <p><strong>Langues</strong> : Français, Anglais</p>
#       <p><strong>Human Skills</strong> : Communication, Travail en équipe</p>
#       <p><strong>Hard Skills</strong> : Python, JavaScript, HTML, CSS, React, Node.js</p>

#       <!-- Portfolio -->
#       <h2>PORTFOLIO</h2>
#       <p>Projets disponibles sur mon site web : www.jeanbadolo.com</p>

#       <!-- Contacts -->
#       <h2>CONTACTS</h2>
#       <p>Email : jean.badolo@example.com, Téléphone : 0123456789</p>

#       <!-- Centres d'intérêts -->
#       <h2>CENTRES D'INTÉRÊTS</h2>
#       <p>Voyages, Photographie, Lecture</p>
#     </div>
#   </div>
# </div>

# <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
# <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
# <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
# </body>
# </html>

# Retourne-moi le contenu HTML. La section PROFIL doit occuper toute la largeur. Ajoute une section tirée d'une des sections contenues dans le JSON en dessous de la section EXPÉRIENCES pour occuper toute la largeur de la page. Réduis aussi les espaces si nécessaire pour que tout tienne sur une seule page A4. En faite apres la section profil creer deux colonne et remplie la premiere d'abord avec les infos puis passe à la seconde avec les autres infos.
# """

# # Initialiser le modèle Google Generative AI
# model = GoogleGenerativeModelInit("gemini-1.5-pro")

# # Générer le contenu HTML
# response_html = model.generate_content([prompt])

# # Contenu HTML généré
# html_content = response_html

# # Chemin du fichier où vous voulez sauvegarder le contenu
# file_path = 'cv.html'

# # Écrire le contenu dans le fichier
# with open(file_path, 'w', encoding='utf-8') as file:
#     file.write(html_content)

# print(f"Le fichier HTML a été sauvegardé sous {file_path}.")

from selenium import webdriver
import os

# Chemin vers le fichier HTML
file_path = 'cv.html'

# Convertir le chemin en URL
file_url = 'file://' + os.path.abspath(file_path)

# Configuration du chemin vers chromedriver
chrome_driver_path = 'chemin/vers/chromedriver'

# Créer une instance du navigateur Chrome
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Ouvrir le fichier HTML dans Chrome
driver.get(file_url)

# Optionnel : Garder le navigateur ouvert pendant un certain temps
import time
time.sleep(10)  # Ajustez la durée en secondes selon vos besoins

# Fermer le navigateur
driver.quit()
