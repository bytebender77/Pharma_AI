from app.models import (
    TrialData, PatentData, MarketData, EximData, WebEvidence, Recommendation, Summary, AnalysisResult
)
import random

# ==========================================
# SCENARIO DATA STORE
# ==========================================
SCENARIOS = {
    # 1. Repurposing: Metformin in Pediatric NAFLD
    "metformin": {
        "market": MarketData(
            therapy="Pediatric Metabolic Disease",
            country="India",
            marketSize=45000000,  # $45M
            yearly=[{"year": 2022, "value": 38}, {"year": 2023, "value": 42}, {"year": 2024, "value": 45}, {"year": 2025, "value": 50}],
            cagr=9.8,
            competitors=[{"molecule": "Sitagliptin", "share": 28}, {"molecule": "Pioglitazone", "share": 22}, {"molecule": "Metformin (current)", "share": 35}]
        ),
        "exim": EximData(exportVolume=1200000, importVolume=500000, dependencyRisk="Medium", trend="Increasing import dependency for API"),
        "patents": [
            PatentData(patentId="US10234567B2", title="Method for sustained-release metformin", assignee="Pharma Corp A", filingDate="2015-03", grantDate="2019-11", expiryDate="2035-03", claims=["Formulation", "Method-of-use"], ftoFlag="Low", source="USPTO"),
            PatentData(patentId="EP3456789B1", title="Pediatric dosing of metformin XR", assignee="Generics Inc", filingDate="2016-05", grantDate="2020-08", expiryDate="2036-05", claims=["Dosing"], ftoFlag="Medium", source="Espacenet"),
            PatentData(patentId="WO2021001234", title="Liquid Metformin Formulation", assignee="Pediatric Meds Ltd", filingDate="2020-06", grantDate="Pending", expiryDate="2040-06", claims=["Formulation"], ftoFlag="High", source="WIPO")
        ],
        "trials": [
            TrialData(nct="NCT04567890", title="Metformin in Pediatric NAFLD", phase="Phase 2", status="Active", sponsor="Hospital XYZ", enrollment=240, startDate="2022-01", completionDate="2025-06", primaryEndpoint="Liver Fat Reduction", results=True),
            TrialData(nct="NCT03998765", title="Metformin for Pediatric Obesity", phase="Phase 2", status="Completed", sponsor="University ABC", enrollment=180, startDate="2020-06", completionDate="2024-03", primaryEndpoint="Weight Loss", results=True),
            TrialData(nct="NCT05551212", title="Metformin + Lifestyle in Obese Youth", phase="Phase 3", status="Recruiting", sponsor="NIDDK", enrollment=400, startDate="2023-09", completionDate="2026-09", primaryEndpoint="BMI Reduction", results=False),
            TrialData(nct="NCT06662323", title="Long-term Safety of Metformin", phase="Phase 4", status="Active", sponsor="Generic Pharma Co", enrollment=1000, startDate="2021-01", completionDate="2025-12", primaryEndpoint="Adverse Events", results=True)
        ],
        "web": [
            WebEvidence(source="ADA Guidelines 2024", type="Guideline", summary="Recommends metformin as first-line therapy for pediatric Type 2 diabetes", link="#"),
            WebEvidence(source="Pediatric Endocrinology Review", type="Review Article", summary="Emerging evidence for metformin in NAFLD prevention", link="#"),
            WebEvidence(source="AASLD Practice Guidance", type="Guideline", summary="Highlights need for pharmacological options in pediatric NASH", link="#"),
            WebEvidence(source="Clinical Liver Disease Journal", type="Journal", summary="Metformin shows promise in reducing BMI z-score in adolescents", link="#")
        ],
        "recommendation": Recommendation(
            path="505(b)(2) pathway with pediatric study plan",
            timeline="18-24 months to Phase 2 completion",
            nextSteps=["Conduct PK bridging study (6 months)", "Engage pediatric KOLs (2 months)", "Formulation feasibility assessment (3 months)"],
            commercialPotential="High — market entry within 3 years; estimated peak sales $25M+ in India"
        ),
        "summary": Summary(
            thesis="High-opportunity repurposing of metformin in pediatric metabolic disease—low patent risk, strong market growth (12% CAGR), and positive early Phase 2 data.",
            confidence="High",
            riskFlags=["Patent expiry in 3+ years (low risk)", "Positive Phase 2 enrollment", "Competitive pressure: medium"]
        )
    },

    # 2. Repurposing: SGLT2 in HFpEF
    "sglt2_hf": {
        "market": MarketData(
            therapy="Heart Failure (HFpEF)",
            country="Global",
            marketSize=6500000000,  # $6.5B
            yearly=[{"year": 2022, "value": 4.2}, {"year": 2023, "value": 5.1}, {"year": 2024, "value": 6.5}, {"year": 2025, "value": 7.8}],
            cagr=18.5,
            competitors=[{"molecule": "Empagliflozin", "share": 45}, {"molecule": "Dapagliflozin", "share": 40}, {"molecule": "Sotagliflozin", "share": 15}]
        ),
        "exim": EximData(exportVolume=8000000, importVolume=2000000, dependencyRisk="Low", trend="Stable API supply from multiple regions"),
        "patents": [
            PatentData(patentId="US9988771B2", title="SGLT2 Inhibitor for Treating Heart Failure", assignee="Boehringer Ingelheim", filingDate="2014-02", grantDate="2018-06", expiryDate="2034-02", claims=["Method-of-use"], ftoFlag="High", source="USPTO"),
            PatentData(patentId="EP2233445B1", title="Crystalline Form of Dapagliflozin", assignee="AstraZeneca", filingDate="2010-11", grantDate="2015-04", expiryDate="2030-11", claims=["Composition"], ftoFlag="Medium", source="Espacenet"),
            PatentData(patentId="US11223344", title="Combination SGLT2 + Diuretic", assignee="CardioPharma", filingDate="2018-05", grantDate="2022-01", expiryDate="2038-05", claims=["Composition"], ftoFlag="Medium", source="USPTO")
        ],
        "trials": [
            TrialData(nct="NCT04445555", title="Empagliflozin in Non-Diabetic HFpEF", phase="Phase 3", status="Completed", sponsor="Boehringer Ingelheim", enrollment=5000, startDate="2020-01", completionDate="2023-12", primaryEndpoint="CV Death or HHF", results=True),
            TrialData(nct="NCT05556666", title="SGLT2i Combination Therapy in HF", phase="Phase 2", status="Recruiting", sponsor="Academic Medical Center", enrollment=300, startDate="2023-06", completionDate="2025-06", primaryEndpoint="Biomarker reduction", results=False),
            TrialData(nct="NCT06667788", title="Dapagliflozin in Acute Heart Failure", phase="Phase 3", status="Completed", sponsor="AstraZeneca", enrollment=2000, startDate="2021-03", completionDate="2024-01", primaryEndpoint="Worsening Heart Failure", results=True),
            TrialData(nct="NCT07778899", title="SGLT2i in CKD without Diabetes", phase="Phase 3", status="Active", sponsor="Kidney Research Inst", enrollment=4000, startDate="2022-05", completionDate="2025-05", primaryEndpoint="eGFR Decline", results=True)
        ],
        "web": [
            WebEvidence(source="ESC Guidelines 2023", type="Guideline", summary="Class I recommendation for SGLT2 inhibitors in HFpEF regardless of diabetes status", link="#"),
            WebEvidence(source="Cardiology Today", type="News", summary="SGLT2 inhibitors show consistent benefit across ejection fraction spectrum", link="#"),
            WebEvidence(source="AHA Scientific Statement", type="Guideline", summary="Role of SGLT2 inhibitors in preventing heart failure hospitalization", link="#"),
            WebEvidence(source="NEJM", type="Journal", summary="Dapagliflozin reduces risk of worsening heart failure", link="#")
        ],
        "recommendation": Recommendation(
            path="Label Expansion / New Indication",
            timeline="6-12 months for regulatory approval (sNDA)",
            nextSteps=["Submit sNDA based on EMPEROR-Preserved data", "Launch medical education campaign for cardiologists", "Update payer value dossiers"],
            commercialPotential="Very High — Standard of care status in a massive, previously underserved patient population"
        ),
        "summary": Summary(
            thesis="SGLT2 inhibitors have transformed HFpEF management. Strong clinical evidence and guideline endorsement drive rapid adoption.",
            confidence="Very High",
            riskFlags=["Generic entry for dapagliflozin in some markets", "Pricing pressure from payers"]
        )
    },

    # 3. Market Gap: Respiratory in India
    "respiratory_india": {
        "market": MarketData(
            therapy="Respiratory (COPD/Asthma)",
            country="India",
            marketSize=1800000000,  # $1.8B
            yearly=[{"year": 2022, "value": 1.4}, {"year": 2023, "value": 1.6}, {"year": 2024, "value": 1.8}, {"year": 2025, "value": 2.1}],
            cagr=11.2,
            competitors=[{"molecule": "Formoterol/Budesonide", "share": 35}, {"molecule": "Salmeterol/Fluticasone", "share": 25}, {"molecule": "Tiotropium", "share": 15}]
        ),
        "exim": EximData(exportVolume=500000, importVolume=1500000, dependencyRisk="Medium", trend="High import of device components (inhalers)"),
        "patents": [
            PatentData(patentId="IN334455", title="Dry Powder Inhaler Device", assignee="Cipla Ltd", filingDate="2012-05", grantDate="2019-08", expiryDate="2032-05", claims=["Device"], ftoFlag="High", source="Indian Patent Office"),
            PatentData(patentId="IN445566", title="Novel Triple Combination for COPD", assignee="GlaxoSmithKline", filingDate="2016-01", grantDate="2021-03", expiryDate="2036-01", claims=["Composition"], ftoFlag="Medium", source="Indian Patent Office"),
            PatentData(patentId="IN556677", title="Inhaler Counter Mechanism", assignee="Device Co", filingDate="2018-02", grantDate="2023-01", expiryDate="2038-02", claims=["Device"], ftoFlag="Low", source="Indian Patent Office")
        ],
        "trials": [
            TrialData(nct="NCT06667777", title="Triple Therapy in Indian COPD Patients", phase="Phase 3", status="Recruiting", sponsor="Cipla", enrollment=800, startDate="2023-09", completionDate="2025-12", primaryEndpoint="Lung Function (FEV1)", results=False),
            TrialData(nct="NCT07778888", title="Biologic for Severe Asthma in India", phase="Phase 3", status="Active", sponsor="AstraZeneca", enrollment=400, startDate="2023-01", completionDate="2026-01", primaryEndpoint="Exacerbation Rate", results=False),
            TrialData(nct="NCT08889900", title="Generic Tiotropium/Olodaterol BE Study", phase="Phase 1", status="Completed", sponsor="Lupin", enrollment=60, startDate="2023-02", completionDate="2023-08", primaryEndpoint="PK Parameters", results=True),
            TrialData(nct="NCT09990011", title="Pediatric Asthma Cohort Study", phase="Observational", status="Active", sponsor="AIIMS", enrollment=1000, startDate="2022-01", completionDate="2027-01", primaryEndpoint="Disease Progression", results=False)
        ],
        "web": [
            WebEvidence(source="GOLD Guidelines 2024", type="Guideline", summary="Emphasis on early triple therapy for symptomatic COPD", link="#"),
            WebEvidence(source="Times of India Health", type="News", summary="Rising pollution levels driving spike in respiratory cases across metros", link="#"),
            WebEvidence(source="CDSCO Alert", type="Regulatory", summary="New quality standards for inhalation aerosols", link="#"),
            WebEvidence(source="Indian Journal of Chest Diseases", type="Journal", summary="Prevalence of severe asthma in India is underestimated", link="#")
        ],
        "recommendation": Recommendation(
            path="Generic/Branded Generic Entry + Device Innovation",
            timeline="2-3 years for development and BE studies",
            nextSteps=["Develop cost-effective DPI device", "Conduct bioequivalence study for triple combination", "Target tier-2/3 cities with affordable pricing"],
            commercialPotential="High — Volume-driven market with significant unmet need due to pollution and smoking rates"
        ),
        "summary": Summary(
            thesis="India's respiratory market is growing rapidly. Opportunity exists for affordable triple combinations and smart inhaler devices.",
            confidence="High",
            riskFlags=["Price control (NLEM)", "Intense competition in generic space", "Regulatory hurdles for new combinations"]
        )
    },

    # 4. Market Gap: Rare Genetic Disorders (EU)
    "rare_disease": {
        "market": MarketData(
            therapy="Rare Genetic Disorders (DMD/SMA)",
            country="EU",
            marketSize=1200000000,  # $1.2B
            yearly=[{"year": 2022, "value": 0.9}, {"year": 2023, "value": 1.0}, {"year": 2024, "value": 1.2}, {"year": 2025, "value": 1.5}],
            cagr=15.5,
            competitors=[{"molecule": "GeneTherapy-A", "share": 45}, {"molecule": "Oligonucleotide-B", "share": 30}, {"molecule": "SmallMol-C", "share": 15}]
        ),
        "exim": EximData(exportVolume=5000, importVolume=20000, dependencyRisk="High", trend="Critical shortage of viral vectors"),
        "patents": [
            PatentData(patentId="US9988776B2", title="AAV Vector for Dystrophin Delivery", assignee="BioGen X", filingDate="2018-01", grantDate="2021-05", expiryDate="2038-01", claims=["Composition", "Vector"], ftoFlag="High", source="USPTO"),
            PatentData(patentId="EP4455667A1", title="Exon Skipping Oligomer", assignee="RarePharma Y", filingDate="2019-09", grantDate="Pending", expiryDate="2039-09", claims=["Method-of-treatment"], ftoFlag="Low", source="Espacenet"),
            PatentData(patentId="EP5566778B1", title="Viral Vector Manufacturing Process", assignee="VectorBio", filingDate="2017-04", grantDate="2022-08", expiryDate="2037-04", claims=["Process"], ftoFlag="Medium", source="Espacenet")
        ],
        "trials": [
            TrialData(nct="NCT05551234", title="Gene Therapy for DMD in Ambulatory Boys", phase="Phase 3", status="Recruiting", sponsor="BioGen X", enrollment=120, startDate="2023-01", completionDate="2026-12", primaryEndpoint="NSAJA Score", results=False),
            TrialData(nct="NCT06667890", title="Novel Small Molecule for SMA Type 1", phase="Phase 1", status="Active", sponsor="StartUp Z", enrollment=30, startDate="2024-02", completionDate="2025-08", primaryEndpoint="Safety & Tolerability", results=False),
            TrialData(nct="NCT07771234", title="Natural History of DMD", phase="Observational", status="Active", sponsor="Patient Advocacy Group", enrollment=500, startDate="2020-01", completionDate="2030-01", primaryEndpoint="Disease Progression", results=True),
            TrialData(nct="NCT08885678", title="Biomarker Validation for SMA", phase="Phase 2", status="Active", sponsor="University Hospital", enrollment=100, startDate="2022-06", completionDate="2025-06", primaryEndpoint="Neurofilament Levels", results=True)
        ],
        "web": [
            WebEvidence(source="EMA Orphan Designation", type="Regulatory", summary="Granted orphan drug status to new AAV-based therapy for DMD", link="#"),
            WebEvidence(source="Rare Disease Day Report", type="News", summary="EU highlights unmet need in non-ambulatory DMD patients", link="#"),
            WebEvidence(source="EU Joint Action", type="Regulatory", summary="New framework for cross-border genetic testing", link="#"),
            WebEvidence(source="Lancet Neurology", type="Journal", summary="Long-term outcomes of gene therapy in SMA", link="#")
        ],
        "recommendation": Recommendation(
            path="Orphan Drug Designation + Accelerated Assessment (EMA)",
            timeline="3-4 years to MAA submission",
            nextSteps=["Apply for Orphan Designation (3 months)", "Initiate Natural History Study (12 months)", "Secure viral vector manufacturing slot"],
            commercialPotential="Very High — high unmet need, premium pricing potential ($300k+/yr), limited competition"
        ),
        "summary": Summary(
            thesis="Significant unmet need in rare genetic disorders in EU. High barrier to entry but substantial commercial reward due to orphan pricing and regulatory incentives.",
            confidence="Medium-High",
            riskFlags=["High manufacturing costs", "Complex regulatory landscape", "Reimbursement challenges"]
        )
    },

    # 5. Patent Expiry: Biologics (US)
    "biologics_expiry": {
        "market": MarketData(
            therapy="Immunology (Anti-TNF)",
            country="USA",
            marketSize=18000000000,  # $18B
            yearly=[{"year": 2022, "value": 20.5}, {"year": 2023, "value": 19.2}, {"year": 2024, "value": 18.0}, {"year": 2025, "value": 16.5}],
            cagr=-5.2,
            competitors=[{"molecule": "Humira (Originator)", "share": 55}, {"molecule": "Amjevita (Biosim)", "share": 20}, {"molecule": "Cyltezo (Biosim)", "share": 10}]
        ),
        "exim": EximData(exportVolume=200000, importVolume=500000, dependencyRisk="Low", trend="Domestic biosimilar manufacturing ramping up"),
        "patents": [
            PatentData(patentId="US8906377", title="Adalimumab Formulation (Citrate-free)", assignee="AbbVie", filingDate="2010-04", grantDate="2014-12", expiryDate="2030-04", claims=["Formulation"], ftoFlag="High", source="USPTO"),
            PatentData(patentId="US9512216", title="Dosing Regimen for RA", assignee="AbbVie", filingDate="2012-06", grantDate="2016-12", expiryDate="2032-06", claims=["Method-of-use"], ftoFlag="Medium", source="USPTO"),
            PatentData(patentId="US10112233", title="Buffer-free Formulation", assignee="AbbVie", filingDate="2014-01", grantDate="2018-05", expiryDate="2034-01", claims=["Formulation"], ftoFlag="High", source="USPTO")
        ],
        "trials": [
            TrialData(nct="NCT05554444", title="Interchangeability Study for Adalimumab Biosimilar", phase="Phase 3", status="Completed", sponsor="Sandoz", enrollment=450, startDate="2021-06", completionDate="2023-06", primaryEndpoint="PK Similarity", results=True),
            TrialData(nct="NCT06665555", title="High-Concentration Biosimilar vs Humira", phase="Phase 1", status="Recruiting", sponsor="Celltrion", enrollment=100, startDate="2024-01", completionDate="2025-01", primaryEndpoint="Safety/PK", results=False),
            TrialData(nct="NCT07776666", title="Switching Study: Humira to Biosimilar", phase="Phase 3", status="Completed", sponsor="Amgen", enrollment=500, startDate="2020-01", completionDate="2022-12", primaryEndpoint="Efficacy Maintenance", results=True),
            TrialData(nct="NCT08887777", title="Autoinjector Usability Study", phase="Phase 1", status="Completed", sponsor="Boehringer Ingelheim", enrollment=50, startDate="2022-03", completionDate="2022-09", primaryEndpoint="Successful Injection Rate", results=True)
        ],
        "web": [
            WebEvidence(source="FDA Biosimilars List", type="Database", summary="Multiple interchangeable biosimilars approved for Humira", link="#"),
            WebEvidence(source="Managed Care Mag", type="News", summary="PBMs shifting formulary preference to lower-cost biosimilars", link="#"),
            WebEvidence(source="Purple Book Update", type="Regulatory", summary="New biosimilar determinations added", link="#"),
            WebEvidence(source="BioPharma Dive", type="News", summary="AbbVie market share erosion accelerates in 2024", link="#")
        ],
        "recommendation": Recommendation(
            path="Interchangeable Biosimilar Development",
            timeline="3-4 years (if starting now, late to market)",
            nextSteps=["Focus on high-concentration formulation", "Conduct switching studies for interchangeability", "Aggressive payer contracting strategy"],
            commercialPotential="Medium — Volume opportunity remains, but price erosion is severe (>60%)"
        ),
        "summary": Summary(
            thesis="The 'patent cliff' has arrived. Success now depends on formulation differentiation (high-conc, citrate-free) and interchangeability status.",
            confidence="High",
            riskFlags=["Intense competition (8+ biosimilars)", "Aggressive rebating by originator", "Litigation costs"]
        )
    },

    # 6. Patent Expiry: Sitagliptin FTO (Brazil)
    "sitagliptin_fto": {
        "market": MarketData(
            therapy="Diabetes (DPP-4 Inhibitors)",
            country="Brazil",
            marketSize=450000000,  # $450M
            yearly=[{"year": 2022, "value": 380}, {"year": 2023, "value": 410}, {"year": 2024, "value": 450}, {"year": 2025, "value": 480}],
            cagr=8.5,
            competitors=[{"molecule": "Januvia (Originator)", "share": 60}, {"molecule": "Galvus", "share": 25}, {"molecule": "Tradjenta", "share": 15}]
        ),
        "exim": EximData(exportVolume=0, importVolume=1000000, dependencyRisk="Medium", trend="Local manufacturing incentives increasing"),
        "patents": [
            PatentData(patentId="BR112012000123", title="Sitagliptin Phosphate Monohydrate", assignee="Merck Sharp & Dohme", filingDate="2006-07", grantDate="2018-05", expiryDate="2026-07", claims=["Composition", "Salt Form"], ftoFlag="High", source="INPI Brazil"),
            PatentData(patentId="BR112015005678", title="Sustained Release Tablet of Sitagliptin", assignee="Merck Sharp & Dohme", filingDate="2013-09", grantDate="2020-02", expiryDate="2033-09", claims=["Formulation"], ftoFlag="Medium", source="INPI Brazil"),
            PatentData(patentId="BR112010009988", title="Process for Sitagliptin Phosphate", assignee="Generic Co", filingDate="2008-01", grantDate="2015-06", expiryDate="2028-01", claims=["Process"], ftoFlag="Low", source="INPI Brazil")
        ],
        "trials": [
            TrialData(nct="NCT08887777", title="Bioequivalence of Generic Sitagliptin in Brazil", phase="Phase 1", status="Active", sponsor="Eurofarma", enrollment=60, startDate="2024-03", completionDate="2024-09", primaryEndpoint="PK Parameters", results=False),
            TrialData(nct="NCT09998888", title="Sitagliptin + Metformin FDC Study", phase="Phase 3", status="Recruiting", sponsor="EMS", enrollment=400, startDate="2023-11", completionDate="2025-05", primaryEndpoint="HbA1c Reduction", results=False),
            TrialData(nct="NCT01112233", title="Sitagliptin vs Linagliptin Head-to-Head", phase="Phase 4", status="Completed", sponsor="Academic", enrollment=800, startDate="2021-01", completionDate="2023-01", primaryEndpoint="Safety Profile", results=True),
            TrialData(nct="NCT02223344", title="Sitagliptin in Elderly Patients", phase="Phase 4", status="Active", sponsor="Merck Sharp & Dohme", enrollment=1200, startDate="2022-06", completionDate="2025-06", primaryEndpoint="Renal Safety", results=True)
        ],
        "web": [
            WebEvidence(source="ANVISA Database", type="Regulatory", summary="Upcoming patent expiry for base compound in 2026", link="#"),
            WebEvidence(source="Brazil Pharma News", type="News", summary="Domestic giants preparing generic launches for Januvia", link="#"),
            WebEvidence(source="Brazilian Diabetes Society", type="Guideline", summary="Sitagliptin remains preferred DPP-4i for elderly patients", link="#"),
            WebEvidence(source="Valor Econômico", type="News", summary="Price war expected in diabetes segment post-2026", link="#")
        ],
        "recommendation": Recommendation(
            path="Generic Launch (Paragraph IV equivalent)",
            timeline="Launch at risk or post-2026",
            nextSteps=["Develop non-infringing SR formulation", "File for ANVISA approval 18 months prior to expiry", "Secure API supply"],
            commercialPotential="High — Strong brand loyalty to be challenged by lower-cost generics"
        ),
        "summary": Summary(
            thesis="Main compound patent expires soon (2026). Opportunity for immediate generic entry for IR, but SR formulation has FTO barriers.",
            confidence="High",
            riskFlags=["Patent litigation on formulation", "ANVISA backlog", "Price competition from other local generics"]
        )
    },

    # 7. Supply Chain: Cephalosporin (China)
    "cephalosporin_supply": {
        "market": MarketData(
            therapy="Anti-Infectives (Cephalosporins)",
            country="Global",
            marketSize=12000000000,  # $12B
            yearly=[{"year": 2022, "value": 11.5}, {"year": 2023, "value": 11.8}, {"year": 2024, "value": 12.0}, {"year": 2025, "value": 12.3}],
            cagr=2.1,
            competitors=[{"molecule": "Ceftriaxone", "share": 30}, {"molecule": "Cefuroxime", "share": 25}, {"molecule": "Cefixime", "share": 20}]
        ),
        "exim": EximData(exportVolume=50000000, importVolume=10000000, dependencyRisk="Very High", trend="80% of Key Starting Materials (KSM) sourced from China"),
        "patents": [
            PatentData(patentId="CN102345678A", title="Process for Ceftriaxone Sodium", assignee="Shandong Pharma", filingDate="2010-05", grantDate="2013-08", expiryDate="2030-05", claims=["Process"], ftoFlag="Low", source="CNIPA"),
            PatentData(patentId="US7654321B2", title="Enzymatic Synthesis of Cephalosporins", assignee="DSM Sinochem", filingDate="2008-01", grantDate="2011-04", expiryDate="2028-01", claims=["Process"], ftoFlag="Medium", source="USPTO"),
            PatentData(patentId="CN105566778B", title="Improved Crystallization Method", assignee="North China Pharm", filingDate="2014-06", grantDate="2017-09", expiryDate="2034-06", claims=["Process"], ftoFlag="Low", source="CNIPA")
        ],
        "trials": [
            TrialData(nct="NCT06661122", title="New Sepsis Protocol with Ceftriaxone", phase="Phase 4", status="Active", sponsor="Global Health Org", enrollment=5000, startDate="2023-01", completionDate="2025-12", primaryEndpoint="Mortality", results=False),
            TrialData(nct="NCT07772233", title="Pediatric Pneumonia Study", phase="Phase 3", status="Completed", sponsor="Generic Co", enrollment=800, startDate="2021-05", completionDate="2023-05", primaryEndpoint="Clinical Cure", results=True)
        ],
        "web": [
            WebEvidence(source="FDA Drug Shortage List", type="Regulatory", summary="Intermittent shortages of injectable cephalosporins reported", link="#"),
            WebEvidence(source="Supply Chain Dive", type="News", summary="Geopolitical tensions impacting API shipments from China", link="#"),
            WebEvidence(source="WHO Essential Medicines", type="Regulatory", summary="Ceftriaxone listed as 'Access' antibiotic, critical for global health", link="#"),
            WebEvidence(source="CPhI Online", type="News", summary="API prices for cephalosporins rise 15% due to energy costs", link="#")
        ],
        "recommendation": Recommendation(
            path="Diversify Supply Chain / Backward Integration",
            timeline="12-24 months to qualify new suppliers",
            nextSteps=["Identify alternate API suppliers in India/Europe", "Audit suppliers for environmental compliance", "Stockpile KSMs for 6 months"],
            commercialPotential="Medium — Commodity market, but supply reliability is a key differentiator"
        ),
        "summary": Summary(
            thesis="High dependency on China for KSMs poses a significant risk. Diversification is critical to ensure business continuity.",
            confidence="Very High",
            riskFlags=["Single-source dependency", "Environmental regulations in China closing plants", "Price volatility"]
        )
    },

    # 8. Supply Chain: Insulin (India)
    "insulin_trade": {
        "market": MarketData(
            therapy="Diabetes (Insulin)",
            country="India",
            marketSize=1500000000,  # $1.5B
            yearly=[{"year": 2022, "value": 1.2}, {"year": 2023, "value": 1.35}, {"year": 2024, "value": 1.5}, {"year": 2025, "value": 1.7}],
            cagr=12.5,
            competitors=[{"molecule": "Human Insulin", "share": 40}, {"molecule": "Glargine", "share": 35}, {"molecule": "Aspart", "share": 25}]
        ),
        "exim": EximData(exportVolume=800000, importVolume=200000, dependencyRisk="Low", trend="India is a net exporter of insulin, but imports high-end analogs"),
        "patents": [
            PatentData(patentId="IN223344", title="Method for Insulin Glargine Production", assignee="Biocon", filingDate="2005-03", grantDate="2010-07", expiryDate="2025-03", claims=["Process"], ftoFlag="Low", source="Indian Patent Office"),
            PatentData(patentId="IN556677", title="Novel Ultra-Rapid Insulin Formulation", assignee="Novo Nordisk", filingDate="2015-11", grantDate="2020-05", expiryDate="2035-11", claims=["Formulation"], ftoFlag="High", source="Indian Patent Office"),
            PatentData(patentId="IN667788", title="Novel Insulin Pen Device", assignee="Device Corp", filingDate="2017-08", grantDate="2022-04", expiryDate="2037-08", claims=["Device"], ftoFlag="Medium", source="Indian Patent Office")
        ],
        "trials": [
            TrialData(nct="NCT03334444", title="Oral Insulin Phase 3 Study", phase="Phase 3", status="Recruiting", sponsor="Oramed", enrollment=400, startDate="2023-01", completionDate="2025-12", primaryEndpoint="HbA1c", results=False),
            TrialData(nct="NCT04445555", title="Weekly Insulin Icodec in India", phase="Phase 3", status="Active", sponsor="Novo Nordisk", enrollment=600, startDate="2022-06", completionDate="2024-12", primaryEndpoint="HbA1c", results=False),
            TrialData(nct="NCT05556677", title="Biosimilar Glargine in Type 1 Diabetes", phase="Phase 3", status="Recruiting", sponsor="Biocon", enrollment=300, startDate="2023-09", completionDate="2025-09", primaryEndpoint="Hypoglycemia Rate", results=False),
            TrialData(nct="NCT06667788", title="Insulin Pump Compatibility Study", phase="Phase 4", status="Completed", sponsor="Medtronic", enrollment=100, startDate="2022-01", completionDate="2023-01", primaryEndpoint="Occlusion Rate", results=True)
        ],
        "web": [
            WebEvidence(source="DGFT Notifications", type="Regulatory", summary="Restrictions on export of certain biologicals relaxed", link="#"),
            WebEvidence(source="Economic Times", type="News", summary="PLI scheme boosting domestic fermentation capacity for insulin", link="#"),
            WebEvidence(source="Pharmexcil Report", type="Report", summary="India's insulin exports to semi-regulated markets grew 15% YoY", link="#"),
            WebEvidence(source="Diabetes Care India", type="Journal", summary="Access to analog insulin remains a challenge in rural India", link="#")
        ],
        "recommendation": Recommendation(
            path="Domestic Manufacturing Expansion (PLI Scheme)",
            timeline="2-3 years for capacity expansion",
            nextSteps=["Apply for PLI benefits", "Scale up fermentation capacity", "Develop biosimilar Aspart/Lispro"],
            commercialPotential="High — Domestic demand growing + export potential to semi-regulated markets"
        ),
        "summary": Summary(
            thesis="India is self-sufficient in human insulin but relies on imports for novel analogs. PLI scheme offers opportunity to localize analog production.",
            confidence="High",
            riskFlags=["Cold chain logistics", "Regulatory approval for biosimilars in export markets", "Price caps"]
        )
    },

    # 9. Pipeline: Alzheimer's (Japan)
    "alzheimers_japan": {
        "market": MarketData(
            therapy="Neurology (Alzheimer's)",
            country="Japan",
            marketSize=3000000000,  # $3B
            yearly=[{"year": 2022, "value": 0.5}, {"year": 2023, "value": 1.2}, {"year": 2024, "value": 3.0}, {"year": 2025, "value": 5.5}],
            cagr=85.0,
            competitors=[{"molecule": "Lecanemab", "share": 70}, {"molecule": "Donanemab", "share": 20}, {"molecule": "Donepezil (Generic)", "share": 10}]
        ),
        "exim": EximData(exportVolume=0, importVolume=500000, dependencyRisk="Medium", trend="High demand for biologic imports"),
        "patents": [
            PatentData(patentId="JP6677889B2", title="Anti-Abeta Protofibril Antibody", assignee="BioArctic/Eisai", filingDate="2008-05", grantDate="2014-02", expiryDate="2028-05", claims=["Composition"], ftoFlag="High", source="JPO"),
            PatentData(patentId="JP7788990B2", title="Method for Early AD Diagnosis", assignee="Sysmex", filingDate="2016-01", grantDate="2019-06", expiryDate="2036-01", claims=["Diagnostic"], ftoFlag="Low", source="JPO"),
            PatentData(patentId="JP8899001A", title="Blood-based Biomarker for AD", assignee="Shimadzu", filingDate="2018-09", grantDate="Pending", expiryDate="2038-09", claims=["Diagnostic"], ftoFlag="Low", source="JPO")
        ],
        "trials": [
            TrialData(nct="NCT05558888", title="Subcutaneous Lecanemab in Japanese Patients", phase="Phase 3", status="Active", sponsor="Eisai", enrollment=300, startDate="2023-04", completionDate="2025-04", primaryEndpoint="Amyloid Clearance", results=False),
            TrialData(nct="NCT06669999", title="Novel Tau Aggregation Inhibitor", phase="Phase 2", status="Recruiting", sponsor="Takeda", enrollment=150, startDate="2024-01", completionDate="2026-01", primaryEndpoint="Cognitive Score (ADAS-Cog)", results=False),
            TrialData(nct="NCT07770011", title="Prevention Study in Pre-symptomatic AD", phase="Phase 3", status="Recruiting", sponsor="Eisai", enrollment=1000, startDate="2023-10", completionDate="2028-10", primaryEndpoint="Time to MCI", results=False),
            TrialData(nct="NCT08881122", title="Tau PET Imaging Correlation", phase="Observational", status="Active", sponsor="National Center for Geriatrics", enrollment=200, startDate="2022-05", completionDate="2025-05", primaryEndpoint="SUVr Correlation", results=True)
        ],
        "web": [
            WebEvidence(source="PMDA Updates", type="Regulatory", summary="Full approval granted for Lecanemab; pricing discussions ongoing", link="#"),
            WebEvidence(source="Nikkei Asia", type="News", summary="Aging population drives urgent demand for disease-modifying therapies", link="#"),
            WebEvidence(source="MHLW Notification", type="Regulatory", summary="New reimbursement pathway for high-cost AD drugs", link="#"),
            WebEvidence(source="Japan Times", type="News", summary="Eisai expands manufacturing capacity for Leqembi", link="#")
        ],
        "recommendation": Recommendation(
            path="Strategic Alliance / Co-promotion",
            timeline="6-12 months",
            nextSteps=["Partner with Eisai/Biogen for distribution", "Develop companion diagnostic", "Establish infusion center network"],
            commercialPotential="Very High — Rapidly aging demographic makes Japan a key market for AD therapies"
        ),
        "summary": Summary(
            thesis="Japan is a critical market for new AD therapies. Lecanemab dominance is established, but opportunity exists for subcutaneous formulations and tau-targeting agents.",
            confidence="High",
            riskFlags=["High cost of therapy", "Healthcare system budget constraints", "Requirement for PET/CSF diagnosis"]
        )
    },

    # 10. Pipeline: CAR-T Oncology
    "cart_oncology": {
        "market": MarketData(
            therapy="Oncology (Cell Therapy)",
            country="Global",
            marketSize=4500000000,  # $4.5B
            yearly=[{"year": 2022, "value": 2.5}, {"year": 2023, "value": 3.2}, {"year": 2024, "value": 4.5}, {"year": 2025, "value": 6.0}],
            cagr=28.0,
            competitors=[{"molecule": "Yescarta", "share": 35}, {"molecule": "Kymriah", "share": 30}, {"molecule": "Carvykti", "share": 25}]
        ),
        "exim": EximData(exportVolume=0, importVolume=0, dependencyRisk="High", trend="Vein-to-vein logistics are the bottleneck"),
        "patents": [
            PatentData(patentId="US10112233B2", title="Chimeric Antigen Receptor T-Cells", assignee="U. Penn / Novartis", filingDate="2012-08", grantDate="2016-05", expiryDate="2032-08", claims=["Composition", "Method"], ftoFlag="High", source="USPTO"),
            PatentData(patentId="US11223344B2", title="Allogeneic CAR-T Platform", assignee="Allogene", filingDate="2017-03", grantDate="2021-11", expiryDate="2037-03", claims=["Platform"], ftoFlag="Medium", source="USPTO"),
            PatentData(patentId="US12334455", title="Universal CAR-T Construct", assignee="Cellectis", filingDate="2018-09", grantDate="2023-02", expiryDate="2038-09", claims=["Composition"], ftoFlag="Medium", source="USPTO")
        ],
        "trials": [
            TrialData(nct="NCT08881111", title="CAR-T for Solid Tumors (Gastric Cancer)", phase="Phase 1", status="Recruiting", sponsor="Legend Biotech", enrollment=40, startDate="2024-02", completionDate="2026-02", primaryEndpoint="Safety/ORR", results=False),
            TrialData(nct="NCT09992222", title="Next-Gen Dual-Target CAR-T", phase="Phase 2", status="Active", sponsor="Gilead", enrollment=120, startDate="2023-08", completionDate="2025-08", primaryEndpoint="PFS", results=False),
            TrialData(nct="NCT01113344", title="CAR-T in Ovarian Cancer", phase="Phase 1", status="Recruiting", sponsor="BioNTech", enrollment=30, startDate="2024-05", completionDate="2026-05", primaryEndpoint="Dose Limiting Toxicity", results=False),
            TrialData(nct="NCT02224455", title="Allogeneic CAR-T in Pancreatic Cancer", phase="Phase 1", status="Active", sponsor="Allogene", enrollment=50, startDate="2023-11", completionDate="2025-11", primaryEndpoint="Safety", results=False)
        ],
        "web": [
            WebEvidence(source="ASCO 2024 Abstracts", type="Conference", summary="Promising early data for Claudin18.2 CAR-T in gastric cancer", link="#"),
            WebEvidence(source="FiercePharma", type="News", summary="Manufacturing failures remain a key challenge for autologous CAR-T", link="#"),
            WebEvidence(source="Nature Medicine", type="Journal", summary="Review: Overcoming the immunosuppressive tumor microenvironment", link="#"),
            WebEvidence(source="FDA Guidance", type="Regulatory", summary="Considerations for the development of CAR-T products", link="#")
        ],
        "recommendation": Recommendation(
            path="Invest in Allogeneic Platform / Solid Tumor Targets",
            timeline="5-7 years to market",
            nextSteps=["Acquire novel binder technology for solid tumors", "Develop 'off-the-shelf' allogeneic platform", "Automate manufacturing"],
            commercialPotential="Extremely High — Solving the solid tumor challenge is the 'holy grail' of cell therapy"
        ),
        "summary": Summary(
            thesis="Hematologic malignancies are crowded. The next frontier is solid tumors and allogeneic (off-the-shelf) therapies to reduce cost and complexity.",
            confidence="Medium",
            riskFlags=["Solid tumor microenvironment barriers", "Safety (CRS/ICANS)", "Manufacturing scalability"]
        )
    },
    
    # 11. Keytruda (Existing - kept for backward compatibility if needed)
    "keytruda": {
        "market": MarketData(
            therapy="Oncology (PD-1 Inhibitors)",
            country="Global",
            marketSize=25000000000,  # $25B
            yearly=[{"year": 2022, "value": 20.9}, {"year": 2023, "value": 25.0}, {"year": 2024, "value": 28.5}, {"year": 2025, "value": 32.0}],
            cagr=12.0,
            competitors=[{"molecule": "Keytruda", "share": 60}, {"molecule": "Opdivo", "share": 25}, {"molecule": "Tecentriq", "share": 10}]
        ),
        "exim": EximData(exportVolume=5000000, importVolume=100000, dependencyRisk="Low", trend="Stable global supply chain"),
        "patents": [
            PatentData(patentId="US8000123B2", title="Anti-PD-1 Antibodies", assignee="Merck Sharp & Dohme", filingDate="2008-06", grantDate="2011-12", expiryDate="2028-06", claims=["Composition of Matter"], ftoFlag="High", source="USPTO"),
            PatentData(patentId="US10555666B2", title="Method of treating lung cancer with PD-1 antagonist", assignee="Merck Sharp & Dohme", filingDate="2015-02", grantDate="2019-05", expiryDate="2036-02", claims=["Method-of-use"], ftoFlag="Medium", source="USPTO")
        ],
        "trials": [
            TrialData(nct="NCT07778888", title="Biosimilar Pembrolizumab vs Keytruda in NSCLC", phase="Phase 3", status="Recruiting", sponsor="Biosim Co", enrollment=600, startDate="2024-01", completionDate="2026-06", primaryEndpoint="ORR", results=False),
            TrialData(nct="NCT08889999", title="Keytruda + Novel ADC in Breast Cancer", phase="Phase 2", status="Active", sponsor="Merck", enrollment=250, startDate="2023-05", completionDate="2025-11", primaryEndpoint="PFS", results=False)
        ],
        "web": [
            WebEvidence(source="FDA Orange Book", type="Database", summary="Key composition patents expiring 2028; formulation patents extend to 2036", link="#"),
            WebEvidence(source="Oncology News", type="News", summary="Multiple biosimilar candidates entering Phase 3 trials for Keytruda", link="#")
        ],
        "recommendation": Recommendation(
            path="Biosimilar Development (351(k) pathway)",
            timeline="4-5 years to launch (target 2029)",
            nextSteps=["Complete Phase 3 comparative efficacy study", "Develop patent litigation strategy (inter partes review)", "Optimize manufacturing yield"],
            commercialPotential="High — Multi-billion dollar opportunity upon patent expiry, though intense competition expected"
        ),
        "summary": Summary(
            thesis="Keytruda patent cliff in 2028 presents a massive biosimilar opportunity. Success requires navigating complex 'patent thicket' and ensuring interchangeability.",
            confidence="High",
            riskFlags=["Litigation risk (patent thicket)", "Crowded biosimilar pipeline", "Price erosion post-LOE"]
        )
    }
}

