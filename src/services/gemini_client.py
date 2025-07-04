import os
import google.generativeai as genai

genai.config(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_slide_outline(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

def generate_explanation(keyword: str) -> str:
    prompt = f"「{keyword}」という用語について、スライドに使えるような喀血な説明文（50～100字程度）を生成してください。"
    response = model.generate_content(prompt)
    return response.text

def generate_figure_description(title: str) -> str:
    prompt = f"「{title}」という図の説明文をスライド用に簡潔に（1～2文）作成してください。"
    response = model.generate_content(prompt)
    return response.text

