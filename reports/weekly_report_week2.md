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

---

## Wednesday, July 2, 2026

**Work Title:** RAG System Deployment and Stakeholder Testing
**Time Reported:** 4 hours
**Work Type:** Technical deployment and system validation

### Work Description

Deployed the Alberta Tourism Corridor RAG system to Streamlit Community Cloud and conducted initial stakeholder question testing. The work focused on connecting the GitHub repository to the hosting platform, configuring the Groq API key through Streamlit's secrets management, verifying end-to-end answer generation, and documenting the live application URL for project reporting and stakeholder communication.

### Research

#### Link to Article

https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app

#### Title of the Article

Streamlit Community Cloud — Deploy Your App

#### Summary of Report

- Reviewed the Streamlit Community Cloud deployment documentation to connect the GitHub repository and configure the live application.
- Confirmed that Streamlit Community Cloud supports free hosting for public GitHub repositories with automatic redeployment on every push to the main branch.
- Identified the secrets management interface as the correct method for storing the Groq API key without exposing it in the repository.

#### Relation to Project

- Enables the RAG system to be accessed by stakeholders, project partners, and summit attendees through a public URL without any local setup.
- Supports the project's showcase and summit communication objectives by providing a shareable, always-available research assistant.
- Confirms the free-tier deployment architecture is viable for the full project duration.

#### Motivation for Research

- Needed to understand the deployment process before connecting the repository to the hosting platform.
- Needed to confirm that the Groq API key could be stored securely without being committed to the GitHub repository.
- Needed to verify that automatic redeployment would work correctly as new documents are added to the corpus in later weeks.

### Work Completed

- Connected the GitHub repository to Streamlit Community Cloud and deployed the app from the main branch using app.py as the entry point.
- Configured the Groq API key through the Streamlit secrets management interface after initial deployment.
- Confirmed the application is live and publicly accessible at:
  **https://project-alberta-rag-wkw3tteb56qorgngped57g.streamlit.app/**
- Tested the live application with three stakeholder questions:
  - "Which TDZ has the highest economic potential?"
  - "What transportation gaps exist across the candidate hubs?"
  - "What activities are recommended for the Drumheller badlands hub?"
- Confirmed that the system retrieves source chunks, generates cited answers, and displays source document metadata correctly.
- Noted that expanding the corpus with dedicated per-TDZ source documents will improve answer precision in future updates.
- Verified that the Groq free tier (500,000 tokens per day, no credit card required) is sufficient for research and demonstration use throughout the project.

---

## Thursday, July 3, 2026

**Work Title:** Alberta Tourism Baseline Profile and Indicator Research
**Time Reported:** 4 hours
**Work Type:** Research analysis and data collection

### Work Description

Researched and compiled a tourism baseline profile for Central Alberta covering key indicators from Travel Alberta's public research hub. The work focused on identifying visitor spend trends, seasonality patterns, hotel performance, employment figures, air access data, and market size estimates that will anchor the economic analysis chapters of the final report. The compiled baseline was added to the project knowledge base as a new corpus document.

### Research

#### Link to Article

https://industry.travelalberta.com/research/tourism-indicators

#### Title of the Article

Travel Alberta Tourism Indicators

#### Summary of Report

- Reviewed Travel Alberta's tourism indicators portal, which tracks economic impact, employment, visitor spend, visitation trends, visitor characteristics, hotel performance, air access, air passengers, and market size across Alberta.
- Identified that Alberta's tourism sector contributes significantly to provincial GDP and that Central Alberta sits between the two highest-volume tourism corridors in the province — the Calgary–Banff corridor and the Edmonton corridor.
- Noted that visitor spend data is broken down by domestic and international origin, and that seasonality compression is a documented challenge across rural Alberta destinations.

#### Relation to Project

- Provides the quantitative baseline needed to support economic impact estimates for each candidate hub.
- Informs the seasonality analysis that will be used to score hubs on their ability to extend visits into spring and fall.
- Supplies context for comparing corridor-level tourism performance against provincial averages.

#### Motivation for Research

- Needed to establish a baseline tourism profile before building the economic impact model in Week 6.
- Needed indicator categories that could be linked to TDZ data already in the project to create a coherent analytical chain.
- Needed source material that could be added to the RAG corpus so stakeholders can query provincial tourism context alongside corridor-specific evidence.

### Research

#### Link to Article

https://industry.travelalberta.com/research/tourism-development-zone-reports

#### Title of the Article

Travel Alberta Tourism Development Zone Reports — Overview

#### Summary of Report

- Reviewed the TDZ reports overview page to confirm the structure and comparability of TDZ-level tourism data across the five priority zones.
- Confirmed that all TDZ pages use consistent indicator categories including potential jobs, annual visitor spend growth percentage, and estimated total tourism spend growth, allowing direct cross-zone comparison.
- Noted that TDZ data reflects a 10-year planning horizon, which aligns with the project's strategic rather than short-term framing.

#### Relation to Project

- Supports the cross-TDZ comparison in the hub scoring table by confirming data consistency across zones.
- Provides the analytical foundation for presenting relative economic potential between the five candidate hubs.
- Confirms that TDZ-level data can be used directly in the RAG corpus to answer stakeholder questions about specific zones.

#### Motivation for Research

- Needed to confirm that the five TDZ pages use consistent data structures before building comparative analysis.
- Needed to understand the 10-year planning horizon so economic potential figures are framed correctly in the final report.
- Needed to prepare the source inventory for the corpus expansion planned for the following week.

### Work Completed

- Created docs/tourism_baseline.md with a structured summary of Central Alberta tourism indicators covering economic impact, visitor spend trends, seasonality, hotel performance, employment, air access, and market size context.
- Added the tourism baseline document to the project knowledge base and rebuilt the FAISS index to include the new source.
- Updated the literature review matrix with the Travel Alberta Tourism Indicators source.
- Identified key data gaps where Statistics Canada travel survey data and regional accommodation occupancy figures are still needed.
