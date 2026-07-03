# RAG Evaluation Question Set

Date: 2026-07-04
Version: 1.0

## Purpose

This document contains the stakeholder question test set for evaluating the Alberta Tourism Corridor RAG system. Questions will be used in Week 8 to score the system on faithfulness, citation quality, completeness, usefulness, and uncertainty handling.

The test set is organized into five categories matching the core project deliverables.

---

## Category 1: TDZ Alignment and Economic Potential

1. Which Tourism Development Zone has the highest estimated tourism spend growth potential?
2. Which TDZ has the highest annual visitor spend growth rate?
3. How many potential jobs are associated with the David Thompson TDZ?
4. What is the estimated tourism spend growth for the Canadian Badlands TDZ?
5. Which TDZ has the strongest resident support for increased visitation?
6. How does the Olds to Lacombe TDZ compare to the Foothills TDZ on economic potential?
7. What are the main tourism activity opportunities identified in the Cochrane to Sundre TDZ?
8. How many stakeholders were engaged in the Foothills TDZ discovery process?

---

## Category 2: Candidate Hub Recommendations

9. What are the five candidate tourism hubs identified for the Bow and Red Deer River corridors?
10. Which candidate hub scored the highest using the eight-criteria screening framework?
11. What is the preliminary score for the Red Deer River Badlands Hub?
12. What are the main transportation gaps identified for the Drumheller badlands hub?
13. Which hub is best positioned to serve as a Calgary visitor dispersal zone?
14. What data is still needed before finalizing the Rocky Mountain House hub recommendation?
15. Which hub has the strongest stakeholder readiness score and why?
16. What target visitor markets are identified for the Central Alberta Rural Experience Hub?

---

## Category 3: Transportation and Corridor Access

17. What are the main highway access routes for the Bow corridor hubs?
18. Which candidate hubs have the weakest corridor access scores?
19. What transportation improvements are most commonly needed across the five candidate hubs?
20. How does the absence of transit from Calgary affect the hub screening scores?
21. What role does Highway 11 play in the west-central adventure gateway hub?
22. Which hub is most dependent on a single road corridor for visitor access?

---

## Category 4: Tourism Baseline and Seasonality

23. What are the eight tourism indicator categories tracked by Travel Alberta?
24. What is the combined estimated tourism spend growth potential across all five priority TDZs?
25. Which city is the primary source market for most of the corridor hubs?
26. Why is seasonality a strategic problem for Central Alberta tourism?
27. What activities have the strongest potential to extend the shoulder season in corridor communities?
28. What is the role of the Royal Tyrrell Museum in the Red Deer River corridor strategy?

---

## Category 5: RAG System and Project Scope

29. What types of stakeholders is the RAG system designed to serve?
30. What is the difference between Tier 1 and Tier 5 source reliability in the corpus?
31. What does the RAG system do when it does not have enough evidence to answer a question?
32. What is the eight-week project timeline for the Alberta tourism corridor strategy?
33. What are the six main data gaps identified in the Week 2 tourism baseline research?
34. How does the hub screening framework connect to the RAG corpus?

---

## Scoring Rubric

Each answer will be scored on five dimensions, each rated 1 to 5:

| Dimension | What to Assess |
|---|---|
| Faithfulness | Does the answer use only retrieved evidence? Does it avoid unsupported claims? |
| Citation quality | Is at least one source cited? Is the citation specific and relevant? |
| Completeness | Does the answer address the full question? |
| Usefulness | Is the answer clear and actionable for a stakeholder? |
| Uncertainty handling | Does the system flag when evidence is missing or weak? |

**Minimum acceptable targets (from RAG system design document):**
- 90% of answers include at least one relevant citation
- 85% of answers avoid unsupported claims
- 80% of answers are useful without manual rewriting

---

## Notes on Test Administration

- Run all 34 questions against the corpus version active at the time of evaluation.
- Record the top source retrieved for each answer and whether it was the most relevant available chunk.
- Note any questions where the system confidently gave a wrong answer — these are the highest-priority failure cases.
- Compare Week 8 results against the initial test run completed after the Week 2 corpus build.
