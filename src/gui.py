import tkinter as tkinter
from tkinter import messagebox
from src.services.gemini_client import generate_slide_outline

def run_gemini():
    topic = entry.get()
    if not topic:
        messagebox.showwarning("入力エラー","講義のタイトルを入力してください。")
        return
    
    prompt = f"「{topic}」という講義タイトルにふさわしい章立て（3～5章）を提案してください。"
    result = generate_slide_outline(prompt)
    output.delete("1.0", tk.END)
    output.insert(tk.END, result)

def launch_gui():
    root = tk.Tk()
    root.title("Slide Copilot GUI")

    tk.Label(root, text="講義タイトル:").pack(pady=5)
    global entry
    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)

    tk.Button(root, text="章立てを生成", command=run_gemini).pack(pady=5)

    global output
    output = tk.Text(root, height=15, width=60)
    output.pack(pady=10)

    root.mainloop()