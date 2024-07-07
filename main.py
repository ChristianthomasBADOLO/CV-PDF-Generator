import json
from services.google.generative_ai import GoogleGenerativeModelInit

# Lire le fichier LaTeX
with open('templates/cv1.tex', 'r') as latex_file:
    latex_template = latex_file.read()

# Charger le fichier JSON
with open('cv.json', 'r') as json_file:
    cv_data = json.load(json_file)

# Construire le prompt pour Gemini
prompt = f"""
Le contenu ci-dessous est une template LaTeX d'un CV, suivie des données JSON d'un CV. Veuillez structurer correctement les sections du CV selon la template LaTeX et ajouter toutes les informations existantes dans le CV JSON.

Template LaTeX:
{latex_template}

Données JSON:
{json.dumps(cv_data, indent=4)}

Veuillez renvoyer le contenu LaTeX complet avec les données du CV insérées aux endroits appropriés.
"""

# Initialiser le modèle Gemini
model = GoogleGenerativeModelInit("gemini-1.5-flash")

# Générer le contenu LaTeX complet
response_latex = model.generate_content([prompt])

# Sauvegarder le LaTeX final dans un fichier
with open('cv_final.tex', 'w') as output_file:
    output_file.write(response_latex)

print("Le CV a été généré avec succès et sauvegardé dans 'cv_final.tex'.")
