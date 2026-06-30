# Weekly Report - Week 2

## Monday, June 29, 2026

**Work Title:** Candidate Hub Table and Corridor Geography Analysis
**Time Reported:** 4 hours
**Work Type:** Research synthesis and strategic analysis

### Work Description

Built the first candidate hub table for the Bow and Red Deer River corridor project. The table converts Week 1 source review and the hub screening framework into five structured hub profiles. Each profile includes TDZ alignment, corridor connection, main access routes, key activities, economic potential indicators, target visitor markets, transportation gaps, data still needed, and RAG source documents required. Preliminary hub scores using the eight-criteria framework were also calculated for each candidate.

### Work Completed

- Created docs/candidate_hub_table.md with five candidate hub profiles.
- Scored each hub using the eight-criteria screening framework from Week 1.
- Identified the Bow Corridor Foothills Hub, Foothills Calgary Visitor Dispersal Hub, and Red Deer River Badlands Hub as the three highest-scoring candidates at 34 out of 40.
- Identified data gaps and RAG source documents still needed for each hub.
- Connected each hub to its primary TDZ and main highway access routes.

---

## Tuesday, June 30, 2026

**Work Title:** RAG System Foundation — Corpus Ingestion and Streamlit Application
**Time Reported:** 4 hours
**Work Type:** Technical development and system design

### Work Description

Built the technical foundation for the Alberta Tourism Corridor RAG system. The work covered the document ingestion pipeline, FAISS vector index construction, semantic retrieval module, and a Streamlit web application for stakeholder-facing question-and-answer. The system uses sentence-transformers for embeddings, FAISS for vector storage, and the Groq API for LLM inference. All project documents collected in Week 1 were ingested into the initial knowledge base.

### Research

#### Link to Article

https://sbert.net/

#### Title of the Article

Sentence-Transformers: Multilingual Sentence, Paragraph, and Image Embeddings

#### Summary of Report

- Reviewed the sentence-transformers library documentation to select an embedding model for the RAG system.
- Identified all-MiniLM-L6-v2 as the best-fit model for this project due to its balance of speed, embedding quality, and compatibility with free-tier deployment.
- Noted that this model runs entirely on CPU, which allows it to run free on Streamlit Community Cloud without requiring a GPU.

#### Relation to Project

- Supports the RAG system embedding layer, which converts project documents and user queries into vector representations.
- Ensures the RAG system can be deployed for free without paid embedding APIs.
- Provides high-quality semantic matching so stakeholder questions find relevant project evidence even when exact keywords are not used.

#### Motivation for Research

- Needed to select an embedding model compatible with free-tier deployment constraints.
- Needed a model that would work offline on project documents without internet access during retrieval.
- Needed a solution that kept the entire embedding pipeline under researcher control.

### Research

#### Link to Article

https://console.groq.com/docs/openai

#### Title of the Article

Groq API Documentation — OpenAI-Compatible Endpoints

#### Summary of Report

- Reviewed the Groq API documentation to confirm the free-tier model options and usage limits.
- Identified Llama 3.3 70B Versatile as the primary LLM for the RAG system due to its strong reasoning quality and generous free-tier throughput.
- Confirmed that Groq provides an OpenAI-compatible API, simplifying integration with the Streamlit application.

#### Relation to Project

- Supports the answer generation layer of the RAG system, which combines retrieved evidence with the user query to produce a cited, stakeholder-ready response.
- Keeps the system free-tier compatible for demonstrations at the September summit.
- Allows the system to be swapped to other LLMs (Google Gemini, OpenAI) without changing retrieval code.

#### Motivation for Research

- Needed a free-tier LLM that could generate high-quality answers using retrieved evidence.
- Needed to verify token limits and throughput to ensure the system handles stakeholder queries reliably.
- Needed to confirm API compatibility before writing the application layer.

### Work Completed

- Created src/ingest.py: reads all markdown documents from docs/ and reports/, splits them into overlapping chunks, embeds them with sentence-transformers, and saves a FAISS index to data/vector_store/.
- Created src/retrieval.py: loads the FAISS index at startup, embeds incoming queries, returns top-k chunks with metadata and relevance scores.
- Created app.py: Streamlit web application with question input, AI-generated answer with citations, and expandable source panels.
- Created requirements.txt with all dependencies pinned for Streamlit Community Cloud deployment.
- Created .streamlit/config.toml with dark theme and project branding.
- Ran src/ingest.py to build the initial FAISS index from Week 1 project documents.
- Confirmed the index was built successfully and retrieval works on test queries.
