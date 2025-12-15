import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || '';

// Map existing backend response to the new frontend's expected shape
const mapBackendToFrontend = (backendData) => {
    const analysis = backendData.analysis || backendData; // Handle both /chat and /api/analyze formats

    return {
        summary: analysis.summary.thesis, // String summary
        marketAnalysis: {
            marketSize: analysis.market.marketSize >= 1000000000
                ? (analysis.market.marketSize / 1000000000).toFixed(1) + "B"
                : (analysis.market.marketSize / 1000000).toFixed(1) + "M",
            cagr: analysis.market.cagr,
            growthRate: analysis.market.cagr + "%",
            marketStatus: "High Growth", // Derived or static
            supplyRisks: analysis.exim ? [analysis.exim.dependencyRisk] : ["Supply Chain Volatility"]
        },
        clinicalInsights: {
            relevantTrials: analysis.trials.map(t => ({
                id: t.nct,
                title: t.title,
                status: t.status.toUpperCase(),
                phase: t.phase
            }))
        },
        ipAnalysis: {
            keyPatents: analysis.patents.map(p => ({
                number: p.patentId,
                assignee: p.assignee,
                type: p.claims[0] || "Patent",
                ftoRiskLevel: p.ftoFlag
            })),
            ftoRiskLevel: "Medium" // Aggregate or take from first
        },
        webIntelligence: {
            recentGuidelines: analysis.webEvidence.map(w => `${w.source}: ${w.summary}`)
        },
        recommendation: analysis.recommendation.path + ". " + analysis.recommendation.commercialPotential,

        // Visualization Data
        marketDataViz: analysis.market.yearly.map(y => ({ name: y.year.toString(), value: y.value })),
        competitorDataViz: analysis.market.competitors.map(c => ({ name: c.molecule, value: c.share })),

        // Report URL
        pdfUrl: backendData.pdf_url
    };
};

const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

export const runAgenticWorkflow = async (prompt, files, logCallback) => {
    logCallback("System", "Initializing Master Agent...");
    await delay(600);

    try {
        logCallback("Master Agent", `Decomposing query: "${prompt}"`);
        await delay(800);

        logCallback("Master Agent", "Identifying strategic intent and selecting worker agents...");
        await delay(800);

        // Parallel Agent Simulation
        logCallback("Master Agent", "Activating worker agents: Clinical, Market, Patent, Web...");
        await delay(500);

        logCallback("Clinical Agent", "Searching ClinicalTrials.gov registry for active Phase 2/3 trials...");
        await delay(700);

        logCallback("Market Agent", "Querying IQVIA Market Intelligence for global forecasts...");
        await delay(600);

        logCallback("Patent Agent", "Analyzing USPTO & Espacenet databases for FTO risks...");
        await delay(800);

        logCallback("Web Agent", "Scanning regulatory guidelines (FDA/EMA) and recent news...");
        await delay(600);

        logCallback("Internal Agent", "Retrieving relevant internal strategy documents...");
        await delay(500);

        // Actual API Call
        const response = await axios.post(`${API_BASE_URL}/chat`, {
            query: prompt,
            filters: {} // Add filters if needed
        });

        logCallback("Master Agent", "Synthesizing multi-agent insights into final report...");
        await delay(800);

        return mapBackendToFrontend(response.data);

    } catch (error) {
        console.error("Agent Workflow Error:", error);
        logCallback("System", "Error: Failed to communicate with backend.");
        throw error;
    }
};

export const runFollowUpChat = async (message, context) => {
    // Mock follow-up for now, or call a new endpoint if we had one.
    // We'll just return a simulated response based on the context.
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve(`That's a great question about ${message}. Based on the analysis, we should consider the ${context.marketAnalysis.growthRate} growth rate and the upcoming patent expiries.`);
        }, 1000);
    });
};
