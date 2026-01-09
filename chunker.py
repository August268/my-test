from chunk import Chunk
from utils import stable_hash

MAX_CHARS = 2000

def split_by_h2(markdown: str) -> List[str]:
    parts = []
    current = []

    lines = markdown.splitlines()

    for line in lines:
        if (line.startswith("## ")):
            if current:
                parts.append("\n".join(current).strip())
                current = []
        current.append(line)

    if current:
        parts.append("\n".join(current).strip())
    
    return [p for p in parts if p]

def split_large_section(text: str, max_chars: int) -> List[int]:
    if len(text) <= max_chars:
        return [text]
    
    chunks = []
    buffer = ""

    for block in text.split("\n\n"):
        if len(buffer) + len(block) < max_chars:
            buffer += ("\n\n" if buffer else "") + block
        else:
            chunks.append(buffer)
            buffer = block
    
    if buffer:
        chunks.append(buffer)
    
    return chunks

def chunk_markdown(markdown: str, *, article_id: int, slug: str, title: str, source_url: str) -> List[Chunk]:
    sections = split_by_h2(markdown)
    chunks: List[Chunk] = []
    index = 0

    for section in sections:
        sub_chunks = split_large_section(section, MAX_CHARS)

        for text in sub_chunks:
            chunk_id = f"{article_id}:{index}:{stable_hash(text)[:8]}"

            metadata = {
                "article_id": article_id,
                "slug": slug,
                "title": title,
                "source": source_url,
                "chunk_index": index,
            }

            chunks.append(
                Chunk(chunk_id, text, metadata)
            )

            index += 1
    
    return chunks
