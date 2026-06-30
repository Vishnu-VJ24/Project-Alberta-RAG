# Daily Research Log

## 2026-06-23

### Literature Reviewed

- Travel Alberta Research Hub
- Travel Alberta Tourism Development Zone Reports page
- Travel Alberta Tourism Indicators page
- Connecting Communities Foundation Integrated Transportation & Economic Corridor Summit page

### What We Learned

- Travel Alberta maintains a research hub with tourism indicators, market profiles, TDZ discovery reports, and Alberta visitor profiles.
- Travel Alberta identifies 10 Tourism Development Zones with high tourism growth and economic impact potential over a 10-year horizon.
- Relevant TDZs for the project likely include David Thompson, Olds to Lacombe, Cochrane/Sundre/Rocky Mountain House, Foothills, and Canadian Badlands. This needs confirmation after mapping the exact corridor geography.
- Tourism indicator categories include economic impact, employment, visitor spend, visitation, visitor characteristics, hotel performance, air access, air passengers, and market size.
- The Integrated Transportation & Economic Corridor Summit is scheduled for September 16, 2026 in Calgary and can serve as a stakeholder communication milestone.

### Problems Solved

- Converted the internship role description into a concrete 8-week research and RAG delivery plan.
- Defined a RAG system purpose, corpus schema, retrieval strategy, and evaluation plan.
- Created a project workspace structure for daily updates and literature tracking.

### Next Actions

- Download or collect the relevant TDZ discovery reports.
- Define exact study geography and municipalities along the Bow and Red Deer corridors.
- Create a source inventory with URLs, file paths, and priority.
- Decide whether the first RAG prototype should be Streamlit or FastAPI.

### Open Questions

- Which company or organization is sponsoring the project?
- Does your supervisor expect the RAG system to be a demo, deployed app, or research prototype?
- Are you allowed to use paid APIs such as OpenAI embeddings, or should we keep everything local/open-source?

## 2026-06-24

### Literature Reviewed

- Travel Alberta TDZ discovery page: David Thompson
- Travel Alberta TDZ discovery page: Olds to Lacombe
- Travel Alberta TDZ discovery page: Cochrane to Sundre
- Travel Alberta TDZ discovery page: Foothills

### What We Learned

- David Thompson, Olds to Lacombe, Cochrane to Sundre, and Foothills are all strong candidates for the Bow and Red Deer corridor analysis.
- The reviewed TDZ pages provide comparable indicators: potential job creation, annual visitor spend growth, estimated tourism spend growth, stakeholder/business/community engagement, resident support, and top activity opportunities.
- Foothills shows the largest listed estimated tourism spend growth among the reviewed TDZs.
- David Thompson shows the highest listed annual visitor spend growth among the reviewed TDZs.
- Olds to Lacombe appears important for Central Alberta rural tourism because of its business engagement and activity fit.
- Cochrane to Sundre appears important for Bow corridor access and Calgary-region visitor dispersal.

### Problems Solved

- Created a TDZ prioritization note that turns source review into a usable project analysis artifact.
- Added reviewed TDZ pages to the literature review matrix.
- Identified initial candidate hub themes for future geospatial and economic-impact analysis.

### Next Actions

- Review the Canadian Badlands TDZ page in detail for Red Deer River corridor relevance.
- Build a corridor geography table of municipalities, highways, tourism assets, airports, and TDZ relationships.
- Start a hub-screening model that scores candidate hubs by TDZ alignment, access, activity fit, and economic potential.

### Open Questions

- Which municipalities should be formally included in the study boundary?
- Should Calgary be treated as part of the corridor or as the main visitor source market?
- Should Edmonton be included as a secondary source market for Red Deer corridor tourism?

## 2026-06-25

### Literature Reviewed

- Travel Alberta TDZ discovery page: Canadian Badlands

### What We Learned

- Canadian Badlands is strongly relevant to the Red Deer River corridor because it connects river valley landscapes, paleontology, hiking, camping, and scenic touring.
- The TDZ page lists 1,340 potential jobs, 4.5% annual visitor spend growth, and $186M estimated tourism spend growth.
- Travel Alberta's Canadian Badlands page reports engagement with 173 stakeholders, 183 businesses, and 9 communities.
- Resident sentiment appears strong, with 83% saying they would welcome more visitors to their community.
- The top activity themes listed on the page are dinosaurs, hiking, and camping.

### Problems Solved

- Filled the main gap in the TDZ prioritization note by adding Canadian Badlands.
- Strengthened the Red Deer River corridor side of the project.
- Updated the literature review matrix with a dedicated Canadian Badlands entry.

### Next Actions

- Add Canadian Badlands to the candidate hub screening model.
- Identify municipalities and tourism assets connected to the Red Deer River and badlands area.
- Collect screenshots of the Canadian Badlands TDZ potential and opportunities sections.

### Open Questions

- Should Drumheller be treated as the anchor for the Red Deer River badlands hub?
- How far east should the Red Deer River corridor analysis extend?
- Which Indigenous, heritage, and paleontology partners should be included in the stakeholder scan?

## 2026-06-26

### Literature Reviewed

- Government of Alberta economic corridors page

