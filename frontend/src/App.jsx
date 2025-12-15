import React, { useState, useRef, useEffect } from 'react';
import {
  Search, Filter, Download, Eye, ChevronDown, ChevronUp, AlertCircle,
  CheckCircle, TrendingUp, Beaker, BookOpen, Globe, Pill, BarChart3,
  Loader2, Upload, Send, Settings2, FileCheck, Bot, LayoutDashboard, Network,
  ShieldCheck, BrainCircuit, Factory
} from 'lucide-react';
import {
  LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip,
  Legend, ResponsiveContainer, PieChart, Pie, Cell
} from 'recharts';

import { runAgenticWorkflow, runFollowUpChat } from './services/geminiService';
import ArchitectureView from './components/ArchitectureView';

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884d8'];

// Example scenarios for quick access
const EXAMPLE_SCENARIOS = [
  {
    title: "Metformin Repurposing",
    desc: "Pediatric metabolic disease opportunities",
    icon: <Pill className="w-4 h-4 text-blue-500" />,
    prompt: "Find pediatric repurposing opportunities for metformin in India beyond diabetes.",
    strategy: { agents: ["Clinical", "Market", "Patent"], output: "Gap Analysis" }
  },
  {
    title: "Keytruda Patent Cliff",
    desc: "Biosimilar entry points 2028",
    icon: <ShieldCheck className="w-4 h-4 text-purple-500" />,
    prompt: "Analyze the patent cliff risks for Keytruda in 2028 and identify biosimilar entry points.",
    strategy: { agents: ["Patent", "Market", "Legal"], output: "Risk Assessment" }
  },
  {
    title: "Alzheimer's Market",
    desc: "EU disease modifying therapies",
    icon: <BrainCircuit className="w-4 h-4 text-emerald-500" />,
    prompt: "Evaluate the market potential for new Alzheimer's disease modifying therapies in the EU.",
    strategy: { agents: ["Market", "Clinical", "Regulatory"], output: "Market Forecast" }
  },
  {
    title: "mRNA Supply Chain",
    desc: "Southeast Asia manufacturing",
    icon: <Factory className="w-4 h-4 text-orange-500" />,
    prompt: "Identify supply chain vulnerabilities for mRNA vaccine production in Southeast Asia.",
    strategy: { agents: ["EXIM", "Market", "Geopolitics"], output: "Supply Chain Map" }
  }
];

