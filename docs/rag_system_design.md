# RAG System Design

## Purpose

The RAG system should answer stakeholder questions about the tourism corridor strategy using traceable evidence from reports, datasets, maps, and project notes.

Example users:

- Municipal economic development staff
- Tourism operators
- Transportation agencies
- Airport and rail project teams
- Conference attendees
- Company executives reviewing investment opportunities
- Researchers writing the final report

## Core User Questions

- Which areas in Central Alberta are under-served by tourism infrastructure?
- What evidence supports a specific adventure hub recommendation?
- How do proposed hubs align with Alberta Tourism Development Zones?
- What transportation improvements would most affect visitor access?
- What are the economic impact assumptions behind each scenario?
- Which sources support the final report's claims?
- What are the risks, constraints, and open uncertainties?

## Corpus Design

Each ingested item should be stored with structured metadata:

- `source_id`
- `title`
- `publisher`
- `publication_date`
- `url_or_file_path`
- `source_type`
- `geography`
- `topic_tags`
- `reliability_tier`
- `citation`
- `chunk_id`
- `chunk_text`

Suggested source types:

- strategy_report
- government_dataset
- tourism_dashboard
- academic_paper
- municipal_plan
- transport_plan
- geospatial_layer
- project_note
- economic_model_output

Reliability tiers:

- Tier 1: official government/statistical source
- Tier 2: official tourism or municipal partner source
- Tier 3: peer-reviewed or academic source
- Tier 4: industry report or credible news
- Tier 5: internal notes requiring verification

## Retrieval Strategy

Use hybrid retrieval:

- Keyword search for exact place names, program names, highways, TDZ names, and policy terms.
- Vector search for broader semantic questions.
- Metadata filters for geography, source type, publication date, and reliability tier.

Recommended answer policy:

- Always cite sources.
- Separate evidence from inference.
- Prefer official and recent sources when answering strategy or data questions.
- Say when the corpus does not contain enough evidence.
- Do not fabricate statistics, budgets, or economic multipliers.

## Technical Architecture

Initial local prototype:

- Python
- FastAPI or Streamlit
- LlamaIndex or LangChain
- Chroma or FAISS vector store
- Sentence-transformer or OpenAI embeddings
- PDF/HTML/CSV ingestion pipeline
- Markdown daily notes as ingestible project memory

Recommended folders:

- `data/raw`
- `data/processed`
- `data/vector_store`
- `notebooks`
- `src/ingestion`
- `src/retrieval`
- `src/app`
- `reports`

## Evaluation Plan

Create a test set of 30-50 stakeholder questions. Score each answer on:

- Faithfulness: answer only uses retrieved evidence.
- Citation quality: sources are specific and relevant.
- Completeness: answers the full question.
- Usefulness: gives a stakeholder-ready response.
- Uncertainty handling: flags missing or weak evidence.

Minimum acceptable prototype target:

- 90% of answers include at least one relevant citation.
- 85% of answers avoid unsupported claims.
- 80% of answers are useful without manual rewriting.

## RAG Deliverables

- Working local demo
- Ingested source library
- Stakeholder question set
- RAG evaluation summary
- Methodology section for the final paper
- Appendix listing corpus sources and limitations

