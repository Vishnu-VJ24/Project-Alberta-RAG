"""
Alberta Tourism Corridor RAG System
Corpus ingestion pipeline.

Reads markdown files from docs/ and reports/, splits them into overlapping
chunks, embeds with sentence-transformers (all-MiniLM-L6-v2), and saves a
FAISS index to data/vector_store/.

Usage:
    python src/ingest.py

Run this locally whenever you add new documents to the corpus.
Then commit the updated data/vector_store/ files to GitHub.
"""

import os
import json
import sys
import numpy as np
from pathlib import Path
from datetime import datetime

# Ensure project root is on path
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))


# ─── Config ──────────────────────────────────────────────────────────────────
DOCS_DIRS = ["docs", "reports"]          # Directories to ingest
VECTOR_STORE_DIR = ROOT / "data" / "vector_store"
CHUNK_SIZE_WORDS = 300                   # Approximate words per chunk
CHUNK_OVERLAP_WORDS = 50                 # Overlap between chunks
EMBEDDING_MODEL = "all-MiniLM-L6-v2"    # CPU-compatible, free, high quality
SKIP_FILES = {".gitkeep"}               # Files to skip


# ─── Helpers ─────────────────────────────────────────────────────────────────
def load_markdown(filepath: Path) -> str:
    """Read a markdown file and return its text content."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE_WORDS,
               overlap: int = CHUNK_OVERLAP_WORDS) -> list[str]:
    """
    Split text into overlapping chunks by approximate word count.
    Tries to split on double newlines (paragraph boundaries) first.
    """
    # Split into paragraphs
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

    chunks = []
    current_words = []
    current_len = 0

    for para in paragraphs:
        para_words = para.split()
        para_len = len(para_words)

        if current_len + para_len > chunk_size and current_words:
            # Save current chunk
            chunks.append(" ".join(current_words))
            # Keep overlap from end of current chunk
            current_words = current_words[-overlap:] if overlap > 0 else []
            current_len = len(current_words)

        current_words.extend(para_words)
        current_len += para_len

    # Save final chunk
    if current_words:
        chunks.append(" ".join(current_words))

    return chunks


def classify_source_type(filepath: Path) -> str:
    """Classify source type from filename."""
    name = filepath.stem.lower()
    if "weekly_report" in name:
        return "weekly_report"
    if "literature" in name:
        return "literature_review"
    if "tdz" in name:
        return "tdz_analysis"
    if "hub" in name:
        return "hub_analysis"
    if "rag" in name:
        return "rag_design"
    if "plan" in name:
        return "project_plan"
    if "log" in name:
        return "daily_log"
    if "candidate" in name:
        return "hub_analysis"
    if "data_inventory" in name:
        return "data_inventory"
    return "project_note"


def get_metadata(filepath: Path) -> dict:
    """Build metadata dict for a source file."""
    return {
        "filepath": str(filepath.relative_to(ROOT)),
        "filename": filepath.name,
        "source_type": classify_source_type(filepath),
        "geography": "Central Alberta — Bow and Red Deer River Corridors",
        "publisher": "Project Internal",
        "reliability_tier": "Tier 5 — internal project notes",
        "ingested_at": datetime.now().isoformat(),
    }


# ─── Main ────────────────────────────────────────────────────────────────────
def build_index():
    print("=" * 60)
    print("Alberta Tourism Corridor RAG — Corpus Ingestion")
    print("=" * 60)

    # Load embedding model
    print(f"\nLoading embedding model: {EMBEDDING_MODEL}")
    try:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer(EMBEDDING_MODEL)
    except ImportError:
        print("ERROR: sentence-transformers not installed.")
        print("Run: pip install sentence-transformers")
        sys.exit(1)

    all_chunks: list[str] = []
    all_metadata: list[dict] = []

    # Collect and chunk documents
    for dir_name in DOCS_DIRS:
        dir_path = ROOT / dir_name
        if not dir_path.exists():
            print(f"  Skipping {dir_name}/ (not found)")
            continue

        md_files = sorted(dir_path.glob("*.md"))
        print(f"\nProcessing {dir_name}/ — {len(md_files)} markdown files")

        for filepath in md_files:
            if filepath.name in SKIP_FILES:
                continue

            text = load_markdown(filepath)
            chunks = chunk_text(text)
            meta = get_metadata(filepath)

            for i, chunk in enumerate(chunks):
                all_chunks.append(chunk)
                all_metadata.append({
                    **meta,
                    "chunk_id": f"{filepath.stem}_chunk_{i:03d}",
                    "chunk_index": i,
                    "total_chunks": len(chunks),
                    "chunk_text": chunk,
                })

            print(f"  {filepath.name}: {len(chunks)} chunks")

    total = len(all_chunks)
    print(f"\nTotal chunks to embed: {total}")

    if total == 0:
        print("No documents found. Nothing to index.")
        sys.exit(0)

    # Generate embeddings
    print("\nGenerating embeddings (this may take a moment)...")
    embeddings = model.encode(
        all_chunks,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True,   # Normalize for cosine similarity
    ).astype(np.float32)

    print(f"Embedding shape: {embeddings.shape}")

    # Build FAISS index
    try:
        import faiss
    except ImportError:
        print("ERROR: faiss-cpu not installed.")
        print("Run: pip install faiss-cpu")
        sys.exit(1)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)   # Inner product = cosine sim after normalize
    index.add(embeddings)
    print(f"FAISS index built: {index.ntotal} vectors, dimension {dimension}")

    # Save index and metadata
    VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)
    index_path = VECTOR_STORE_DIR / "index.faiss"
    metadata_path = VECTOR_STORE_DIR / "metadata.json"

    faiss.write_index(index, str(index_path))

    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(all_metadata, f, indent=2, ensure_ascii=False)

    print(f"Saved:")
    print(f"  Index    -> {index_path}")
    print(f"  Metadata -> {metadata_path}")
    print(f"\nDone. {total} chunks from {len(DOCS_DIRS)} directories indexed.")
    print("Commit data/vector_store/ to GitHub to deploy the updated corpus.")


if __name__ == "__main__":
    build_index()