### What We Learned

- Alberta frames economic corridors as links to markets in and out of the province that support economic, social, and environmental activity.
- This framing is useful for the tourism project because transportation improvements should be tied to visitor movement, market access, regional development, and stakeholder coordination.
- The project should connect tourism hub recommendations to transportation logic rather than treating hubs as isolated attractions.

### Problems Solved

- Created a recreation hub screening framework with criteria for TDZ alignment, corridor access, activity fit, economic potential, rural benefit, seasonality potential, stakeholder readiness, and RAG evidence strength.
- Connected Week 1 source review to a practical method for ranking candidate hubs.
- Defined preliminary hub themes for west-central adventure, Central Alberta rural experiences, Bow corridor foothills, and Red Deer River badlands tourism.

### Next Actions

- Build the first candidate hub table using the screening criteria.
- Start mapping candidate municipalities, highways, airports, river access points, parks, trails, and tourism assets.
- Begin collecting source documents for the first RAG ingestion test.

### Open Questions

- Should the first hub scoring model use equal weights or prioritize transportation access and economic potential?
- Should screenshots be embedded in the weekly report or stored as appendix evidence?
- Should the first RAG prototype use local open-source embeddings or a hosted API?

## 2026-06-29

### Literature Reviewed

- Candidate hub data synthesized from Week 1 TDZ review (David Thompson, Olds to Lacombe, Cochrane to Sundre, Foothills, Canadian Badlands)

### What We Learned

- The five candidate hubs score between 32 and 34 out of 40 using the unweighted screening framework, indicating all five are viable for deeper analysis.
- The three highest-scoring hubs are the Bow Corridor Foothills Hub, the Foothills Calgary Visitor Dispersal Hub, and the Red Deer River Badlands Hub, each scoring 34 out of 40.
- Transportation gaps appear across all five hubs. The most consistent gap is the absence of transit connections from Calgary or Edmonton to corridor recreation areas.
- Data gaps are significant in four areas: seasonal visitor counts by month, accommodation occupancy and capacity, origin-destination data for corridor travelers, and Indigenous tourism partnership inventories.
- The Foothills TDZ candidate has the largest economic potential by far ($468M estimated tourism spend growth, 3,381 potential jobs), making it the most important hub for economic impact framing.
- The Canadian Badlands hub has the strongest resident support (83%) and the most distinctive tourism product (paleontology and badlands landscapes), giving it strong differentiation potential.

### Problems Solved

- Converted the Week 1 hub themes and TDZ data into a structured, scored, five-hub candidate table.
- Identified specific data still needed for each hub, which will guide source collection in Weeks 3 and 4.
- Identified RAG source documents required for each hub, which will guide ingestion priorities.

### Next Actions

- Build the RAG system foundation so that research evidence can be queried by stakeholders.
- Start collecting additional source documents for hub analysis: municipal tourism plans, Parks Canada visitor data, Royal Tyrrell Museum data.
- Refine hub scores once weighted criteria are established after stakeholder priorities are clearer.

### Open Questions

- Should the three highest-scoring hubs (Foothills, Bow Foothills, Badlands) be the focus of the final report's hub chapter?
- Should the hub scoring model weight economic potential and transportation access more heavily than other criteria?
- How should Indigenous tourism partnerships be incorporated into the hub analysis?

## 2026-06-30

### Literature Reviewed

- Sentence-Transformers documentation (sbert.net): embedding model selection for the RAG system
- Groq API documentation: LLM model options, free-tier usage, and OpenAI-compatible endpoints

### What We Learned

- The all-MiniLM-L6-v2 sentence-transformer model is the best free-tier embedding option for this project. It runs on CPU, requires no API key, and produces high-quality semantic embeddings for retrieval tasks.
- The Groq API provides free-tier access to Llama 3.3 70B Versatile, which has strong reasoning quality and fast inference speeds. It is well-suited for the RAG answer-generation layer.
- FAISS with inner-product similarity (after L2 normalization) is sufficient for a corpus of this size. The index can be committed directly to the GitHub repo and loaded at app startup.
- Streamlit Community Cloud provides free hosting that connects directly to a GitHub repo and auto-deploys on push, making it the best free-tier deployment platform for the RAG demo.

### Problems Solved

- Built the full RAG pipeline: document ingestion → embedding → FAISS index → semantic retrieval → Groq LLM generation → Streamlit UI.
- Resolved the free-tier deployment question: Streamlit Community Cloud for hosting, sentence-transformers for embeddings, Groq for LLM, FAISS for vector store — all free.
- Built and tested the initial FAISS index from Week 1 project documents.

### Next Actions

- Deploy the Streamlit app to Streamlit Community Cloud.
- Add more source documents to the corpus (TDZ pages scraped as text, municipal tourism plans, additional research findings).
- Begin Week 2 tourism trend and baseline indicator analysis.
- Write a stakeholder question test set for evaluating RAG answer quality.

### Open Questions

- Should the Groq API key be stored in Streamlit secrets or as a GitHub Actions secret?
- How many test questions should the evaluation set include before the Week 8 formal evaluation?
- Should the app be password-protected for the demo or open access?
