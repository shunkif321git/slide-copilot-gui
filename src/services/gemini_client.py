import os
import google.generativeai as genai

genai.config(api_key=os.getenv("GEMINI_API_KEY"))

def generate_slide_outline(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-pro")
    responce = model.generate_content(prompt)
    return response.text