export default function App() {
  const [prompt, setPrompt] = useState('');
  const [advancedOpen, setAdvancedOpen] = useState(false);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [expandedSections, setExpandedSections] = useState({
    trials: false,
    market: false,
    patents: false,
    web: false
  });
  const [darkMode, setDarkMode] = useState(true);
  const [filters, setFilters] = useState({
    molecule: '',
    indication: '',
    country: 'India',
    dateRange: '2-years',
    pediatric: false,
    sources: ['clinical', 'market', 'patent', 'web', 'internal']
  });

  // Backend Integration State
  const [activeView, setActiveView] = useState('workspace');
  const [logs, setLogs] = useState([]);
  const [files, setFiles] = useState([]);
  const [chatInput, setChatInput] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const [isChatProcessing, setIsChatProcessing] = useState(false);

  const logsEndRef = useRef(null);
  const chatEndRef = useRef(null);

  // Auto-scroll logs
  useEffect(() => {
    logsEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [logs]);

  // Auto-scroll chat
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [chatHistory]);

  const handleLog = (agentName, message) => {
    setLogs(prev => [...prev, {
      id: Math.random().toString(36).substring(7),
      agentName,
      message,
      timestamp: new Date(),
      status: message.toLowerCase().includes('error') ? 'error' : 'info'
    }]);
  };

  const handleFileUpload = async (e) => {
    if (e.target.files && e.target.files.length > 0) {
      const newFiles = [];
      for (let i = 0; i < e.target.files.length; i++) {
        const file = e.target.files[i];
        const text = await file.text();
        newFiles.push({ name: file.name, content: text, type: file.type });
      }
      setFiles(prev => [...prev, ...newFiles]);
      handleLog("System", `Uploaded ${newFiles.length} files for RAG context.`);
    }
  };

  const handleSearch = async (searchPrompt = prompt) => {
    if (!searchPrompt.trim()) return;
    setPrompt(searchPrompt);
    setLoading(true);
    setResults(null);
    setLogs([]);
    setChatHistory([]);

    try {
      const report = await runAgenticWorkflow(searchPrompt, files, handleLog);
      setResults(report);
      handleLog("System", "Report generated successfully.");
    } catch (error) {
      console.error(error);
      handleLog("System", "Critical Error: Failed to generate report.");
    } finally {
      setLoading(false);
    }
  };

  const handleFollowUp = async () => {
    if (!chatInput.trim() || !results) return;

    const userMsg = chatInput;
    setChatInput('');
    setIsChatProcessing(true);
    setChatHistory(prev => [...prev, { id: Date.now().toString(), role: 'user', content: userMsg }]);

    try {
      const response = await runFollowUpChat(userMsg, results);
      setChatHistory(prev => [...prev, { id: (Date.now() + 1).toString(), role: 'assistant', content: response }]);
    } catch (e) {
      setChatHistory(prev => [...prev, { id: (Date.now() + 1).toString(), role: 'assistant', content: "Error connecting to agent." }]);
    } finally {
      setIsChatProcessing(false);
    }
  };

  const handleGenerateReport = () => {
    if (results && results.pdfUrl) {
      window.open(results.pdfUrl, '_blank');
    } else {
      alert('Report generation failed or URL not available.');
    }
  };

  const TrialCard = ({ trial }) => (
    <div className={`border rounded-lg p-4 mb-3 hover:shadow-md transition ${darkMode ? 'border-slate-700 bg-slate-800/50' : 'border-gray-200 bg-white'}`}>
      <div className="flex justify-between items-start mb-2">
        <div>
          <p className="font-mono text-sm font-bold text-blue-500">{trial.id || "NCT..."}</p>
          <p className={`font-semibold ${darkMode ? 'text-slate-200' : 'text-gray-800'}`}>{trial.title}</p>
        </div>
        <span className={`px-2 py-1 rounded text-xs font-bold ${trial.status === 'RECRUITING' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'}`}>
          {trial.status}
        </span>
      </div>
      <div className={`grid grid-cols-2 gap-2 text-sm ${darkMode ? 'text-slate-400' : 'text-gray-600'}`}>
        <p><strong>Phase:</strong> {trial.phase}</p>
      </div>
    </div>
  );

  const PatentCard = ({ patent }) => (
    <div className={`border rounded-lg p-4 mb-3 ${darkMode ? 'border-slate-700 bg-slate-800/50' : 'border-gray-200 bg-white'}`}>
      <div className="flex justify-between items-start mb-2">
        <div>
          <p className="font-mono text-sm font-bold text-purple-500">{patent.number}</p>
          <p className={`font-semibold ${darkMode ? 'text-slate-200' : 'text-gray-800'}`}>{patent.assignee}</p>
        </div>
        <span className={`px-2 py-1 rounded text-xs font-bold ${results?.ipAnalysis.ftoRiskLevel === 'Low' ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'}`}>
          Type: {patent.type}
        </span>
      </div>
    </div>
  );

  return (
    <div className={`min-h-screen transition-colors ${darkMode ? 'bg-[#0B1120] text-slate-100' : 'bg-slate-50 text-slate-900'}`}>

      {/* Header */}
      <header className={`${darkMode ? 'bg-[#0B1120] border-slate-800' : 'bg-white border-blue-100'} shadow-sm border-b transition-colors`}>
        <div className="max-w-7xl mx-auto px-6 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <div className="flex items-center gap-3">
                <div className="bg-blue-600/20 p-2 rounded-lg border border-blue-500/20">
                  <Beaker className="w-8 h-8 text-blue-500" />
                </div>
                <div>
                  <h1 className={`text-2xl font-bold tracking-tight ${darkMode ? 'text-white' : 'text-gray-900'}`}>R&D Innovation Master Agent</h1>
                  <p className={`text-xs font-medium ${darkMode ? 'text-slate-400' : 'text-gray-600'}`}>Orchestrated analysis of repurposing & innovation opportunities</p>
                </div>
              </div>

              {/* View Switcher */}
              <div className={`ml-8 flex items-center p-1 rounded-lg border ${darkMode ? 'bg-slate-900 border-slate-800' : 'bg-slate-100 border-slate-200'}`}>
                <button
                  onClick={() => setActiveView('workspace')}
                  className={`px-3 py-1.5 rounded-md text-xs font-medium transition-colors ${activeView === 'workspace' ? (darkMode ? 'bg-slate-800 text-white shadow' : 'bg-white text-blue-600 shadow') : 'text-slate-500 hover:text-slate-400'}`}
                >
                  Workspace
                </button>
                <button
                  onClick={() => setActiveView('architecture')}
                  className={`px-3 py-1.5 rounded-md text-xs font-medium transition-colors ${activeView === 'architecture' ? (darkMode ? 'bg-slate-800 text-white shadow' : 'bg-white text-blue-600 shadow') : 'text-slate-500 hover:text-slate-400'}`}
                >
                  Architecture
                </button>
              </div>
            </div>

            <button
              onClick={() => setDarkMode(!darkMode)}
              className={`px-4 py-2 rounded-lg font-semibold text-xs transition ${darkMode ? 'bg-slate-800 text-yellow-400 hover:bg-slate-700 border border-slate-700' : 'bg-gray-200 text-gray-900 hover:bg-gray-300'}`}
            >
              {darkMode ? '☀️ Light' : '🌙 Dark'}
            </button>
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-6 py-8">

        {activeView === 'architecture' ? (
          <div className={`rounded-xl border p-6 min-h-[600px] ${darkMode ? 'bg-[#151B2B] border-slate-800' : 'bg-white border-slate-200'}`}>
            <ArchitectureView darkMode={darkMode} />
          </div>
        ) : (
          <>
            {/* Search Section */}
            <div className={`rounded-xl shadow-xl p-8 mb-8 transition-colors ${darkMode ? 'bg-[#151B2B] border border-slate-800 shadow-black/20' : 'bg-white border border-blue-100'}`}>
              <div className="mb-6">
                <label className={`block text-xs font-semibold uppercase tracking-wider mb-3 ${darkMode ? 'text-slate-400' : 'text-gray-700'}`}>Research Query</label>
                <div className="flex gap-3">
                  <input
                    type="text"
                    value={prompt}
                    onChange={(e) => setPrompt(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
                    placeholder="E.g., Find pediatric repurposing opportunities for metformin in India..."
                    className={`flex-1 px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition ${darkMode ? 'bg-slate-800/50 border-slate-700 text-white placeholder-slate-500' : 'bg-white border-gray-300 text-gray-900'}`}
                  />
                  <button
                    onClick={() => handleSearch()}
                    disabled={loading}
                    className="px-8 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-500 disabled:opacity-50 flex items-center gap-2 transition shadow-lg shadow-blue-900/20"
                  >
                    {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : <Search className="w-4 h-4" />}
                    {loading ? 'Analyzing...' : 'Search'}
                  </button>
                </div>
              </div>

              {/* Advanced Filters & Upload */}
              <div className="flex items-center justify-between">
                <button
                  onClick={() => setAdvancedOpen(!advancedOpen)}
                  className={`flex items-center gap-2 text-xs font-medium transition ${darkMode ? 'text-blue-400 hover:text-blue-300' : 'text-blue-600 hover:text-blue-700'}`}
                >
                  <Settings2 className="w-3.5 h-3.5" />
                  Advanced Filters {advancedOpen ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
                </button>

                <label className={`flex items-center gap-2 text-xs cursor-pointer transition-colors ${darkMode ? 'text-slate-400 hover:text-white' : 'text-slate-500 hover:text-slate-800'}`}>
                  <Upload className="w-3.5 h-3.5" />
                  <span className="truncate max-w-[150px]">{files.length > 0 ? `${files.length} files attached` : 'Attach Context (PDF/TXT)'}</span>
                  <input type="file" className="hidden" onChange={handleFileUpload} multiple accept=".txt,.md,.json,.csv" />
                </label>
              </div>

              {advancedOpen && (
                <div className={`mt-4 rounded-lg p-4 grid grid-cols-2 md:grid-cols-4 gap-4 border transition ${darkMode ? 'bg-slate-800/50 border-slate-700' : 'bg-gray-50 border-gray-200'}`}>
                  <div>
                    <label className={`block text-xs font-semibold mb-2 ${darkMode ? 'text-slate-400' : 'text-gray-600'}`}>Molecule</label>
                    <input
                      type="text"
                      value={filters.molecule}
                      onChange={(e) => setFilters({ ...filters, molecule: e.target.value })}
                      placeholder="e.g., Metformin"
                      className={`w-full px-3 py-2 border rounded text-sm ${darkMode ? 'bg-slate-900 border-slate-700 text-white' : 'bg-white border-gray-300'}`}
                    />
                  </div>
                  <div>
                    <label className={`block text-xs font-semibold mb-2 ${darkMode ? 'text-slate-400' : 'text-gray-600'}`}>Indication</label>
                    <input
                      type="text"
                      value={filters.indication}
                      onChange={(e) => setFilters({ ...filters, indication: e.target.value })}
                      placeholder="e.g., NAFLD"
                      className={`w-full px-3 py-2 border rounded text-sm ${darkMode ? 'bg-slate-900 border-slate-700 text-white' : 'bg-white border-gray-300'}`}
                    />
                  </div>
                  <div>
                    <label className={`block text-xs font-semibold mb-2 ${darkMode ? 'text-slate-400' : 'text-gray-600'}`}>Country</label>
                    <select
                      value={filters.country}
                      onChange={(e) => setFilters({ ...filters, country: e.target.value })}
                      className={`w-full px-3 py-2 border rounded text-sm ${darkMode ? 'bg-slate-900 border-slate-700 text-white' : 'bg-white border-gray-300'}`}
                    >
                      <option>India</option>
                      <option>USA</option>
                      <option>EU</option>
                    </select>
                  </div>
                  <div>
                    <label className={`block text-xs font-semibold mb-2 ${darkMode ? 'text-slate-400' : 'text-gray-600'}`}>Date Range</label>
                    <select
                      value={filters.dateRange}
                      onChange={(e) => setFilters({ ...filters, dateRange: e.target.value })}
                      className={`w-full px-3 py-2 border rounded text-sm ${darkMode ? 'bg-slate-900 border-slate-700 text-white' : 'bg-white border-gray-300'}`}
                    >
                      <option value="1-year">1 Year</option>
                      <option value="2-years">2 Years</option>
                      <option value="5-years">5 Years</option>
                    </select>
                  </div>
                </div>
              )}
            </div>

            {/* Results Section */}
            {results ? (
              <div className="space-y-6 pb-32 animate-fadeIn">
                {/* Executive Summary */}
                <div className={`rounded-xl shadow-md border p-8 ${darkMode ? 'bg-gradient-to-r from-slate-800 to-slate-900 border-slate-700' : 'bg-gradient-to-r from-blue-50 to-indigo-50 border-blue-200'}`}>
                  <div className="flex items-start gap-4">
                    <div className={`p-3 rounded-lg ${darkMode ? 'bg-blue-900/50' : 'bg-blue-100'}`}>
                      <CheckCircle className="w-6 h-6 text-blue-600" />
                    </div>
                    <div className="flex-1">
                      <h2 className={`text-2xl font-bold mb-2 ${darkMode ? 'text-white' : 'text-gray-900'}`}>Executive Summary</h2>
                      <p className={`text-lg leading-relaxed mb-4 ${darkMode ? 'text-slate-300' : 'text-gray-700'}`}>{results.summary}</p>
                      <div className="flex gap-8">
                        <div>
                          <p className={`text-xs font-semibold uppercase ${darkMode ? 'text-slate-400' : 'text-gray-600'}`}>Market Opportunity</p>
                          <p className="text-xl font-bold text-emerald-600">${results.marketAnalysis.marketSize}</p>
                        </div>
                        <div>
                          <p className={`text-xs font-semibold uppercase ${darkMode ? 'text-slate-400' : 'text-gray-600'}`}>Key Risk</p>
                          <div className="flex items-center gap-2 mt-1">
                            <AlertCircle className="w-4 h-4 text-amber-500" />
                            <span className={`text-sm font-medium ${darkMode ? 'text-slate-200' : 'text-gray-700'}`}>
                              {results.marketAnalysis.supplyRisks?.[0] || "Supply Chain Volatility"}
                            </span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Collapsible Sections */}
                {/* Clinical Trials */}
                <div className={`rounded-xl shadow-md border overflow-hidden ${darkMode ? 'bg-[#151B2B] border-slate-700' : 'bg-white border-gray-200'}`}>
                  <button
                    onClick={() => setExpandedSections(prev => ({ ...prev, trials: !prev.trials }))}
                    className={`w-full px-8 py-5 flex items-center justify-between border-b transition ${darkMode ? 'bg-slate-800/50 border-slate-700 hover:bg-slate-800' : 'bg-gradient-to-r from-emerald-50 to-teal-50 border-gray-200 hover:from-emerald-100'}`}
                  >
                    <div className="flex items-center gap-3">
                      <Beaker className="w-5 h-5 text-emerald-600" />
                      <h3 className={`font-bold ${darkMode ? 'text-slate-100' : 'text-gray-900'}`}>Clinical Trials ({results.clinicalInsights?.relevantTrials?.length || 0})</h3>
                    </div>
                    {expandedSections.trials ? <ChevronUp className={darkMode ? 'text-slate-400' : ''} /> : <ChevronDown className={darkMode ? 'text-slate-400' : ''} />}
                  </button>
                  {expandedSections.trials && (
                    <div className="p-8">
                      {results.clinicalInsights?.relevantTrials?.map((trial, i) => (
                        <TrialCard key={i} trial={trial} />
                      ))}
                      {(!results.clinicalInsights?.relevantTrials || results.clinicalInsights.relevantTrials.length === 0) && (
                        <p className="text-sm text-slate-500">No clinical trials found.</p>
                      )}
                    </div>
                  )}
                </div>

                {/* Market Data */}
                <div className={`rounded-xl shadow-md border overflow-hidden ${darkMode ? 'bg-[#151B2B] border-slate-700' : 'bg-white border-gray-200'}`}>
                  <button
                    onClick={() => setExpandedSections(prev => ({ ...prev, market: !prev.market }))}
                    className={`w-full px-8 py-5 flex items-center justify-between border-b transition ${darkMode ? 'bg-slate-800/50 border-slate-700 hover:bg-slate-800' : 'bg-gradient-to-r from-orange-50 to-amber-50 border-gray-200 hover:from-orange-100'}`}
                  >
                    <div className="flex items-center gap-3">
                      <BarChart3 className="w-5 h-5 text-orange-600" />
                      <h3 className={`font-bold ${darkMode ? 'text-slate-100' : 'text-gray-900'}`}>Market & Commercial Opportunity</h3>
                    </div>
                    {expandedSections.market ? <ChevronUp className={darkMode ? 'text-slate-400' : ''} /> : <ChevronDown className={darkMode ? 'text-slate-400' : ''} />}
                  </button>
                  {expandedSections.market && (
                    <div className="p-8">
                      {/* Market Analysis Section - Redesigned */}
                      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
                        <div className={`p-4 rounded-lg border ${darkMode ? 'bg-slate-800 border-slate-700' : 'bg-orange-50 border-orange-100'}`}>
                          <p className="text-xs font-semibold text-orange-600 mb-1">MARKET SIZE</p>
                          <p className={`text-2xl font-bold ${darkMode ? 'text-slate-100' : 'text-gray-900'}`}>${results.marketAnalysis.marketSize}</p>
                          <p className="text-xs text-gray-500">Global / Target</p>
                        </div>
                        <div className={`p-4 rounded-lg border ${darkMode ? 'bg-slate-800 border-slate-700' : 'bg-blue-50 border-blue-100'}`}>
                          <p className="text-xs font-semibold text-blue-600 mb-1">3-YEAR CAGR</p>
                          <p className={`text-2xl font-bold ${darkMode ? 'text-slate-100' : 'text-gray-900'}`}>{results.marketAnalysis.cagr || results.marketAnalysis.growthRate}</p>
                        </div>
                        <div className={`p-4 rounded-lg border ${darkMode ? 'bg-slate-800 border-slate-700' : 'bg-green-50 border-green-100'}`}>
                          <p className="text-xs font-semibold text-green-600 mb-1">STATUS</p>
                          <p className={`text-2xl font-bold ${darkMode ? 'text-slate-100' : 'text-gray-900'}`}>{results.marketAnalysis.marketStatus || "High Growth"}</p>
                        </div>
                      </div>

                      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                        <div>
                          <h4 className={`font-semibold mb-4 ${darkMode ? 'text-slate-200' : 'text-gray-900'}`}>Market Trend (2022-2025)</h4>
                          <div className="h-64">
                            <ResponsiveContainer width="100%" height="100%">
                              <LineChart data={results.marketDataViz}>
                                <CartesianGrid strokeDasharray="3 3" stroke={darkMode ? '#334155' : '#e2e8f0'} />
                                <XAxis dataKey="name" stroke={darkMode ? '#94a3b8' : '#64748b'} />
                                <YAxis stroke={darkMode ? '#94a3b8' : '#64748b'} />
                                <Tooltip contentStyle={{ backgroundColor: darkMode ? '#1e293b' : '#fff', borderColor: darkMode ? '#334155' : '#e2e8f0' }} />
                                <Line type="monotone" dataKey="value" stroke="#f97316" strokeWidth={2} dot={{ r: 4 }} />
                              </LineChart>
                            </ResponsiveContainer>
                          </div>
                        </div>
                        <div>
                          <h4 className={`font-semibold mb-4 ${darkMode ? 'text-slate-200' : 'text-gray-900'}`}>Competitive Share</h4>
                          <div className="h-64">
                            <ResponsiveContainer width="100%" height="100%">
                              <PieChart>
                                <Pie
                                  data={results.competitorDataViz || []}
                                  cx="50%"
                                  cy="50%"
                                  innerRadius={60}
                                  outerRadius={80}
                                  paddingAngle={5}
                                  dataKey="value"
                                >
                                  {(results.competitorDataViz || []).map((entry, index) => (
                                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                                  ))}
                                </Pie>
                                <Tooltip contentStyle={{ backgroundColor: darkMode ? '#1e293b' : '#fff', borderColor: darkMode ? '#334155' : '#e2e8f0' }} />
                                <Legend />
                              </PieChart>
                            </ResponsiveContainer>
                          </div>
                        </div>
                      </div>
                    </div>
                  )}
                </div>

                {/* Patents */}
                <div className={`rounded-xl shadow-md border overflow-hidden ${darkMode ? 'bg-[#151B2B] border-slate-700' : 'bg-white border-gray-200'}`}>
                  <button
                    onClick={() => setExpandedSections(prev => ({ ...prev, patents: !prev.patents }))}
                    className={`w-full px-8 py-5 flex items-center justify-between border-b transition ${darkMode ? 'bg-slate-800/50 border-slate-700 hover:bg-slate-800' : 'bg-gradient-to-r from-purple-50 to-indigo-50 border-gray-200 hover:from-purple-100'}`}
                  >
                    <div className="flex items-center gap-3">
                      <BookOpen className="w-5 h-5 text-purple-600" />
                      <h3 className={`font-bold ${darkMode ? 'text-slate-100' : 'text-gray-900'}`}>Patent Landscape & IP Risk ({results.ipAnalysis?.keyPatents?.length || 0})</h3>
                    </div>
                    {expandedSections.patents ? <ChevronUp className={darkMode ? 'text-slate-400' : ''} /> : <ChevronDown className={darkMode ? 'text-slate-400' : ''} />}
                  </button>
                  {expandedSections.patents && (
                    <div className="p-8">
                      {results.ipAnalysis?.keyPatents?.map((patent, i) => (
                        <PatentCard key={i} patent={patent} />
                      ))}
                      {(!results.ipAnalysis?.keyPatents || results.ipAnalysis.keyPatents.length === 0) && (
                        <p className="text-sm text-slate-500">No patents found.</p>
                      )}
                    </div>
                  )}
                </div>

                {/* Web Evidence & Guidelines */}
                <div className={`rounded-xl shadow-md border overflow-hidden ${darkMode ? 'bg-[#151B2B] border-slate-700' : 'bg-white border-gray-200'}`}>
                  <button
                    onClick={() => setExpandedSections(prev => ({ ...prev, web: !prev.web }))}
                    className={`w-full px-8 py-5 flex items-center justify-between border-b transition ${darkMode ? 'bg-slate-800/50 border-slate-700 hover:bg-slate-800' : 'bg-gradient-to-r from-cyan-50 to-blue-50 border-gray-200 hover:from-cyan-100'}`}
                  >
                    <div className="flex items-center gap-3">
                      <Globe className="w-5 h-5 text-cyan-600" />
                      <h3 className={`font-bold ${darkMode ? 'text-slate-100' : 'text-gray-900'}`}>Guideline & Web Intelligence</h3>
                    </div>
                    {expandedSections.web ? <ChevronUp className={darkMode ? 'text-slate-400' : ''} /> : <ChevronDown className={darkMode ? 'text-slate-400' : ''} />}
                  </button>
                  {expandedSections.web && (
                    <div className="p-8 space-y-4">
                      {results.webIntelligence?.recentGuidelines?.map((item, i) => (
                        <div key={i} className={`border rounded-lg p-4 hover:shadow-md transition ${darkMode ? 'border-slate-700 bg-slate-800/50' : 'border-gray-200'}`}>
                          <div className="flex items-start gap-3">
                            <div className="p-2 bg-cyan-100 rounded">
                              <Globe className="w-4 h-4 text-cyan-600" />
                            </div>
                            <div className="flex-1">
                              <p className={`font-semibold ${darkMode ? 'text-slate-200' : 'text-gray-900'}`}>Guideline / News</p>
                              <p className={`text-sm ${darkMode ? 'text-slate-400' : 'text-gray-700'}`}>{item}</p>
                            </div>
                          </div>
                        </div>
                      ))}
                      {(!results.webIntelligence?.recentGuidelines || results.webIntelligence.recentGuidelines.length === 0) && (
                        <p className="text-sm text-slate-500">No web intelligence found.</p>
                      )}
                    </div>
                  )}
                </div>

                {/* Recommendation */}
                <div className={`rounded-xl shadow-md border p-8 ${darkMode ? 'bg-gradient-to-r from-emerald-900/30 to-green-900/30 border-emerald-800' : 'bg-gradient-to-r from-emerald-50 to-green-50 border-emerald-200'}`}>
                  <div className="flex items-start gap-4 mb-6">
                    <div className={`p-3 rounded-lg ${darkMode ? 'bg-emerald-900/50' : 'bg-emerald-100'}`}>
                      <TrendingUp className="w-6 h-6 text-emerald-600" />
                    </div>
                    <div className="flex-1">
                      <h2 className={`text-2xl font-bold mb-2 ${darkMode ? 'text-white' : 'text-gray-900'}`}>Recommendation & Next Steps</h2>
                      <p className={`text-lg leading-relaxed ${darkMode ? 'text-slate-300' : 'text-gray-700'}`}>
                        {results.recommendation}
                      </p>
                    </div>
                  </div>
                  <button
                    onClick={handleGenerateReport}
                    className="px-6 py-3 bg-emerald-600 text-white font-semibold rounded-lg hover:bg-emerald-700 flex items-center gap-2 transition shadow-lg shadow-emerald-900/20"
                  >
                    <Download className="w-4 h-4" />
                    Generate PDF Report
                  </button>
                </div>

                {/* Chat / Follow-up Floating Bar */}
                <div className={`fixed bottom-0 inset-x-0 border-t backdrop-blur-md p-4 transition-colors z-50 ${darkMode ? 'bg-slate-900/80 border-slate-800' : 'bg-white/80 border-slate-200'}`}>
                  <div className="max-w-4xl mx-auto">
                    {chatHistory.length > 0 && (
                      <div className={`mb-4 max-h-40 overflow-y-auto rounded-lg border p-3 space-y-3 ${darkMode ? 'bg-slate-950 border-slate-800' : 'bg-slate-50 border-slate-200'}`}>
                        {chatHistory.map((msg, i) => (
                          <div key={i} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                            <div className={`max-w-[85%] text-xs py-2 px-3 rounded-lg ${msg.role === 'user' ? 'bg-blue-600 text-white' : (darkMode ? 'bg-slate-800 text-slate-200' : 'bg-white border border-gray-200 text-gray-800')}`}>
                              {msg.content}
                            </div>
                          </div>
                        ))}
                        <div ref={chatEndRef} />
                      </div>
                    )}

                    <div className="relative">
                      <input
                        type="text"
                        value={chatInput}
                        onChange={(e) => setChatInput(e.target.value)}
                        onKeyDown={(e) => e.key === 'Enter' && handleFollowUp()}
                        placeholder="Ask a follow-up question about this report..."
                        className={`w-full pl-4 pr-12 py-3 rounded-xl border outline-none shadow-lg text-sm transition-colors ${darkMode ? 'bg-slate-800 border-slate-700 text-white placeholder-slate-500 focus:border-blue-500' : 'bg-white border-slate-200 text-slate-900 placeholder-slate-400 focus:border-blue-400'}`}
                        disabled={isChatProcessing}
                      />
                      <button
                        onClick={handleFollowUp}
                        disabled={isChatProcessing || !chatInput.trim()}
                        className="absolute right-2 top-2 p-1.5 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:bg-slate-400 transition"
                      >
                        {isChatProcessing ? <Loader2 className="w-4 h-4 animate-spin" /> : <Send className="w-4 h-4" />}
                      </button>
                    </div>
                  </div>
                </div>

              </div>
            ) : (
              // Empty State
              !loading && (
                <div className={`rounded-xl shadow-md border p-16 text-center animate-fadeIn ${darkMode ? 'bg-[#151B2B] border-slate-800' : 'bg-white border-gray-200'}`}>
                  <div className="p-4 bg-blue-50 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                    <Search className="w-8 h-8 text-blue-600" />
                  </div>
                  <h3 className={`text-2xl font-bold mb-2 ${darkMode ? 'text-white' : 'text-gray-900'}`}>Start Your Research</h3>
                  <p className={`max-w-md mx-auto mb-8 ${darkMode ? 'text-slate-400' : 'text-gray-600'}`}>
                    Enter a research query above to analyze repurposing opportunities across clinical trials, market data, patents, and internal knowledge.
                  </p>

                  {/* Example Chips */}
                  <div className="flex flex-wrap justify-center gap-2 max-w-2xl mx-auto">
                    {EXAMPLE_SCENARIOS.map((s, i) => (
                      <button
                        key={i}
                        onClick={() => handleSearch(s.prompt)}
                        className={`px-3 py-1.5 rounded-full text-xs font-medium border transition-colors ${darkMode ? 'bg-slate-800 border-slate-700 text-slate-300 hover:text-blue-400 hover:border-blue-500' : 'bg-slate-100 border-slate-200 text-slate-600 hover:text-blue-600 hover:bg-blue-50'}`}
                      >
                        {s.title}
                      </button>
                    ))}
                  </div>
                </div>
              )
            )}
          </>
        )}
      </main>

      {/* Logs Overlay (Optional) */}
      {logs.length > 0 && loading && (
        <div className="fixed bottom-4 right-4 w-80 bg-[#151B2B] border border-slate-800 rounded-lg shadow-2xl p-4 z-50 animate-slideIn">
          <div className="flex items-center justify-between mb-2">
            <h4 className="text-xs font-bold text-slate-400 uppercase">Live Agent Activity</h4>
            <Loader2 className="w-3 h-3 animate-spin text-blue-500" />
          </div>
          <div className="h-40 overflow-y-auto text-[10px] font-mono space-y-1.5">
            {logs.map(log => (
              <div key={log.id} className={log.status === 'error' ? 'text-red-400' : 'text-slate-300'}>
                <span className="text-blue-500 font-semibold">[{log.agentName}]</span> {log.message}
              </div>
            ))}
            <div ref={logsEndRef} />
          </div>
        </div>
      )}

    </div>
  );
}
