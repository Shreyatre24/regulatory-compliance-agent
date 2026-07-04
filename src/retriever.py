"""Retriever: given a requirement, return the most relevant clauses from the regulation (RAG).

v0.1 can be naive (keyword / simple similarity). A vector store is explicitly v0.2 —
do NOT build one yet (see MILESTONES.md). Keep it small.

TODO(you): replace the stub with real retrieval. Simplest path: chunk the regulation,
embed chunks + the requirement, return top-k by cosine similarity. Or start even simpler
with keyword overlap and upgrade later.
"""
from typing import List, Dict


class Retriever:
    def __init__(self, regulation_text: str):
        self.regulation_text = regulation_text
        # TODO(you): build your chunks / index here.

    def retrieve(self, requirement: Dict, k: int = 3) -> List[str]:
        # --- STUB: returns a mock clause so the pipeline runs ---
        return [f"[stub clause relevant to {requirement['id']}]"]
