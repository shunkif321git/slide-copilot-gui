# -*- coding: utf-8 -*-
"""slide_gui.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AbjGxzAMooiuapWOkcZnFv2mjzUIbS-R
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class SlideCopilotApp:
  def __init__(self, root):
    self.root = root
    self.root.title("講義スライド作成コパイロット")
    self.chapter_count = 0
    self.chapter_entries = []

    self.create_main_from()

  def create_main_from(self):
    #講座情報フレーム
    lecture_frame = ttk.LabelFrame(self.root, text='講座情報')
    lecture_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    ttk.Label(lecture_frame, text="講座タイトル:").grid(row=0, column=0, sticky="e")
    self.title_entry = ttk.Entry(lecture_frame, width=40)
    self.title_entry.grid(row=0, column=1)

    ttk.Label(lecture_frame, text="作成者・機関名:").grid(row=1, column=0, sticky="e")
    self.author_entry = ttk.Entry(lecture_frame, width=40)
    self.author_entry.grid(row=1, column=1)

    ttk.Label(lecture_frame, text="日付:").grid(row=2, column=0, sticky="e")
    self.date_entry = ttk.Entry(lecture_frame, width=40)
    self.date_entry.grid(row=2, column=1)

    # 章構成フレーム
    chapter_frame = ttk.LabelFrame(self.root, text="章構成")
    chapter_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    self.chapter_container = ttk.Frame(chapter_frame)
    self.chapter_container.grid(row=0, column=0, columnspan=2)

    self.add_chapter_button = ttk.Button(chapter_frame, text="章を追加", command=self.add_chapter)
    self.add_chapter_button.grid(row=1, column=0, pady=5)

    self.generate_button = ttk.Button(chapter_frame, text="生成（仮）", command=self.generate)
    self.generate_button.grid(row=1, column=1, pady=5)

  def add_chapter(self):
    row = self.chapter_count
    frame = ttk.Frame(self.chapter_container)
    frame.grid(row=row, column=0, sticky="w", pady=2)

    ttk.Label(frame, text=f"第{row + 1}章:").grid(row=0, column=0, sticky="e")
    chapter_title = ttk.Entry(frame, width=40)
    chapter_title.grid(row=0, column=1)
    self.chapter_entries.append(chapter_title)

    self.chapter_count += 1

  def generate(self):
    title = self.title_entry.get()
    author = self.author_entry.get()
    date = self.date_entry.get()
    chapters = [e.get() for e in self.chapter_entries if e.get()]

    summary = f"講座のタイトル:{title}\n作成者: {author}\n日付: {date}\n\n章構成:\n"
    for i, ch in enumerate(chapters):
      summary += f"  第{i+1}章: {ch}\n"

    messagebox.showinfo("入力内容の確認", summary)

if __name__ == "__main__":
  root = tk.Tk()
  app = SlideCopilotApp(root)
  root.mainloop()