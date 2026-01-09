import requests
from article import Article
from utils import slugify

def get_data(url: str) -> List[Article]:
    response = requests.get(url)
    article_list = []

    if response.status_code != 200:
        return
    else:
        data = response.json()

        for a in data["articles"]:
            slug = str(a["id"]) + "-" + slugify(a["title"])

            article = Article(a["id"], a["title"], a["html_url"], slug, a["body"], a["updated_at"])

            article_list.append(article)

        return article_list