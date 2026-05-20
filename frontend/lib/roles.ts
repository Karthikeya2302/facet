import { Crown, Users, Briefcase, User, LucideIcon } from "lucide-react";

export type RoleId = "ceo" | "hr" | "manager" | "employee";

export interface SuggestedChip {
  question: string;
  locked: boolean;
}

export interface RoleConfig {
  id: RoleId;
  label: string;
  icon: LucideIcon;
  gradient: string;
  hoverBorder: string;
  context: string;
  chips: SuggestedChip[];
}

export const roles: Record<RoleId, RoleConfig> = {
  ceo: {
    id: "ceo",
    label: "CEO",
    icon: Crown,
    gradient: "from-amber-400 to-orange-500",
    hoverBorder: "hover:border-amber-400/50",
    context:
      "You have full access — board minutes, M&A plans, exec comp, all salary data.",
    chips: [
      { question: "What did the board decide about Project Nightingale?", locked: false },
      { question: "What is the executive compensation structure?", locked: false },
      { question: "Summarize the Q3 board minutes", locked: false },
    ],
  },
  hr: {
    id: "hr",
    label: "HR",
    icon: Users,
    gradient: "from-pink-400 to-rose-500",
    hoverBorder: "hover:border-pink-400/50",
    context:
      "You can see HR docs (salary bands, hiring, performance) and everything below. CEO-only is restricted.",
    chips: [
      { question: "What are the salary bands for senior engineers?", locked: false },
      { question: "What's the Q4 hiring pipeline status?", locked: false },
      { question: "What is Project Nightingale?", locked: true },
    ],
  },
  manager: {
    id: "manager",
    label: "Manager",
    icon: Briefcase,
    gradient: "from-cyan-400 to-blue-500",
    hoverBorder: "hover:border-cyan-400/50",
    context:
      "You can see manager-level docs (budgets, roadmaps) and employee content. HR and CEO is restricted.",
    chips: [
      { question: "What's the Q1 roadmap for the payments team?", locked: false },
      { question: "What's my team's 2025 budget?", locked: false },
      { question: "What are the engineering salary bands?", locked: true },
    ],
  },
  employee: {
    id: "employee",
    label: "Employee",
    icon: User,
    gradient: "from-emerald-400 to-teal-500",
    hoverBorder: "hover:border-emerald-400/50",
    context:
      "You can see general company content — handbook, holiday policy, IT setup, expense policy.",
    chips: [
      { question: "How many vacation days do I get?", locked: false },
      { question: "How do I set up my laptop?", locked: false },
      { question: "What is Project Nightingale?", locked: true },
    ],
  },
};

export type AgentStatus = "pending" | "passed" | "failed" | "idle";

export interface AgentState {
  id: string;
  label: string;
  description: string;
  status: AgentStatus;
  healerAction?: string;
  healerReasoning?: string;
}

export const initialAgents: AgentState[] = [
  { id: "retrieval", label: "Retrieval Agent", description: "Waiting...", status: "idle" },
  { id: "grader", label: "Grader Agent", description: "Waiting...", status: "idle" },
  { id: "healer", label: "Healer Agent", description: "Waiting...", status: "idle" },
  { id: "access", label: "Access Agent", description: "Waiting...", status: "idle" },
  { id: "answer", label: "Answer Generator", description: "Waiting...", status: "idle" },
];
