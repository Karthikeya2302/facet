"use client";

import { useEffect, useState, useRef } from "react";
import { useRouter } from "next/navigation";
import {
  Crown,
  Users,
  Briefcase,
  User,
  LogOut,
  Lock,
  Send,
  Search,
  CheckCircle2,
  XCircle,
  Loader2,
  Database,
  Shield,
  Sparkles,
  FileCheck,
  Wrench,
  Zap,
} from "lucide-react";
import {
  roles,
  RoleId,
  AgentState,
  initialAgents,
  SuggestedChip,
} from "@/lib/roles";
import { streamQuery } from "@/lib/sse";

type MessageType = "user" | "assistant" | "access-denied";

interface Message {
  id: string;
  type: MessageType;
  content: string;
  restrictedLevel?: string;
}

type CacheStatus = "hit" | "miss" | "write" | null;

const roleIcons: Record<RoleId, typeof Crown> = {
  ceo: Crown,
  hr: Users,
  manager: Briefcase,
  employee: User,
};

const agentIcons: Record<string, typeof Search> = {
  retrieval: Search,
  generator: Sparkles,
  grader: FileCheck,
  healer: Wrench,
  access: Shield,
  answer: Sparkles,
};

function findLastIdx<T>(arr: T[], pred: (x: T) => boolean): number {
  for (let i = arr.length - 1; i >= 0; i--) {
    if (pred(arr[i])) return i;
  }
  return -1;
}

