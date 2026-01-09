import os
import logging
from pathlib import Path
from dotenv import load_dotenv

from scraper import get_data
from markdown_formatter import create_markdown_directory, convert_article_to_markdown
from chunker import chunk_markdown
from openai_client import OpenAIClient

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

load_dotenv()

ARTICLES_DIRECTORY = os.getenv("ARTICLE_MARKDOWN_OUTPUT")
VECTOR_STORE_NAME = os.getenv("OPENAI_VECTOR_STORE_NAME")
OPENAI_API_KEY = os.getenv("OPEN_API_KEY")

def main():
    url = "https://support.optisigns.com/api/v2/help_center/en-us/articles.json?per_page=40"
    articles = get_data(url)

    create_markdown_directory(ARTICLES_DIRECTORY)

    client = OpenAIClient(
        openai_api_key=OPENAI_API_KEY,
        vector_store_name=VECTOR_STORE_NAME,
    )

    total_files = len(articles)
    total_chunks = 0

    for article in articles:
        convert_article_to_markdown(article, ARTICLES_DIRECTORY)

        f = open(ARTICLES_DIRECTORY + "/" + article.slug + ".md", "r", encoding="utf-8")

        chunks = chunk_markdown(
            f.read(),
            article_id=article.id,
            slug=article.slug,
            title=article.title,
            source_url=article.source_url,
            updated_at=article.updated_at
        )

        total_chunks += len(chunks)

        logging.info(f"Normalized: {article.slug}.md | Chunks generated: {len(chunks)}")

        # Upload chunks to vector store
        client.upload_chunks(chunks)

    logging.info("--- FINAL EMBEDDING REPORT ---")
    logging.info(f"Total Files Processed: {total_files}")
    logging.info(f"Total Chunks Embedded: {total_chunks}")

if __name__ == "__main__":
    main()