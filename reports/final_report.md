# Central Alberta Tourism Corridor Strategy
### Internship Final Report

**Prepared by:** Vishnu  
**Period:** June 17 – July 13, 2026  
**Project:** Bow and Red Deer River Tourism Corridor Strategy  
**Live RAG App:** https://project-alberta-rag-wkw3tteb56qorgngped57g.streamlit.app/  
**GitHub:** https://github.com/Vishnu-VJ24/Project-Alberta-RAG

---

## Executive Summary

The research and analytical work produced twelve documents, a live AI-powered research assistant, and a strategic foundation covering TDZ alignment, hub scoring, geospatial asset mapping, infrastructure gap analysis, and transportation opportunity identification.

**Combined economic potential across five TDZs: $1.15 billion in estimated 10-year tourism spend growth and 8,351 potential jobs.**

The strongest near-term intervention is a seasonal rail shuttle from Red Deer County to Sylvan Lake using the existing CN right-of-way — confirmed viable by the project stakeholder. The highest-priority under-served zone is the Abraham Lake and Nordegg backcountry (David Thompson TDZ), which has world-class assets and critical infrastructure gaps. The Foothills TDZ has the highest economic potential ($468M) and is nearest to deployment-ready.

---

## 1. Tourism Development Zone Overview

| TDZ | 10-Year Spend Growth | Potential Jobs | Key Asset |
|---|---|---|---|
| Foothills | $468M | 3,381 | Bar U Ranch, Foothills scenery, Calgary proximity |
| David Thompson | $252M | 1,838 | Abraham Lake, Nordegg heritage, Hwy 11 corridor |
| Canadian Badlands | $186M | 1,340 | Royal Tyrrell Museum (450,000+ visitors/year) |
| Cochrane to Sundre | $147M | 1,073 | Raven River, Sundre Rodeo, foothills recreation |
| Olds to Lacombe | $98M | 719 | Sylvan Lake, agritourism, CN/CPKC rail corridor |
| **Total** | **$1,151M** | **8,351** | |

---

## 2. Candidate Hub Analysis

Hubs were scored 0–40 across eight criteria: TDZ alignment, economic potential, corridor access, accommodation capacity, tourism asset density, seasonality potential, stakeholder readiness, and RAG evidence strength.

| Hub | Score | Primary Strength | Primary Gap |
|---|---|---|---|
| Foothills Calgary Dispersal (Okotoks–Nanton) | 34/40 | Highest economic TDZ; 80km from 1.4M Calgary market | No transit from Calgary; US cross-border market untapped |
| Bow Corridor Foothills (Cochrane–Sundre) | 34/40 | Outdoor recreation density; Hwy 22 scenic corridor | No transit; Hwy 22 bottleneck; limited accommodation |
| Red Deer River Badlands (Drumheller) | 34/40 | Royal Tyrrell is Canada's top palaeontology draw | All 450K+ visitors arrive by car; rail tracks removed |
| West-Central Adventure Gateway (Rocky Mtn House) | 29/40 | Highest gap-to-potential ratio; Abraham Lake is world-class | Single highway access; no transit; no backcountry accommodation |
| Central Alberta Rural Experience (Sylvan Lake) | 26/40 | Only zone with active freight rail (CN + CPKC) | Rail opportunity untapped; agritourism unpackaged |

### Hub Priority Order
1. **Foothills** — strongest economics, closest to ready
2. **Drumheller** — massive anchor asset; invest in dispersal, not attraction
3. **Cochrane-Sundre** — strong outdoor product; needs transit and accommodation
4. **David Thompson** — world-class assets; urgent infrastructure case
5. **Central Alberta / Sylvan Lake** — rail opportunity is the unlock

---

## 3. RAG Research Assistant

An AI-powered research tool was built and deployed for stakeholder use. Any question about the corridor strategy can be queried and will receive a cited answer drawn from the project corpus.

| Component | Detail |
|---|---|
| **Live URL** | https://project-alberta-rag-wkw3tteb56qorgngped57g.streamlit.app/ |
| **LLM** | Groq API — Llama 3.3 70B (free tier) |
| **Embeddings** | all-MiniLM-L6-v2, FAISS vector index |
| **Corpus** | 156 chunks · 21 project documents |
| **Hosting** | Streamlit Community Cloud (free, auto-redeploys on GitHub push) |
| **Cost** | $0 — all components are on free tiers |

**To add new documents:** Drop `.md` files into `docs/` or `reports/`, run `python src/ingest.py`, commit `data/vector_store/`, push to GitHub. Live within 2 minutes.

