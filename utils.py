import re
import hashlib

def slugify(input: str) -> str:
    slugified_string = " ".join(re.sub(r"[^a-zA-Z0-9 ]", "", input).split()).lower().replace(" ", "-")

    return slugified_string

def stable_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()