import json
from services.google.generative_ai import GoogleGenerativeModelInit

# Read the LaTeX file
with open('templates/cv6.tex', 'r') as latex_file:
    latex_template = latex_file.read()

# Load the JSON file
with open('cv_nabi.json', 'r') as json_file:
    cv_data = json.load(json_file)

prompt = f"""
Below you will find a LaTeX template of a CV and the JSON data of a CV. Your task is to properly structure each section of the CV according to the LaTeX template and insert all the information from the JSON data.

Mandatory instructions:
1. Ensure that each section of the JSON is represented in the final LaTeX document.
2. Add additional sections if necessary to include all the information from the JSON.
3. Remove sections from the template that do not correspond to the JSON data.
4. Format the content so that everything fits on a single A4 page. This is essential and crucial.
5. Split the page into two columns after the "profile" section to use space optimally. Use the `multicols` package to manage columns.
6. Use a smaller font size (e.g., \\small or \\footnotesize) if necessary to make the content fit on a single page.
7. Reduce vertical spacing (\\vspace) between sections to save space.
8. Condense text where possible by shortening sentences and summarizing information.
9. Prioritize key sections like "Profile", "Professional Experience", and "Education" over less critical sections.
10. Use appropriate LaTeX commands to ensure a professional and visually appealing layout.

Here is the LaTeX template:
{latex_template}

Here is the JSON data:
{json.dumps(cv_data, indent=4)}

Please provide the complete LaTeX document with all CV data correctly inserted and structured. Ensure that the final document is optimized to fit on a single A4 page.

Note: You are an expert in design and highly proficient in LaTeX. Apply your expertise to ensure the final output is professional, visually appealing, and perfectly formatted.
"""


# Initialize the Gemini model
model = GoogleGenerativeModelInit("gemini-pro")

# Generate the complete LaTeX content
response_latex = model.generate_content([prompt])

# Save the final LaTeX to a file
with open('cv6_nabi_final.tex', 'w') as output_file:
    output_file.write(response_latex)

print("The CV has been successfully generated and saved in 'cv_final.tex'.")