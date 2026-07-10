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

## 2026-07-02

### Literature Reviewed

- Streamlit Community Cloud deployment documentation

### What We Learned

- Streamlit Community Cloud supports free hosting for public GitHub repositories and auto-redeploys on every push to main. This means every new document added to the corpus and every code update goes live automatically without any manual redeploy step.
- The Groq API free tier provides 500,000 tokens per day with no credit card required. At approximately 1,500 tokens per RAG query, the system can handle over 300 queries per day before hitting the limit, which is well above the expected load for a research demonstration.
- Initial stakeholder testing confirmed that the RAG system retrieves relevant context and generates cited answers correctly. The system correctly answered questions about TDZ activities and transportation gaps.
- The live application URL is: https://project-alberta-rag-wkw3tteb56qorgngped57g.streamlit.app/

### Problems Solved

- Deployed the RAG application publicly for the first time.
- Resolved the Groq API key configuration by adding it through Streamlit's secrets management interface after the initial deployment.
- Confirmed that the free-tier deployment architecture is viable for the full project duration.

### Next Actions

- Expand the RAG corpus with dedicated source documents for each TDZ to improve answer precision.
- Research and compile Alberta tourism baseline indicators for the economic analysis chapter.
- Build a stakeholder question test set to evaluate RAG answer quality in Week 8.

### Open Questions

- Should the app URL be shared with the project partner and supervisor this week?
- Should the corpus expansion prioritize TDZ documents or provincial baseline data first?

## 2026-07-03

### Literature Reviewed

- Travel Alberta Tourism Indicators: https://industry.travelalberta.com/research/tourism-indicators
- Travel Alberta Tourism Development Zone Reports overview: https://industry.travelalberta.com/research/tourism-development-zone-reports

### What We Learned

- Alberta tourism employment is highly seasonal, with most rural jobs concentrated in June through August. The shoulder-season gap in Central Alberta is larger than in mountain or urban destinations because rural areas lack winter and off-season product offerings.
- The combined estimated tourism spend growth potential for the five priority TDZs is $1,151M over a 10-year horizon. The Foothills TDZ alone accounts for $468M of that total.
- Calgary is the primary domestic source market for four of the five candidate hubs. Edmonton is a secondary source for the David Thompson and Olds-Lacombe hubs.
- Rural accommodation capacity along the corridor is a binding constraint on overnight visitor spend. Expanding or connecting existing accommodation to marketing networks is a consistent theme across TDZ stakeholder feedback.
- The Royal Tyrrell Museum is a recognized international paleontology destination and is likely the strongest single demand anchor in the corridor for attracting long-haul and international visitors.

### Problems Solved

- Created a structured tourism baseline document covering all eight indicator categories: economic impact, employment, visitor spend, visitation trends, seasonality, hotel performance, air access, and market size.
- Identified the six most important data gaps remaining in the baseline: seasonal visitor counts, accommodation occupancy by community, origin-destination data for corridor highways, overnight visitor proportions, Indigenous tourism operator inventory, and Royal Tyrrell Museum annual visitation figures.

### Next Actions

- Add the tourism baseline document to the RAG corpus and rebuild the FAISS index.
- Begin collecting the data gap items identified today, starting with Statistics Canada travel survey data.
- Start building the corridor geography table mapping municipalities, highways, rivers, parks, and tourism assets.

### Open Questions

- Should the economic impact model use TDZ-level spend growth figures as the primary input, or should it be anchored to Statistics Canada visitor spend data?
- Which data gap should be prioritized for collection in Week 3: seasonal counts, accommodation capacity, or origin-destination data?

## 2026-07-04

### Literature Reviewed

- RAGAS evaluation framework documentation: https://docs.ragas.io/en/stable/

### What We Learned

- RAGAS is a framework for evaluating RAG systems on faithfulness, answer relevance, context precision, and context recall. For this project, a manual evaluation approach is more appropriate than an automated RAGAS pipeline given the small corpus and domain-specific questions.
- Faithfulness and citation quality are the two most critical metrics for this project. Every claim in the final report and summit presentation needs to be traceable to a specific source document.
- A 34-question test set across five categories gives a representative sample of the stakeholder questions the system is expected to handle.

### Problems Solved

- Built the RAG evaluation question set with 34 questions and a five-dimension scoring rubric.
- Defined minimum acceptable targets for the Week 8 formal evaluation.
- Closed out Week 2 with all deliverables committed and pushed to GitHub.
- Shared the live RAG application with the project partner.

### Week 2 Deliverables Completed

1. Candidate hub table — five hubs fully scored
2. RAG system — built, indexed, and deployed live
3. Tourism baseline profile — eight indicator categories
4. RAG evaluation framework — 34-question test set and scoring rubric

