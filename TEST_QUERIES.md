# Synthetic Pharma Strategy Queries

Here are 10 strategic queries designed to test the Agentic AI system across various pharmaceutical planning use cases.

## 1. Repurposing Opportunities
**Query:** "Identify repurposing opportunities for Metformin in pediatric non-alcoholic fatty liver disease (NAFLD) considering recent Phase 2 data."
*   **Focus:** Clinical evidence, patent feasibility, pediatric safety.

**Query:** "Evaluate the potential of SGLT2 inhibitors for heart failure with preserved ejection fraction (HFpEF) in non-diabetic patients."
*   **Focus:** Cross-indication efficacy, market expansion potential.

## 2. Market Gap Analysis
**Query:** "Which respiratory diseases show low competition but high patient burden in India?"
*   **Focus:** Epidemiology vs. competitor density (Blue Ocean strategy).

**Query:** "Identify underserved rare genetic disorders in the EU market with no approved therapies."
*   **Focus:** Orphan drug designation potential, unmet need.

## 3. Patent Expiry & FTO
**Query:** "List top-selling biologics losing patent exclusivity in the US within the next 3 years and assess biosimilar entry barriers."
*   **Focus:** Loss of Exclusivity (LoE), legal landscape.

**Query:** "Analyze Freedom-to-Operate (FTO) risk for a sustained-release formulation of Sitagliptin in Brazil."
*   **Focus:** Formulation patents, regional IP landscape.

## 4. Supply Chain Risk
**Query:** "Assess the supply chain dependency risk for Cephalosporin API imports from China over the last 12 months."
*   **Focus:** Import volumes, single-source risks, geopolitical trends (EXIM data).

**Query:** "Analyze the impact of recent trade restrictions on Insulin analog imports into India."
*   **Focus:** Trade barriers, volume fluctuations, domestic capacity.

## 5. Clinical Pipeline Analysis
**Query:** "Map the competitive landscape of Phase 3 Alzheimer's disease disease-modifying therapies in Japan."
*   **Focus:** Late-stage pipeline, competitor trial status, regional focus.

**Query:** "Identify sponsors with active oncology trials for CAR-T therapies targeting solid tumors."
*   **Focus:** Innovation leaders, trial status, technology platforms.

---

## Example API Request

You can test the system using the following `curl` command. This sends a query to the Master Agent, which orchestrates the analysis and returns a JSON response with a link to the generated PDF report.

### cURL Command
```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{
           "query": "Which respiratory diseases show low competition but high patient burden in India?",
           "filters": {
             "country": "India",
             "therapy_area": "Respiratory"
           }
         }'
```

### JSON Payload
```json
{
  "query": "Which respiratory diseases show low competition but high patient burden in India?",
  "filters": {
    "country": "India",
    "therapy_area": "Respiratory"
  }
}
```
