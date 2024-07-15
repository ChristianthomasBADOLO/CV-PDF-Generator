# import json
# from services.google.generative_ai import GoogleGenerativeModelInit

# # Read the LaTeX file
# with open('templates/cv3.tex', 'r') as latex_file:
#     latex_template = latex_file.read()

# # Load the JSON file
# with open('cv_badolo.json', 'r') as json_file:
#     cv_data = json.load(json_file)

# prompt = f"""
# Below you will find a LaTeX template of a CV and the JSON data of a CV. Your task is to properly structure each section of the CV according to the LaTeX template and insert all the information from the JSON data. 

# Mandatory instructions:
# 1. Ensure that each section of the JSON is represented in the final LaTeX document.
# 2. Add additional sections if necessary to include all the information from the JSON.
# 3. Remove sections from the template that do not correspond to the JSON data.
# 4. Format the content so that everything fits on a single A4 page. This is essential and crucial.
# 5. Split the page into two columns after the "profile" section to use space optimally.
# 6. Use a smaller font size (e.g., \\small or \\footnotesize) if necessary to make the content fit on a single page.
# 7. Reduce vertical spacing (\\vspace) between sections to save space.
# 8. Use appropriate LaTeX commands to manage columns (e.g., the multicols package).

# Here is the LaTeX template:
# {latex_template}

# Here is the JSON data:
# {json.dumps(cv_data, indent=4)}

# Please provide the complete LaTeX document with all CV data correctly inserted and structured. Ensure that the final document is optimized to fit on a single A4 page.

# Note: You are an expert in design and highly proficient in LaTeX. Apply your expertise to ensure the final output is professional, visually appealing, and perfectly formatted.
# """

# # Initialize the Gemini model
# model = GoogleGenerativeModelInit("gemini-pro")

# # Generate the complete LaTeX content
# response_latex = model.generate_content([prompt])

# # Save the final LaTeX to a file
# with open('cv3_final.tex', 'w') as output_file:
#     output_file.write(response_latex)

# print("The CV has been successfully generated and saved in 'cv_final.tex'.")





# import json
# from services.google.generative_ai import GoogleGenerativeModelInit

# # Read the LaTeX file
# with open('templates/cv6.tex', 'r') as latex_file:
#     latex_template = latex_file.read()

# # Load the JSON file
# with open('cv_nabi.json', 'r', encoding='utf-8') as json_file:
#     cv_data = json.load(json_file)

# prompt = f"""
# Vous trouverez ci-dessous un template LaTeX de CV et du contenu de CV au format JSON. Votre tâche consiste à structurer chaque section du CV en fonction du template LaTeX et à insérer toutes les informations provenant des données JSON.

# Instructions obligatoires :

# 1. Représentation complète : Assurez-vous que chaque section des données JSON est représentée dans le document LaTeX final.
# 2. Ajout de sections supplémentaires : Ajoutez des sections supplémentaires si nécessaire pour inclure toutes les informations des données JSON.
# 3. Suppression des sections inutiles : Supprimez les sections du modèle qui ne correspondent pas aux données JSON.
# 4. Mise en page sur une seule page A4 : Formatez le contenu du CV pour qu'il tienne sur une seule page A4. Ceci est essentiel et crucial.
# 5. Utilisation de colonnes : Après la section "profil", sectionnner la feuille A4 en deux colonnes pour optimiser l'utilisation de l'espace.
# 6. Taille de police réduite : Utilisez une taille de police appropriée pour que le contenu tienne sur une seule page avec un bon formatage et une bonne lisibilté.
# 7. Réduction de l'espacement vertical : Réduisez l'espacement vertical (\\vspace) entre les sections pour économiser de l'espace.
# 8. Utilisation appropriée des commandes LaTeX pour les colonnes : Utilisez les commandes appropriées pour gérer les colonnes, telles que celles du package `multicols`.

# Objectif final :
# Fournissez un code latex complet du contenu où toutes les données sont correctement insérées et structurées, avec une mise en page optimisée pour tenir sur une seule page A4. Assurez-vous que le document final est professionnel, visuellement attrayant et parfaitement formaté.

# Voici le modèle LaTeX :
# {latex_template}

# Voici les données JSON :
# {json.dumps(cv_data, indent=4)} """

# # Initialize the Gemini model
# model = GoogleGenerativeModelInit("gemini-pro")

# # Generate the complete LaTeX content
# response_latex = model.generate_content([prompt])

# # Save the final LaTeX to a file
# with open('cv3_final.tex', 'w') as output_file:
#     output_file.write(response_latex)

# print("Le CV a été généré avec succès et enregistré dans 'cv3_final.tex'.")


import json
from langchain_huggingface import HuggingFaceEndpoint  # Import depuis le nouveau package

# Lire le fichier LaTeX
with open('templates/cv6.tex', 'r') as latex_file:
    latex_template = latex_file.read()
    

# Charger le fichier JSON
with open('cv_nabi.json', 'r', encoding='utf-8') as json_file:
    cv_data = json.load(json_file)


prompt = f"""
Vous trouverez ci-dessous un template LaTeX de CV et du contenu de CV au format JSON. Votre tâche consiste à structurer chaque section du CV en fonction du template LaTeX et à insérer toutes les informations provenant des données JSON.

Instructions obligatoires :

1. Représentation complète : Assurez-vous que chaque section des données JSON est représentée dans le document LaTeX final.
2. Ajout de sections supplémentaires : Ajoutez des sections supplémentaires si nécessaire pour inclure toutes les informations des données JSON.
3. Suppression des sections inutiles : Supprimez les sections du modèle qui ne correspondent pas aux données JSON.
4. Mise en page sur une seule page A4 : Formatez le contenu du CV pour qu'il tienne sur une seule page A4. Ceci est essentiel et crucial.
5. Utilisation de colonnes : Après la section "profil", sectionnner la feuille A4 en deux colonnes pour optimiser l'utilisation de l'espace.
6. Taille de police réduite : Utilisez une taille de police appropriée pour que le contenu tienne sur une seule page avec un bon formatage et une bonne lisibilité.
7. Réduction de l'espacement vertical : Réduisez l'espacement vertical (\\vspace) entre les sections pour économiser de l'espace.
8. Utilisation appropriée des commandes LaTeX pour les colonnes : Utilisez les commandes appropriées pour gérer les colonnes, telles que celles du package `multicols`.

Objectif final :
Fournissez un code latex complet du contenu où toutes les données sont correctement insérées et structurées, avec une mise en page optimisée pour tenir sur une seule page A4. Assurez-vous que le document final est professionnel, visuellement attrayant et parfaitement formaté.

Voici le modèle LaTeX :
{latex_template}

Voici les données JSON :
{json.dumps(cv_data, indent=4)} """

# Initialiser le modèle HuggingFace
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",
    model_kwargs={"load_in_16bit": True},
    temperature=0.9,
    repetition_penalty=1.03,
    top_p=0.9,
    huggingfacehub_api_token="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"
)

# Préparer les messages pour le modèle
messages = [
    {"role": "user", "content": prompt},
]

# Générer le contenu LaTeX
response_latex = llm.invoke(messages)

# Enregistrer le LaTeX final dans un fichier
with open('cv1_final.tex', 'w') as output_file:
    output_file.write(response_latex)

print("Le CV a été généré avec succès et enregistré dans 'cv3_final.tex'.")
