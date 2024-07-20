
import google.generativeai as genai

from config.globals import GOOGLE_AI_API_KEY


# Configure GenAI
genai.configure(api_key=GOOGLE_AI_API_KEY)


class GoogleGenerativeModelInit:
  def __init__(self, model_name:str):
    """
      model_name: str - The name of the model to initialise. enum: ["gemini-pro", "gemini-vision"]
    """
    self.model_name = model_name
    self.api_key = GOOGLE_AI_API_KEY
    
    # Initialise the model
    self.model = genai.GenerativeModel(self.model_name)

  def generate_content(self, prompt: str):
      """
      Generate content using the specified model.
      
      prompt: str - The prompt to generate content for.
      
      Returns:
          str - The generated content.
      """
      response = self.model.generate_content(prompt)
      return response.text
