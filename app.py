"""
Alberta Tourism Corridor RAG — Streamlit Application
app.py

Stakeholder-facing research assistant for the Bow and Red Deer River Corridor
tourism strategy. Powered by FAISS + sentence-transformers + Groq Llama 3.3.

Deploy free on: https://streamlit.io/cloud
"""

import os
import sys
import streamlit as st
from pathlib import Path

# ── Path setup ────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

# ── Page config (MUST be first Streamlit call) ────────────────────────────────
st.set_page_config(
    page_title="Alberta Tourism Corridor RAG",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "Central Alberta Tourism Corridor Strategy — RAG Research Assistant · 2026",
    },
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* ── Background ── */
.stApp {
    background: linear-gradient(160deg, #0d1117 0%, #161b27 50%, #0d1f17 100%);
    min-height: 100vh;
}

/* ── Header ── */
.rag-header {
    text-align: center;
    padding: 2rem 0 0.5rem;
}
.rag-header h1 {
    font-size: 2.6rem;
    font-weight: 700;
    background: linear-gradient(90deg, #4ade80, #86efac, #bbf7d0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.25rem;
    letter-spacing: -0.5px;
}
.rag-header .subtitle {
    color: rgba(255,255,255,0.5);
    font-size: 0.95rem;
    font-weight: 400;
    letter-spacing: 0.3px;
}

/* ── Metric cards ── */
div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(74,222,128,0.2);
    border-radius: 10px;
    padding: 0.75rem 1rem;
}
div[data-testid="metric-container"] label {
    color: rgba(255,255,255,0.5) !important;
    font-size: 0.8rem !important;
}
div[data-testid="metric-container"] div[data-testid="stMetricValue"] {
    color: #4ade80 !important;
    font-size: 1.5rem !important;
    font-weight: 600 !important;
}

/* ── Answer box ── */
.answer-box {
    background: rgba(74,222,128,0.05);
    border: 1px solid rgba(74,222,128,0.25);
    border-radius: 12px;
    padding: 1.5rem 1.75rem;
    margin: 1rem 0;
    line-height: 1.75;
    color: rgba(255,255,255,0.9);
    font-size: 0.97rem;
}

/* ── Text area ── */
.stTextArea textarea {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(74,222,128,0.35) !important;
    color: rgba(255,255,255,0.9) !important;
    border-radius: 10px !important;
    font-size: 0.95rem !important;
    line-height: 1.6 !important;
}
.stTextArea textarea:focus {
    border-color: rgba(74,222,128,0.65) !important;
    box-shadow: 0 0 0 2px rgba(74,222,128,0.15) !important;
}

/* ── Search button ── */
.stButton > button {
    background: linear-gradient(135deg, #16a34a, #4ade80) !important;
    color: #0d1117 !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    border: none !important;
    border-radius: 9px !important;
    padding: 0.6rem 1.5rem !important;
    width: 100% !important;
    transition: all 0.2s ease !important;
    letter-spacing: 0.3px !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(74,222,128,0.35) !important;
}
.stButton > button:active {
    transform: translateY(0px) !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.02) !important;
    border-right: 1px solid rgba(255,255,255,0.07) !important;
}
[data-testid="stSidebar"] .stMarkdown {
    color: rgba(255,255,255,0.75);
}

/* ── Expanders (source cards) ── */
details {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 8px !important;
    margin-bottom: 0.5rem !important;
}
summary {
    color: rgba(255,255,255,0.8) !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
}

/* ── Divider ── */
hr {
    border-color: rgba(255,255,255,0.08) !important;
    margin: 1.25rem 0 !important;
}

/* ── Info / warning ── */
.stAlert {
    border-radius: 10px !important;
}

/* ── Sidebar example buttons ── */
[data-testid="stSidebar"] .stButton > button {
    background: rgba(255,255,255,0.05) !important;
    color: rgba(255,255,255,0.8) !important;
    font-weight: 400 !important;
    font-size: 0.82rem !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    text-align: left !important;
    padding: 0.4rem 0.75rem !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(74,222,128,0.08) !important;
    border-color: rgba(74,222,128,0.3) !important;
    transform: none !important;
    box-shadow: none !important;
}

/* ── Select/slider ── */
.stSlider [data-baseweb="slider"] div[role="slider"] {
    background: #4ade80 !important;
}
</style>
""",
    unsafe_allow_html=True,
)


# ── Retriever (cached so it loads only once) ──────────────────────────────────
@st.cache_resource(show_spinner="Loading knowledge base…")
def load_retriever():
    try:
        from src.retrieval import TourismRAGRetriever
        r = TourismRAGRetriever()
        return r, None
    except FileNotFoundError as e:
        return None, str(e)
    except Exception as e:
        return None, f"{type(e).__name__}: {e}"


# ── Groq client ───────────────────────────────────────────────────────────────
def get_groq_client():
    api_key = None
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        api_key = os.environ.get("GROQ_API_KEY")

    if not api_key:
        return None
    try:
        from groq import Groq
        return Groq(api_key=api_key)
    except ImportError:
        return None


# ── LLM answer generation ─────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are a research assistant for the Central Alberta Tourism Corridor Strategy project.
Your role is to help municipal staff, tourism operators, transportation agencies, and summit stakeholders
understand tourism trends, hub recommendations, TDZ alignment, transportation needs, and economic impact
for the Bow and Red Deer River corridors.

Rules:
- Answer using ONLY the context provided below. Do not use external knowledge.
- Cite the source document name for each claim (e.g. "According to candidate_hub_table.md…").
- Clearly separate evidence from interpretation.
- If the context does not have enough information, say so explicitly.
- Do not fabricate statistics, job figures, budgets, or economic multipliers.
- Keep answers clear, concise, and stakeholder-ready."""


def generate_answer(client, query: str, context: str) -> str:
    user_msg = (
        f"Context from the project knowledge base:\n\n{context}\n\n"
        f"---\n\nQuestion: {query}\n\nAnswer (cite sources):"
    )
    resp = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg},
        ],
        temperature=0.1,
        max_tokens=900,
    )
    return resp.choices[0].message.content


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🏔️ About")
    st.markdown(
        """
This tool lets you query the research corpus for the
**Central Alberta Tourism Corridor Strategy** using
retrieval-augmented generation (RAG).

**Corridors covered:**
- 🌊 Bow River Corridor
- 🌊 Red Deer River Corridor

**TDZs indexed:**
- David Thompson
- Olds to Lacombe
- Cochrane to Sundre
- Foothills
- Canadian Badlands
"""
    )

    st.divider()
    st.markdown("### 💡 Example Questions")

    EXAMPLES = [
        "Which TDZ has the highest economic potential?",
        "What activities are recommended for the Drumheller badlands hub?",
        "What are the transportation gaps across all five candidate hubs?",
        "Which hub has the strongest stakeholder readiness?",
        "What data is still needed for the west-central adventure gateway?",
        "How does the RAG system support stakeholder decision-making?",
        "Which communities benefit most from rural tourism dispersal?",
        "What is the Foothills TDZ's estimated tourism spend growth?",
    ]

    for q in EXAMPLES:
        if st.button(q, key=f"ex_{q}", use_container_width=True):
            st.session_state["_query_preset"] = q

    st.divider()
    st.markdown("### ⚙️ Settings")
    top_k = st.slider("Sources to retrieve", min_value=2, max_value=8, value=4, step=1)

    source_type_options = ["All source types"]
    retriever, _err = load_retriever()
    if retriever:
        source_type_options += retriever.source_types

    source_filter_label = st.selectbox("Filter by source type", source_type_options)
    source_filter = None if source_filter_label == "All source types" else source_filter_label

    st.divider()
    st.caption("Central Alberta Tourism Corridor Project · Week 2 · 2026")


