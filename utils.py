import re
import hashlib

def slugify(input: str) -> str:
    slugified_string = " ".join(re.sub(r"[^a-zA-Z0-9 ]", "", input).split()).lower().replace(" ", "-")

    return slugified_string