from html_to_markdown import convert, ConversionOptions
import os

def convert_article_to_markdown(article: Article, destination_folder_name: str):
    file_destination = destination_folder_name + "/" + article.slug + ".md"

    options = ConversionOptions(
            strip_tags=["img", "nav", "ads"]
        )

    markdown = convert(article.html_body, options)

    with open(file_destination, "w", encoding="utf-8") as f:
        f.write(markdown)

def create_markdown_directory(folder_name):
    try:
        os.mkdir(folder_name)
        print(f"Directory '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{folder_name}' already exists.")