**To update the Groq API key:** Streamlit Cloud dashboard → app settings → Secrets → update `GROQ_API_KEY`.

A 34-question evaluation test set is in `docs/rag_evaluation_questions.md`. Minimum targets: 90% of answers cite a source; 85% avoid unsupported claims; 80% are usable without rewriting.

---

## 4. Tourism Baseline — Key Indicators

| Indicator | Finding |
|---|---|
| Primary source market | Calgary (1.4M), secondary Edmonton (1.1M) |
| International gateway | Calgary International (YYC) — only major air entry point |
| Seasonality | Near-total summer dependence; June–August window in all rural zones |
| Visitor spend pattern | Day-trip dominated — accommodation ceiling prevents overnight conversion |
| US drive market | Substantial volume on Hwy 2 from Montana; zero targeted corridor marketing |
| Accommodation stock | Strongest in Red Deer and Drumheller; critical gaps at Nordegg and backcountry sites |

**Key data still needed:** Seasonal visitor counts by month (Statistics Canada TSRC); Sylvan Lake peak-day visitor count (Lacombe County); accommodation occupancy by community (Travel Alberta).

---

## 5. Corridor Geography — Five Zones

| Zone | Communities | Highway Spine | Rail | Gap Rating |
|---|---|---|---|---|
| Bow Corridor West | Cochrane, Sundre, Cremona, Water Valley | Hwy 22, Hwy 1A | None | High |
| Central Alberta | Olds, Innisfail, Red Deer, Lacombe, Sylvan Lake | Hwy 2 (QEII) | CN + CPKC (freight) | Moderate |
| West-Central | Rocky Mountain House, Nordegg, Caroline | Hwy 11 | None | **Critical** |
| Foothills / Bow South | Okotoks, High River, Black Diamond, Nanton | Hwy 2, Hwy 22, Hwy 7 | CPKC (freight) | High |
| Red Deer River East | Drumheller, East Coulee, Morrin, Rosedale | Hwy 9 | None (tracks removed) | **Critical** |

**Critical finding:** Central Alberta is the only zone with active rail. Every other zone — including Drumheller — has no rail infrastructure.

---

## 6. Sylvan Lake Rail Opportunity

> **Stakeholder input (Vern, July 6 2026):** Drumheller rail is not viable — tracks removed. Sylvan Lake on the CN right-of-way is the strongest near-term rail opportunity in the corridor.

**The case:** Sylvan Lake charges $50/day to park in summer — a direct congestion signal. Active CN/CPKC freight lines already run through Red Deer and Lacombe County. No new track required.

| Scenario | Daily Visitors | Conversion | Daily Riders | Daily Revenue |
|---|---|---|---|---|
| Conservative | 5,000 | 10% | 500 | $10,000 |
| Base | 5,000 | 20% | 1,000 | $20,000 |
| High | 8,000 | 20% | 1,600 | $32,000 |

*Fare model: $10 one-way from Red Deer County vs $50/day parking.*

**Data still needed:** Actual Sylvan Lake peak-day visitor count (contact: Lacombe County Planning, or Alberta Parks visitor use statistics).

---

## 7. Asset Gap Analysis

### Four Structural Gaps — Corridor-Wide

| Gap | What It Means |
|---|---|
| **Transit desert** | Every zone — 100% of visitors arrive by personal vehicle |
| **Spend concentration** | Visitor dollars concentrate at anchor assets (Tyrrell, Sylvan Lake, Abraham Lake); surrounding communities receive minimal benefit |
| **Accommodation ceiling** | 3 of 5 zones cannot convert day visitors to overnight guests — insufficient supply |
| **Marketing disconnection** | No zone has its assets connected into a bookable consumer itinerary |

### Investment Priority by Gap Type

| Priority | Gap | Action |
|---|---|---|
| 1 | Transit | Sylvan Lake rail shuttle; David Thompson seasonal shuttle |
| 2 | Accommodation | Glamping/cabin development at Nordegg and Drumheller |
| 3 | Spend dispersal | Circuit packaging and joint ticketing across assets |
| 4 | Last-mile | Abraham Lake visitor node; Drumheller valley loop wayfinding |
| 5 | Marketing | Hwy 2A heritage route; foothills cultural circuit |

---

## 8. Under-Served Zone Profiles