### Next Actions (Week 3)

- Build corridor geography table: municipalities, highways, rivers, parks, airports for each hub area.
- Expand RAG corpus with dedicated TDZ text documents scraped from Travel Alberta pages.
- Begin geospatial asset and gap analysis.
- Start collecting Statistics Canada travel survey data.

### Open Questions

- Should the corridor geography table be built as one document or split by hub?
- Should Week 3 start with corpus expansion or corridor geography mapping first?

## 2026-07-07

### Literature Reviewed

- Alberta Parks: Sylvan Lake Provincial Park page
- CN Railway network overview

### What We Learned

- Central Alberta is the only corridor zone with active freight rail infrastructure — CN runs through Red Deer and Lacombe County, CPKC runs near Ponoka. All other corridor zones have no active rail.
- Drumheller rail is confirmed not viable by the project stakeholder: tracks no longer exist. Transportation recommendations for that hub must focus on road-based improvements.
- Sylvan Lake is experiencing real summer congestion — the $50/day parking charge is a direct market signal that demand exceeds current access capacity. This is the strongest near-term case for a rail-linked tourism intervention in the entire corridor.
- The five corridor zones differ significantly in their transportation infrastructure. Only the Central Alberta zone has the rail right-of-way needed for a passenger or tourist shuttle service.

### Problems Solved

- Built the corridor geography table across five zones, providing the first structured geospatial reference for the project.
- Incorporated stakeholder feedback from the July 6 meeting into the project analysis.
- Resolved the Drumheller vs Sylvan Lake rail question in favour of Sylvan Lake based on infrastructure reality.

### Next Actions

- Build the Sylvan Lake visitor conversion economic model.
- Identify geospatial tourism asset gaps using the corridor geography table.
- Begin under-served zone analysis.

### Open Questions

- What is the actual annual visitor count for Sylvan Lake? This is needed to run the conversion model with real numbers.
- Should the Sylvan Lake rail proposal be positioned as a pilot for the September summit, or as a longer-term recommendation?

## 2026-07-08

### Literature Reviewed

- CPKC network documentation
- Government of Alberta Economic Corridors (revisited for transportation policy framing)

### What We Learned

- CPKC lines supplement CN in the Central Alberta corridor zone, providing additional right-of-way options for a Sylvan Lake rail service. Both operators would need to be engaged for any passenger rail activation.
- The provincial economic corridors framework explicitly supports transportation links that enable economic and social activity — this framing strengthens the policy case for a Sylvan Lake rail shuttle.
- The Integrated Transportation and Economic Corridor Summit in September 2026 is a direct communication opportunity. A Sylvan Lake rail proposal aligned with CN/CPKC right-of-way is a concrete, costed transportation recommendation that fits the summit's agenda.
- The illustrative visitor conversion model shows daily rail revenue potential of $10,000 to $32,000 depending on volume and conversion rate assumptions. Actual figures require real visitor count data.

### Problems Solved

- Built a full transportation opportunity analysis for the Sylvan Lake CN right-of-way route.
- Developed a replicable visitor conversion framework that can be applied to other potential rail or shuttle opportunities in the corridor.
- Updated the project hub structure to include Sylvan Lake as a rail-linked node within the Central Alberta hub.

### Next Actions

- Collect actual Sylvan Lake visitor data from Lacombe County or Alberta Parks.
- Begin the geospatial asset gap analysis using the corridor geography table.
- Expand the RAG corpus with the new corridor geography and Sylvan Lake documents.
- Rebuild the FAISS index and push the updated knowledge base.

### Open Questions

- Should the conversion rate assumption be validated against comparable rail shuttle case studies from other Canadian provinces?
- Should the Sylvan Lake analysis be presented to the summit as a standalone case study or embedded in the broader transportation improvement plan?

## 2026-07-09

### Literature Reviewed

- Statistics Canada Travel Survey of Residents of Canada (TSRC) methodology

### What We Learned

- The TSRC distinguishes between same-day visits and overnight stays — this is the critical split for assessing whether corridor zones are capturing day-trip visitors, overnight visitors, or neither. Most under-served zones in this corridor are capturing day trips but losing the overnight visit and its associated spend.
- The four structural gap patterns in the corridor — transit desert, visitor spend concentration, accommodation ceiling, and marketing disconnection — are not unique to this region. They are the same patterns that characterize under-developed rural tourism zones nationally.
- The David Thompson zone (Abraham Lake, Nordegg) has the highest gap-to-potential ratio of any zone. Exceptional assets, almost no supporting infrastructure. This is the most urgent investment case in the project area.
- Zones 3 and 5 (David Thompson and Drumheller) were both rated Critical. Zones 1 and 4 (Cochrane-Sundre and Foothills) rated High. Zone 2 (Central Alberta) rated Moderate — it has the best infrastructure of any corridor zone.

