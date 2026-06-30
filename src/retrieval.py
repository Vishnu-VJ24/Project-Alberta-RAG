"""
Alberta Tourism Corridor RAG System
Semantic retrieval module.

Loads the FAISS index and metadata built by src/ingest.py,
embeds incoming queries, and returns the top-k most relevant chunks.
"""

import json
import sys
import numpy as np
from pathlib import Path
from typing import Optional

ROOT = Path(__file__).parent.parent
VECTOR_STORE_DIR = ROOT / "data" / "vector_store"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
DEFAULT_TOP_K = 5


class TourismRAGRetriever:
    """
    Retriever for the Alberta Tourism Corridor RAG corpus.

    Loads the FAISS index at startup and provides a retrieve() method
    that returns the top-k most semantically similar chunks for a query.
    """

    def __init__(
        self,
        vector_store_dir: Path = VECTOR_STORE_DIR,
        model_name: str = EMBEDDING_MODEL,
    ):
        self.vector_store_dir = Path(vector_store_dir)
        self.model_name = model_name
        self._model = None
        self.index = None
        self.metadata: list[dict] = []
        self._load()

    # ─── Loading ─────────────────────────────────────────────────────────────
    def _load(self):
        """Load FAISS index and metadata from disk."""
        index_path = self.vector_store_dir / "index.faiss"
        meta_path = self.vector_store_dir / "metadata.json"

        if not index_path.exists():
            raise FileNotFoundError(
                f"FAISS index not found at {index_path}.\n"
                "Run  python src/ingest.py  to build the index first."
            )

        try:
            import faiss
        except ImportError:
            raise ImportError("faiss-cpu not installed. Run: pip install faiss-cpu")

        self.index = faiss.read_index(str(index_path))

        with open(meta_path, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

    @property
    def model(self):
        """Lazy-load the embedding model."""
        if self._model is None:
            try:
                from sentence_transformers import SentenceTransformer
            except ImportError:
                raise ImportError(
                    "sentence-transformers not installed. "
                    "Run: pip install sentence-transformers"
                )
            self._model = SentenceTransformer(self.model_name)
        return self._model

    # ─── Retrieval ───────────────────────────────────────────────────────────
    def retrieve(
        self,
        query: str,
        top_k: int = DEFAULT_TOP_K,
        source_type_filter: Optional[str] = None,
    ) -> list[dict]:
        """
        Retrieve the top-k most relevant chunks for a query.

        Args:
            query:              The user's question or search string.
            top_k:              Number of chunks to return.
            source_type_filter: Optional. Filter results to a specific source type
                                (e.g. 'tdz_analysis', 'hub_analysis', 'daily_log').

        Returns:
            List of dicts, each with:
                - score       (float, cosine similarity 0–1)
                - chunk_text  (str)
                - filename    (str)
                - source_type (str)
                - chunk_id    (str)
                - filepath    (str)
        """
        # Embed query
        query_vec = self.model.encode(
            [query],
            convert_to_numpy=True,
            normalize_embeddings=True,
        ).astype(np.float32)

        # Search (fetch extra if filtering)
        search_k = top_k * 4 if source_type_filter else top_k
        search_k = min(search_k, self.index.ntotal)

        scores, indices = self.index.search(query_vec, search_k)

        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx < 0:
                continue
            meta = self.metadata[idx]

            if source_type_filter and meta.get("source_type") != source_type_filter:
                continue

            results.append(
                {
                    "score": float(score),
                    "chunk_text": meta["chunk_text"],
                    "filename": meta["filename"],
                    "source_type": meta["source_type"],
                    "chunk_id": meta["chunk_id"],
                    "filepath": meta["filepath"],
                    "geography": meta.get("geography", ""),
                    "reliability_tier": meta.get("reliability_tier", ""),
                }
            )

            if len(results) >= top_k:
                break

        return results

    def format_context(self, results: list[dict]) -> str:
        """
        Format retrieved chunks into a prompt-ready context string.

        Each source is labelled with its filename and relevance score
        so the LLM can cite it in its response.
        """
        if not results:
            return "No relevant context found in the knowledge base."

        parts = []
        for i, r in enumerate(results, 1):
            parts.append(
                f"[Source {i} | {r['filename']} | relevance: {r['score']:.3f}]\n"
                f"{r['chunk_text']}"
            )

        return "\n\n---\n\n".join(parts)

    # ─── Corpus Info ─────────────────────────────────────────────────────────
    @property
    def corpus_size(self) -> int:
        """Total number of indexed chunks."""
        return self.index.ntotal if self.index else 0

    @property
    def source_types(self) -> list[str]:
        """Unique source types in the corpus."""
        return sorted({m["source_type"] for m in self.metadata})

    @property
    def source_files(self) -> list[str]:
        """Unique source filenames in the corpus."""
        return sorted({m["filename"] for m in self.metadata})