| Priority | Zone | Why Under-Served | Key Intervention |
|---|---|---|---|
| 1 | Abraham Lake and Nordegg (David Thompson) | World-class assets; no transit, no visitor facilities, no accommodation near Abraham Lake | Visitor node at Abraham Lake; seasonal shuttle from Rocky Mtn House; 2-day circuit package |
| 2 | Drumheller valley communities (East Coulee, Morrin, Rosedale) | 450K Tyrrell visitors do not disperse into valley communities | Valley loop wayfinding on Hwy 10; joint ticketing with Tyrrell; shuttle pilot |
| 3 | Highway 2A heritage corridor (Olds to Lacombe) | Tens of thousands of QEII bypass vehicles per week; no corridor brand or wayfinding | "Historic Heartland Route" signage at QEII on-ramps; self-guided driving itinerary |
| 4 | High River, Black Diamond, Turner Valley triangle | Strong foothills culture assets within 80km of Calgary; no transit, US market untapped | Foothills cultural circuit; US cross-border wayfinding on Hwy 2 |
| 5 | Sundre and upper Red Deer headwaters | Alberta's best brown trout fishery + Sundre Rodeo; no wayfinding, no trailhead shuttle | Hwy 22 wayfinding; Sundre outdoor adventure package |

---

## 9. Strategic Recommendations

### Transportation
- **Sylvan Lake CN rail shuttle** — highest priority; existing infrastructure, real demand signal, concrete economic model
- **David Thompson backcountry shuttle** — seasonal service from Rocky Mtn House to Abraham Lake and Nordegg
- **Drumheller valley loop shuttle** — weekend summer shuttle connecting Tyrrell, Atlas Coal Mine, East Coulee, Rosebud
- **Highway 2A heritage route** — lowest-cost intervention; branding and QEII on-ramp signage only

### Hub Development
- **Foothills first** — strongest economics, nearest to deployment-ready; prioritize Calgary transit link
- **Drumheller** — invest in dispersal from Tyrrell into valley, not new attractions
- **David Thompson** — Abraham Lake visitor node is the single highest-impact infrastructure investment
- **Sylvan Lake** — advance CN/CPKC engagement; collect real visitor count data before summit

### Marketing
- Position Hwy 2A as a distinct "Historic Heartland Route" corridor product
- Create a foothills cultural circuit: Bar U Ranch → Turner Valley → Leighton Art Centre → Nanton
- Target US cross-border drive visitors on Hwy 2 explicitly — currently zero dedicated marketing
- Connect the Royal Tyrrell Museum to the broader badlands valley circuit with joint programming

---

## 10. Deliverable Summary

| Week | Day | Deliverable |
|---|---|---|
| **Week 1** | Mon–Fri | TDZ research; hub screening framework; RAG system design; literature review; data inventory |
| **Week 2** | Mon | Candidate hub table — 5 hubs scored |
| | Tue | RAG system built — ingest pipeline, FAISS index, Streamlit app |
| | Wed | RAG system deployed live on Streamlit Cloud |
| | Thu | Tourism baseline profile — 8 indicator categories |
| | Fri | RAG evaluation framework — 34-question test set |
| **Week 3** | Mon | Corridor geography table — 5 zones mapped |
| | Tue | Sylvan Lake rail transportation analysis |
| | Wed | Asset gap analysis — 5 zones, 4 structural patterns |
| | Thu | Under-served zone profiles — 5 priority zones |
| | Fri | Corridor synthesis — strategic narrative |

---

## 11. What Was Not Completed

| Week | Planned Work |
|---|---|
| Week 4 | Transportation needs assessment; Sylvan Lake visitor data collection; shuttle case studies |
| Week 5 | Hub economic impact model; final hub scoring |
| Week 6 | Marketing and branding strategy; visitor personas |
| Week 7 | Integrated final report draft |
| Week 8 | Formal RAG evaluation; September summit presentation materials |

---

## 12. Handover Notes

**Most urgent next action:** Collect actual Sylvan Lake annual and peak-day visitor count from Lacombe County Planning and Development, or Alberta Parks. This is the linchpin number for the transportation chapter.

**Top five next actions for the successor:**

1. Get Sylvan Lake visitor data — call Lacombe County directly
2. Expand RAG corpus — scrape Travel Alberta TDZ pages as text files, add to `docs/`, re-run ingest
3. Run the 34-question RAG evaluation in `docs/rag_evaluation_questions.md` and identify corpus gaps
4. Complete the transportation improvement plan — Sylvan Lake analysis is the foundation
5. Research comparable Canadian tourist rail/shuttle case studies for benchmarking the conversion model

**Project files:** All in GitHub repo. The `docs/` folder contains all analysis; `reports/` contains weekly reports, this final report, and the screenshot log. The RAG system code is in `src/`.

---

*All analytical documents, the RAG system codebase, and the research corpus are committed to GitHub and remain live and accessible. The RAG application auto-redeploys on every GitHub push at no cost.*
