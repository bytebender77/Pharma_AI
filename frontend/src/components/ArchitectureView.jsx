import React from 'react';
import { Network, Database, BrainCircuit, Server, Shield, Globe, FileText, Users } from 'lucide-react';

const ArchitectureView = ({ darkMode }) => {
    const bgColor = darkMode ? 'bg-slate-800' : 'bg-white';
    const borderColor = darkMode ? 'border-slate-700' : 'border-gray-200';
    const textColor = darkMode ? 'text-slate-200' : 'text-gray-800';
    const subTextColor = darkMode ? 'text-slate-400' : 'text-gray-500';

    return (
        <div className={`w-full h-full p-8 flex flex-col items-center justify-center ${textColor}`}>
            <h2 className="text-2xl font-bold mb-8">Agentic Architecture</h2>

            <div className="grid grid-cols-3 gap-12 w-full max-w-5xl relative">
                {/* Layer 1: User Interface */}
                <div className="col-span-3 flex justify-center mb-8">
                    <div className={`p-6 rounded-xl border-2 border-blue-500 ${bgColor} flex flex-col items-center w-64 relative z-10`}>
                        <Users className="w-8 h-8 text-blue-500 mb-2" />
                        <h3 className="font-bold">User Interface</h3>
                        <p className={`text-xs ${subTextColor}`}>React + Tailwind Dashboard</p>
                        <div className="absolute -bottom-12 left-1/2 w-0.5 h-12 bg-blue-500/50"></div>
                    </div>
                </div>

                {/* Layer 2: Orchestration */}
                <div className="col-span-3 flex justify-center mb-8">
                    <div className={`p-6 rounded-xl border-2 border-purple-500 ${bgColor} flex flex-col items-center w-80 relative z-10`}>
                        <BrainCircuit className="w-8 h-8 text-purple-500 mb-2" />
                        <h3 className="font-bold">Master Agent</h3>
                        <p className={`text-xs ${subTextColor}`}>Query Decomposition & Planning</p>
                        <div className="absolute -bottom-12 left-1/2 w-0.5 h-12 bg-purple-500/50"></div>
                    </div>
                </div>

                {/* Layer 3: Worker Agents */}
                <div className="col-span-3 grid grid-cols-4 gap-4">
                    {[
                        { name: "Clinical Agent", icon: FileText, color: "text-emerald-500", border: "border-emerald-500" },
                        { name: "Market Agent", icon: Database, color: "text-orange-500", border: "border-orange-500" },
                        { name: "Patent Agent", icon: Shield, color: "text-indigo-500", border: "border-indigo-500" },
                        { name: "Web Agent", icon: Globe, color: "text-cyan-500", border: "border-cyan-500" }
                    ].map((agent, i) => (
                        <div key={i} className={`p-4 rounded-lg border ${agent.border} ${bgColor} flex flex-col items-center`}>
                            <agent.icon className={`w-6 h-6 ${agent.color} mb-2`} />
                            <h4 className="font-semibold text-sm">{agent.name}</h4>
                        </div>
                    ))}
                </div>

                {/* Layer 4: Data Sources */}
                <div className="col-span-3 mt-8 pt-8 border-t border-dashed border-slate-600">
                    <div className="flex justify-between text-xs text-center opacity-70">
                        <div className="flex-1">ClinicalTrials.gov (Mock)</div>
                        <div className="flex-1">IQVIA / EXIM (Mock)</div>
                        <div className="flex-1">USPTO / Espacenet (Mock)</div>
                        <div className="flex-1">Web / Internal Docs</div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ArchitectureView;