export default function ChatPage() {
  const router = useRouter();
  const [role, setRole] = useState<RoleId | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [isProcessing, setIsProcessing] = useState(false);
  const [agents, setAgents] = useState<AgentState[]>(initialAgents);
  const [cacheStatus, setCacheStatus] = useState<CacheStatus>(null);
  const [streamError, setStreamError] = useState<string | null>(null);
  const [showInitialChips, setShowInitialChips] = useState(true);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const storedRole = localStorage.getItem("role") as RoleId | null;
    if (!storedRole || !roles[storedRole]) {
      router.push("/");
      return;
    }
    setRole(storedRole);
  }, [router]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleLogout = () => {
    localStorage.removeItem("role");
    router.push("/");
  };

  const handleSubmit = (question: string, _chip?: SuggestedChip) => {
    if (!question.trim() || isProcessing || !role) return;

    setShowInitialChips(false);
    setIsProcessing(true);
    setStreamError(null);

    setMessages((prev) => [
      ...prev,
      { id: Date.now().toString(), type: "user", content: question },
    ]);
    setInput("");

    // reset pipeline tracker
    setAgents([]);
    setCacheStatus(null);

    streamQuery(
      role,
      question,
      (event) => {
        switch (event.type) {
          case "cache_hit":
            setCacheStatus("hit");
            break;

          case "cache_miss":
            setCacheStatus("miss");
            break;

          case "cache_write":
            setCacheStatus("write");
            break;

          case "agent_start":
            setAgents((prev) => [
              ...prev,
              {
                id: event.agent,
                label: event.label,
                description: event.label,
                status: "pending",
              },
            ]);
            break;

          case "agent_done":
            setAgents((prev) => {
              const idx = findLastIdx(prev, (a) => a.id === event.agent);
              if (idx === -1) return prev;
              const next = [...prev];
              next[idx] = { ...next[idx], description: event.label, status: "pending" };
              return next;
            });
            break;

          case "agent_pass":
            setAgents((prev) => {
              const idx = findLastIdx(prev, (a) => a.id === event.agent);
              if (idx === -1) return prev;
              const next = [...prev];
              next[idx] = { ...next[idx], description: event.label, status: "passed" };
              return next;
            });
            break;

          case "agent_fail":
            setAgents((prev) => {
              const idx = findLastIdx(prev, (a) => a.id === event.agent);
              if (idx === -1) return prev;
              const next = [...prev];
              next[idx] = { ...next[idx], description: event.label, status: "failed" };
              return next;
            });
            break;

          case "healer_decision":
            setAgents((prev) => {
              const idx = findLastIdx(prev, (a) => a.id === "healer");
              if (idx === -1) return prev;
              const next = [...prev];
              next[idx] = {
                ...next[idx],
                healerAction: event.action,
                healerReasoning: event.reasoning,
              };
              return next;
            });
            break;

          case "answer":
            setMessages((prev) => [
              ...prev,
              {
                id: Date.now().toString(),
                type: "assistant",
                content: event.text,
              },
            ]);
            break;

          case "access_denied":
            setMessages((prev) => [
              ...prev,
              {
                id: Date.now().toString(),
                type: "access-denied",
                content: `Access denied — content exists at ${event.found_at_role} level`,
                restrictedLevel: event.found_at_role,
              },
            ]);
            break;

          case "no_info":
            setMessages((prev) => [
              ...prev,
              {
                id: Date.now().toString(),
                type: "assistant",
                content: "I couldn't find that information.",
              },
            ]);
            break;

          case "error":
            setStreamError(event.message);
            break;

          default:
            break;
        }
      },
      () => {
        setIsProcessing(false);
      },
      (err) => {
        setStreamError(err instanceof Error ? err.message : "Connection error");
        setIsProcessing(false);
      }
    );
  };

  if (!role) {
    return (
      <main className="min-h-screen flex items-center justify-center bg-zinc-950">
        <Loader2 className="w-6 h-6 text-zinc-500 animate-spin" />
      </main>
    );
  }

  const config = roles[role];
  const RoleIcon = roleIcons[role];

  return (
    <main className="min-h-screen flex flex-col bg-zinc-950">
      {/* Header */}
      <header className="sticky top-0 z-10 flex items-center justify-between px-4 py-3 bg-zinc-900/80 border-b border-zinc-800 backdrop-blur-sm">
        <div className="flex items-center gap-3">
          <div
            className={`p-2 rounded-lg bg-gradient-to-br ${config.gradient}`}
          >
            <RoleIcon className="w-5 h-5 text-white" />
          </div>
          <span className="text-zinc-300 text-sm">
            Logged in as{" "}
            <span
              className={`font-semibold bg-gradient-to-r ${config.gradient} bg-clip-text text-transparent`}
            >
              {config.label}
            </span>
          </span>
        </div>
        <button
          onClick={handleLogout}
          className="flex items-center gap-2 px-3 py-1.5 text-sm text-zinc-400 hover:text-white
            rounded-lg hover:bg-zinc-800 transition-colors"
        >
          <LogOut className="w-4 h-4" />
          Logout
        </button>
      </header>

      {/* Main Content */}
      <div className="flex-1 flex flex-col lg:flex-row">
        {/* Chat Column */}
        <div className="flex-1 flex flex-col min-h-0">
          {/* Role Context */}
          <div className="p-4 border-b border-zinc-800">
            <p className="text-zinc-400 text-sm leading-relaxed">
              {config.context}
            </p>
          </div>

          {/* Suggested Chips */}
          {showInitialChips && (
            <div className="p-4 border-b border-zinc-800">
              <div className="flex flex-wrap gap-2">
                {config.chips.map((chip, index) => (
                  <button
                    key={index}
                    onClick={() => handleSubmit(chip.question, chip)}
                    disabled={isProcessing}
                    className={`inline-flex items-center gap-1.5 px-3 py-1.5 text-sm rounded-full
                      border transition-all duration-200
                      ${
                        chip.locked
                          ? "bg-zinc-800/50 border-zinc-700/50 text-zinc-500 hover:border-red-500/50 hover:text-red-400"
                          : "bg-zinc-800/50 border-zinc-700/50 text-zinc-300 hover:border-zinc-600 hover:bg-zinc-800"
                      }
                      disabled:opacity-50 disabled:cursor-not-allowed`}
                  >
                    {chip.locked && <Lock className="w-3 h-3" />}
                    {chip.question}
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Messages Area */}
          <div className="flex-1 overflow-y-auto p-4 space-y-4">
            {messages.length === 0 && (
              <div className="flex items-center justify-center h-full">
                <p className="text-zinc-600 text-sm">
                  Ask a question to get started...
                </p>
              </div>
            )}

            {messages.map((message) => (
              <div
                key={message.id}
                className={`flex ${message.type === "user" ? "justify-end" : "justify-start"}`}
              >
                <div
                  className={`max-w-[80%] px-4 py-3 rounded-2xl ${
                    message.type === "user"
                      ? "bg-blue-600/20 border border-blue-500/30 text-blue-100"
                      : message.type === "access-denied"
                        ? "bg-red-600/20 border border-red-500/30 text-red-200"
                        : "bg-zinc-800/80 border border-zinc-700/50 text-zinc-200"
                  }`}
                >
                  {message.type === "access-denied" && (
                    <div className="flex items-center gap-2 mb-1">
                      <Lock className="w-4 h-4 text-red-400" />
                      <span className="text-xs font-medium text-red-400">
                        Access Denied
                      </span>
                    </div>
                  )}
                  <p className="text-sm leading-relaxed">{message.content}</p>
                </div>
              </div>
            ))}
            <div ref={messagesEndRef} />
          </div>

          {/* Input Area */}
          <div className="p-4 border-t border-zinc-800">
            <form
              onSubmit={(e) => {
                e.preventDefault();
                handleSubmit(input);
              }}
              className="flex gap-2"
            >
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Ask a question..."
                disabled={isProcessing}
                className="flex-1 px-4 py-2.5 bg-zinc-800/50 border border-zinc-700/50 rounded-xl
                  text-zinc-200 placeholder-zinc-500 text-sm
                  focus:outline-none focus:ring-2 focus:ring-zinc-600 focus:border-transparent
                  disabled:opacity-50"
              />
              <button
                type="submit"
                disabled={isProcessing || !input.trim()}
                className={`px-4 py-2.5 rounded-xl font-medium text-sm transition-all
                  bg-gradient-to-r ${config.gradient} text-white
                  hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed`}
              >
                <Send className="w-4 h-4" />
              </button>
            </form>
            {streamError && (
              <p className="mt-2 text-xs text-red-400">{streamError}</p>
            )}
          </div>
        </div>

        {/* Agent Tracker Column */}
        <div className="w-full lg:w-72 border-t lg:border-t-0 lg:border-l border-zinc-800 bg-zinc-900/50">
          <div className="sticky top-16 p-4">
            <h3 className="text-sm font-semibold text-zinc-300 mb-4 flex items-center gap-2">
              <Database className="w-4 h-4" />
              Live Pipeline
            </h3>

            {/* Cache status pill */}
            {cacheStatus && (
              <div
                className={`mb-3 inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium border ${
                  cacheStatus === "hit"
                    ? "bg-emerald-900/30 text-emerald-400 border-emerald-500/30"
                    : cacheStatus === "write"
                      ? "bg-emerald-900/20 text-emerald-500 border-emerald-500/20"
                      : "bg-zinc-800 text-zinc-400 border-zinc-700/50"
                }`}
              >
                <Zap className="w-3 h-3" />
                {cacheStatus === "hit"
                  ? "Cache hit"
                  : cacheStatus === "write"
                    ? "Cached"
                    : "Cache miss"}
              </div>
            )}

            <div className="space-y-3">
              {agents.map((agent, i) => {
                const AgentIcon = agentIcons[agent.id] || Database;
                return (
                  <div
                    key={`${agent.id}-${i}`}
                    className={`p-3 rounded-lg border transition-all duration-300 ${
                      agent.status === "pending"
                        ? "bg-zinc-800/50 border-zinc-700/50"
                        : agent.status === "passed"
                          ? "bg-emerald-900/20 border-emerald-500/30"
                          : agent.status === "failed"
                            ? "bg-red-900/20 border-red-500/30"
                            : "bg-zinc-800/30 border-zinc-800/50"
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <AgentIcon
                          className={`w-4 h-4 ${
                            agent.status === "passed"
                              ? "text-emerald-400"
                              : agent.status === "failed"
                                ? "text-red-400"
                                : agent.status === "pending"
                                  ? "text-zinc-400"
                                  : "text-zinc-600"
                          }`}
                        />
                        <span
                          className={`text-xs font-medium ${
                            agent.status === "idle"
                              ? "text-zinc-600"
                              : "text-zinc-300"
                          }`}
                        >
                          {agent.label}
                        </span>
                      </div>
                      <div>
                        {agent.status === "pending" && (
                          <Loader2 className="w-4 h-4 text-zinc-400 animate-spin" />
                        )}
                        {agent.status === "passed" && (
                          <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                        )}
                        {agent.status === "failed" && (
                          <XCircle className="w-4 h-4 text-red-400" />
                        )}
                      </div>
                    </div>
                    <p
                      className={`text-xs mt-1 ${
                        agent.status === "idle"
                          ? "text-zinc-700"
                          : "text-zinc-500"
                      }`}
                    >
                      {agent.description}
                    </p>

                    {/* Healer Agent Reasoning */}
                    {agent.id === "healer" && agent.healerAction && (
                      <div className="mt-2 pl-2 border-l-2 border-zinc-700">
                        <p className="text-xs text-zinc-500">
                          Action:{" "}
                          <span className="text-zinc-400">
                            {agent.healerAction}
                          </span>
                        </p>
                        <p className="text-xs text-zinc-600 italic">
                          {agent.healerReasoning}
                        </p>
                      </div>
                    )}
                  </div>
                );
              })}
            </div>

            {!isProcessing && agents.length === 0 && (
              <p className="text-center text-zinc-600 text-xs mt-4">
                Waiting for a query...
              </p>
            )}
          </div>
        </div>
      </div>
    </main>
  );
}
