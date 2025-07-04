import os
import google.generativeai as gemini

gemini.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_slide_outline(title: str) -> list:
    prompt = f"""
    「{title}」という講義の章構成（3～5章）を提案してください。
    出力は以下の形式で：
    1. 〇〇
    2. 〇〇
    3. 〇〇
    """
    response = model.generate_content(prompt)
    # シンプルに各行を章タイトルとして扱う
    lines = response.text.strip().split("\n")
    chapters = [line.split(".", 1)[-1] for line in lines if ". " in line]
    return chapters

def generate_slide_content(chapter_title: str) -> str:
    prompt = f"""
    「{chapter_title}」という章について、スライド1～2枚分に相当する簡潔な説明文を生成してください。
    出力は200字程度で箇条書き形式にしてください。
    """
    response = model.generate_content(prompt)
    return response.text
