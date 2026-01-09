from dataclasses import dataclass
from typing import Dict

@dataclass
class Chunk:
    name: str
    text: str
    metadata: Dict