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
Vous trouverez ci-dessous une template LaTeX d'un CV ainsi que les données JSON d'un CV. Votre tâche consiste à structurer correctement chaque section du CV selon la template LaTeX fournie et à insérer toutes les informations présentes dans les données JSON. Assurez-vous que chaque section du JSON soit correctement représentée dans le document LaTeX final. Ajoutez des sections supplémentaires si nécessaire pour couvrir toutes les informations du JSON. Supprimez les sections dans la template qui ne correspondent pas aux données du JSON.

Template LaTeX:
{latex_template}

Données JSON:
{json.dumps(cv_data, indent=4)}

Veuillez fournir le contenu LaTeX complet avec toutes les données du CV insérées aux endroits appropriés et correctement structurées, en respectant la structure et le style de la template LaTeX. Supprimez les sections de la template qui ne correspondent pas aux données JSON.
"""

# Initialiser le modèle Gemini
model = GoogleGenerativeModelInit("gemini-1.5-flash")

# Générer le contenu LaTeX complet
response_latex = model.generate_content([prompt])

# Sauvegarder le LaTeX final dans un fichier
with open('cv_final.tex', 'w') as output_file:
    output_file.write(response_latex)

print("Le CV a été généré avec succès et sauvegardé dans 'cv_final.tex'.")
