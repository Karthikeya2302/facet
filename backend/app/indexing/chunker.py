from __future__ import annotations

from llama_index.core.node_parser import SentenceSplitter

_splitter = SentenceSplitter(chunk_size=400, chunk_overlap=50)


def split(text: str) -> list[str]:
    return _splitter.split_text(text)