def get_scenario(query: str) -> str:
    q = query.lower()
    
    # 1. Metformin / Pediatric NAFLD
    if "metformin" in q and ("pediatric" in q or "nafld" in q):
        return "metformin"
    
    # 2. SGLT2 / HFpEF
    elif "sglt2" in q or "heart failure" in q or "hfpef" in q:
        return "sglt2_hf"
    
    # 3. Respiratory / India
    elif "respiratory" in q or ("india" in q and ("copd" in q or "asthma" in q)):
        return "respiratory_india"
    
    # 4. Rare Genetic / EU
    elif "rare" in q or "genetic" in q or "orphan" in q or "dmd" in q or "sma" in q:
        return "rare_disease"
    
    # 5. Biologics Expiry
    elif "biologic" in q or "expiry" in q or "biosimilar" in q or "humira" in q:
        return "biologics_expiry"
    
    # 6. Sitagliptin FTO
    elif "sitagliptin" in q or "brazil" in q:
        return "sitagliptin_fto"
    
    # 7. Cephalosporin Supply
    elif "cephalosporin" in q or "supply chain" in q or "api" in q:
        return "cephalosporin_supply"
    
    # 8. Insulin Trade
    elif "insulin" in q or "trade" in q or "import" in q:
        return "insulin_trade"
    
    # 9. Alzheimer's Japan
    elif "alzheimer" in q or "japan" in q or "lecanemab" in q:
        return "alzheimers_japan"
    
    # 10. CAR-T Oncology
    elif "car-t" in q or "oncology" in q or "solid tumor" in q:
        return "cart_oncology"
    
    # Fallback / Default
    elif "keytruda" in q or "pembrolizumab" in q or "pd-1" in q:
        return "keytruda"
        
    else:
        return "metformin"

