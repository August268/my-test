import re

def slugify(input: str) -> str:
    slugified_string = " ".join(re.sub(r"[^a-zA-Z0-9 ]", "", input).split()).lower().replace(" ", "_")

    return slugified_string