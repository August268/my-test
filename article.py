from dataclasses import dataclass

@dataclass
class Article:
    id: int
    title: str
    source_url: str
    slug: str
    html_body: str
    updated_at: str