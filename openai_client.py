import io
from typing import List
from openai import OpenAI
from chunk import Chunk

class OpenAIClient:
    def __init__(self, openai_api_key: str, vector_store_name: str):
        self.client = OpenAI(api_key=openai_api_key)
        self.vector_store_name = vector_store_name
        self.vector_store_id = self.get_or_create_vector_storage()
    
    def get_or_create_vector_storage(self) -> str:
        stores = self.client.vector_stores.list().data

        for store in stores:
            if store.name == self.vector_store_name:
                return store.id
        
        new_vector_store = self.client.vector_stores.create(name = self.vector_store_name)
        return new_vector_store.id

    def upload_chunks(self, chunks: List[Chunk]):
        for chunk in chunks:
            metadata = f"""---
article_id: {chunk.metadata.get("article_id")}
title: "{chunk.metadata.get("title")}"
slug: {chunk.metadata.get("slug")}
source: {chunk.metadata.get("source")}
chunk_index: {chunk.metadata.get("chunk_index")}
"updayed_at": {chunk.metadata.get("updated_at")}
---
            """
            content = metadata + chunk.text.strip()

            if not content:
                continue

            # Create in-memory file
            file_obj = io.BytesIO(content.encode("utf-8"))
            file_obj.name = f"{chunk.name}.md"

            # check for duplicate files
            for file in self.client.files.list().data:
                if file.filename.removesuffix(".md") == chunk.name:
                    self.client.files.delete(file.id)

            # Upload file
            uploaded_file = self.client.files.create(
                file=file_obj,
                purpose="assistants"
            )

            # Attach to vector store
            self.client.vector_stores.files.create(
                vector_store_id=self.vector_store_id,
                file_id=uploaded_file.id
            )