from html_to_markdown import convert
import os

folder_name = "files"

def convert_article_to_markdown(article: Article):
    file_name = article.slug + ".md"

    with open(folder_name + "/" + file_name, "w", encoding="utf-8") as f:
        f.write(f"---\nid: {article.id}\ntitle: {article.title}\nsource: {article.source_url}\nupdated_at: {article.updated_at}\n---\n")
        f.write(convert(article.html_body))

def create_markdown_directory():
    try:
        os.mkdir(folder_name)
        print(f"Directory '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{folder_name}' already exists.")