# ── Main header ───────────────────────────────────────────────────────────────
st.markdown(
    """
<div class="rag-header">
    <h1>🏔️ Alberta Tourism Corridor RAG</h1>
    <p class="subtitle">
        Research Assistant &nbsp;·&nbsp; Bow &amp; Red Deer River Corridors
        &nbsp;·&nbsp; Powered by FAISS + Groq Llama 3.3
    </p>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# ── Load retriever ────────────────────────────────────────────────────────────
retriever, load_error = load_retriever()

if load_error:
    st.error(
        f"""
**⚠️ Knowledge base not found.**

Run the ingestion script first to build the FAISS index:

```bash
pip install -r requirements.txt
python src/ingest.py
```

Then restart the app.

_Technical detail:_ `{load_error}`
"""
    )
    st.stop()

# ── Corpus metrics ────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
c1.metric("📄 Indexed Chunks", retriever.corpus_size)
c2.metric("🗂️ Source Files", len(retriever.source_files))
c3.metric("🗺️ TDZs Covered", "5")
c4.metric("🏔️ Candidate Hubs", "5")

st.divider()

# ── Query input ───────────────────────────────────────────────────────────────
preset = st.session_state.pop("_query_preset", "")
default_val = preset if preset else st.session_state.get("_last_query", "")

col_q, col_btn = st.columns([5, 1])
with col_q:
    query = st.text_area(
        "Ask a question about the Alberta tourism corridor strategy:",
        value=default_val,
        height=90,
        placeholder="e.g. Which hub has the strongest economic potential and why?",
        key="query_input",
    )
with col_btn:
    st.write("")
    st.write("")
    st.write("")
    search = st.button("🔍 Search", use_container_width=True)

# ── Results ───────────────────────────────────────────────────────────────────
if search and query.strip():
    st.session_state["_last_query"] = query

    with st.spinner("Retrieving relevant context…"):
        results = retriever.retrieve(query, top_k=top_k, source_type_filter=source_filter)
        context = retriever.format_context(results)

    if not results:
        st.warning("No relevant context found for that query. Try rephrasing or broadening your question.")
        st.stop()

    client = get_groq_client()

    if client:
        with st.spinner("Generating answer with Groq Llama 3.3…"):
            try:
                answer = generate_answer(client, query, context)
                st.markdown("### 💬 Answer")
                st.markdown(
                    f'<div class="answer-box">{answer}</div>',
                    unsafe_allow_html=True,
                )
            except Exception as e:
                st.error(f"LLM error: {e}")
                st.markdown("### 📄 Retrieved Context (LLM unavailable)")
                st.code(context)
    else:
        st.warning(
            """
**GROQ_API_KEY not configured.** Showing retrieved context without AI-generated answer.

To enable answers:
1. Get a free key at [console.groq.com](https://console.groq.com)
2. Add to `.streamlit/secrets.toml`:
   ```toml
   GROQ_API_KEY = "gsk_your_key_here"
   ```
3. Restart the app.
"""
        )
        st.markdown("### 📄 Retrieved Context")
        st.code(context, language="markdown")

    st.markdown("### 📚 Sources Retrieved")
    for i, r in enumerate(results, 1):
        relevance_pct = int(r["score"] * 100)
        with st.expander(
            f"Source {i} — {r['filename']}  |  relevance: {relevance_pct}%",
            expanded=(i == 1),
        ):
            col_a, col_b = st.columns(2)
            col_a.markdown(f"**Type:** `{r['source_type']}`")
            col_b.markdown(f"**Chunk:** `{r['chunk_id']}`")
            st.markdown(f"**Path:** `{r['filepath']}`")
            st.divider()
            st.markdown(r["chunk_text"])

elif search:
    st.warning("Please enter a question.")

else:
    st.info(
        "👆 Type a question above or click an example prompt in the sidebar to get started."
    )