# ==========================================
# 1. IQVIA Mock API (Market Data)
# ==========================================
def get_iqvia_data(query: str) -> MarketData:
    scenario = get_scenario(query)
    return SCENARIOS[scenario]["market"]

# ==========================================
# 2. EXIM Mock Server (Export/Import)
# ==========================================
def get_exim_data(query: str) -> EximData:
    scenario = get_scenario(query)
    return SCENARIOS[scenario]["exim"]

# ==========================================
# 3. USPTO Patent Mock API
# ==========================================
def get_uspto_data(query: str) -> list[PatentData]:
    scenario = get_scenario(query)
    return SCENARIOS[scenario]["patents"]

# ==========================================
# 4. Clinical Trials Mock API
# ==========================================
def get_clinical_trials(query: str) -> list[TrialData]:
    scenario = get_scenario(query)
    return SCENARIOS[scenario]["trials"]

# ==========================================
# 5. Web Intelligence Mock Service
# ==========================================
def get_web_intelligence(query: str) -> list[WebEvidence]:
    scenario = get_scenario(query)
    return SCENARIOS[scenario]["web"]

# ==========================================
# Helper / Aggregator
# ==========================================

def get_mock_analysis_result(query: str) -> AnalysisResult:
    """
    Aggregates data from all mock services to form the final analysis result.
    """
    scenario = get_scenario(query)
    data = SCENARIOS[scenario]
    
    return AnalysisResult(
        summary=data["summary"],
        trials=get_clinical_trials(query),
        market=get_iqvia_data(query),
        exim=get_exim_data(query),
        patents=get_uspto_data(query),
        webEvidence=get_web_intelligence(query),
        recommendation=data["recommendation"]
    )
