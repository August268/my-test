import re
import requests
from article import Article

def get_data(url: str) -> List[Article]:
    response = requests.get(url)
    article_list = []

    if response.status_code != 200:
        return
    else:
        data = response.json()

        for a in data["articles"]:
            slug = slugify(a["title"])

            article = Article(a["id"], a["title"], a["html_url"], slug, a["body"], a["updated_at"])

            article_list.append(article)

        return article_list

def slugify(input: str) -> str:
    slugified_string = " ".join(re.sub(r"[^a-zA-Z0-9 ]", "", input).split()).lower().replace(" ", "_")

    return slugified_string