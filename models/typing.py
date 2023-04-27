from typing import Dict, List
from pydantic import BaseModel


class TextInput(BaseModel):
    text: str


class ListTextsInput(BaseModel):
    texts: List[str]

