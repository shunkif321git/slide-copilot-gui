# 全自動スライド生成スクリプト
from pptx_writer import create_pptx_with_slides
from gemini_client import generate_slide_outline, generate_slide_content

def generate_all_slides(lecture_title: str, output_file: str):
    print(f"[1] 章構成を生成中...")
    chapters = generate_slide_outline(lecture_title)

    print(f"[2] 各章の説明文を生成中...")
    slides = []
    for chapter in chapters:
        print(f"   - {chapter} ...")
        content = generate_slide_content(chapter)
        slides.append({"title": chapter, "content": content})

    print(f"[3] スライドに書き出し中...")
    create_pptx_with_slides(output_file, slides)
    print(f"[完了] {output_file}を生成しました")

if __name__ == "__main__":
    # ここで講義タイトルを入力
    title = "AIの基礎と応用" # ⇚変更の必要あり
    generate_all_slides(title, "auto_generated_slides.pptx")
