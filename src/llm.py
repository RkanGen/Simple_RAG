import os
import google.generativeai as genai
def get_llm():
    api_key = os.getenv("GOOGLE_API_KEY")
    # Configure the Gemini API using the loaded key
    genai.configure(api_key=api_key)
    text_model = genai.GenerativeModel('gemini-1.5-flash')
    response = text_model.generate_content()
    return response.text