### Problems Solved

- Built the asset gap analysis across all five zones with structured gap ratings.
- Identified four cross-corridor structural gaps that apply project-wide rather than zone-specific.
- Confirmed investment priority order by zone for the transportation and hub recommendation sections.

### Next Actions

- Build under-served zone profiles with specific recommended interventions per zone.
- Identify which data gaps are most critical to fill before Week 5 hub refinement.
- Rebuild FAISS index with new analysis documents.

### Open Questions

- Should the TSRC data be used to establish a quantitative overnight conversion rate benchmark for each zone?
- Is the accommodation gap in Zone 3 the binding constraint or is access the more urgent priority?

## 2026-07-10

### Literature Reviewed

- Government of Alberta Tourism Development in Alberta framework

### What We Learned

- The province explicitly recognizes visitor spend dispersal from urban to rural communities as a core tourism development objective. The project's under-served zone work directly aligns with this provincial priority.
- Heritage corridor and scenic route development is a recognized provincial tool for rural dispersal — the Highway 2A heritage corridor opportunity identified today is well-supported by existing policy frameworks.
- The Integrated Transportation and Economic Corridor Summit in September is the right venue for presenting both the under-served zone findings and the Sylvan Lake rail proposal. Both fit squarely within the summit's mandate.
- The five under-served zones identified today collectively represent the strongest case for the project's dispersal strategy. They show that the problem is not a lack of assets — it is a lack of infrastructure and marketing to connect those assets to visitors.

### Problems Solved

- Completed the under-served zone analysis with five priority zones, four-criterion framework, gap evidence, and concrete recommended interventions for each.
- Confirmed Abraham Lake and Nordegg backcountry as Priority 1 under-served zone.
- Identified the Highway 2A heritage corridor as the lowest-cost, highest-impact new corridor product opportunity.
- Completed Week 3 analytical deliverables: corridor geography table, Sylvan Lake rail analysis, asset gap analysis, and under-served zone profiles — four documents covering the full geospatial scope of the project.

### Next Actions

- Do the Week 3 Friday close-out.
- Rebuild FAISS index and push all new documents to GitHub.
- Prepare for Week 4 transportation needs assessment.

### Open Questions

- Should the Hwy 2A heritage corridor recommendation be fast-tracked as a near-term win given its low infrastructure cost?
- How should the under-served zone findings be presented in the final report — as a standalone chapter or integrated into the hub recommendations chapter?

## 2026-07-11

### Literature Reviewed

- Transport Canada Gateway and Corridor Programs documentation

### What We Learned

- Transport Canada supports multimodal corridor development integrating passenger and freight, which aligns with the CN and CPKC right-of-way activation concept for the Sylvan Lake rail opportunity.
- Federal corridor programs typically require provincial and municipal co-investment — this means the Sylvan Lake proposal needs to be framed as a multi-order-of-government initiative at the September summit, not just a provincial or local project.
- The five key strategic insights from Week 3 are: infrastructure quality does not match asset quality in four of five zones; four structural gaps apply corridor-wide; the Sylvan Lake rail opportunity is the most actionable near-term intervention; the David Thompson zone has the highest gap-to-potential ratio; and the Hwy 2A heritage corridor is the lowest-cost new product opportunity.

### Problems Solved

- Synthesized four Week 3 deliverables into a coherent strategic narrative in docs/week3_corridor_synthesis.md.
- Identified five priority decisions for the Week 4 transportation assessment: Sylvan Lake ridership data, David Thompson shuttle feasibility, Drumheller road improvements, Hwy 2A corridor branding precedents, and CN vs CPKC engagement strategy.
- Closed out Week 3 with all five deliverables committed and pushed to GitHub.
- Confirmed the RAG corpus at 121 chunks across 19 project documents — updated and live on Streamlit.

### Week 3 Deliverables Completed

1. Corridor geography table — five zones fully mapped
2. Sylvan Lake rail transportation analysis — economic model complete
3. Asset gap analysis — five zones rated, four structural patterns identified
4. Under-served zone profiles — five zones with interventions
5. Corridor synthesis — strategic cross-cutting narrative

### Next Actions (Week 4)

- Transportation needs assessment: formal analysis of each corridor zone's transportation improvement priorities
- Collect Sylvan Lake actual visitor count data
- Research comparable rural shuttle and tourist rail case studies from other Canadian provinces
- Start drafting the transportation improvement plan chapter for the final report

### Open Questions

- Should the Week 4 transportation assessment start with the Sylvan Lake rail case study or the corridor-wide transit gap analysis?
- Is there a comparable tourist rail shuttle operating on CN or CPKC right-of-way anywhere in Canada that can serve as a benchmark?





