from scraper import get_data
from markdown_formatter import (convert_article_to_markdown, create_markdown_directory)

def main():
    url = "https://support.optisigns.com/api/v2/help_center/en-us/articles.json?per_page=50"
    result = get_data(url)

    articles = result

    create_markdown_directory()
    
    for a in articles:
        markdown = convert_article_to_markdown(a)

if __name__ == "__main__":
    main()