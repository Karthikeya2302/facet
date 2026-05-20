"use client";

import { useRouter } from "next/navigation";
import { Crown, Users, Briefcase, User } from "lucide-react";

const roles = [
  {
    id: "ceo",
    label: "CEO",
    icon: Crown,
    gradient: "from-amber-400 to-orange-500",
    hoverBorder: "hover:border-amber-400/50",
  },
  {
    id: "hr",
    label: "HR",
    icon: Users,
    gradient: "from-pink-400 to-rose-500",
    hoverBorder: "hover:border-pink-400/50",
  },
  {
    id: "manager",
    label: "Manager",
    icon: Briefcase,
    gradient: "from-cyan-400 to-blue-500",
    hoverBorder: "hover:border-cyan-400/50",
  },
  {
    id: "employee",
    label: "Employee",
    icon: User,
    gradient: "from-emerald-400 to-teal-500",
    hoverBorder: "hover:border-emerald-400/50",
  },
];

export default function HomePage() {
  const router = useRouter();

  const handleRoleSelect = (roleId: string) => {
    localStorage.setItem("role", roleId);
    router.push("/chat");
  };

  return (
    <main className="min-h-screen flex flex-col items-center justify-center p-4 bg-zinc-950">
      <div className="w-full max-w-2xl text-center">
        {/* Title */}
        <h1 className="text-6xl font-bold mb-4">
          <span className="bg-gradient-to-r from-violet-400 via-fuchsia-400 to-pink-400 bg-clip-text text-transparent">
            Facet
          </span>
        </h1>

        {/* Subtitle */}
        <p className="text-zinc-400 text-lg mb-12 leading-relaxed italic max-w-xl mx-auto">
          Internal Knowledge Assistant — each role sees a different facet of
          the same knowledge.
        </p>

        {/* Role Grid */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {roles.map((role) => {
            const IconComponent = role.icon;
            return (
              <button
                key={role.id}
                onClick={() => handleRoleSelect(role.id)}
                className={`group flex flex-col items-center justify-center gap-3 p-6 rounded-xl 
                  bg-zinc-900/60 border border-zinc-800 
                  transition-all duration-200 ease-out
                  hover:-translate-y-1 hover:shadow-lg hover:shadow-zinc-900/50
                  ${role.hoverBorder}
                  focus:outline-none focus:ring-2 focus:ring-zinc-500 focus:ring-offset-2 focus:ring-offset-zinc-950`}
              >
                <div
                  className={`p-3 rounded-lg bg-gradient-to-br ${role.gradient} shadow-lg`}
                >
                  <IconComponent className="w-6 h-6 text-white" />
                </div>
                <span
                  className={`font-medium bg-gradient-to-r ${role.gradient} bg-clip-text text-transparent`}
                >
                  {role.label}
                </span>
              </button>
            );
          })}
        </div>
      </div>
    </main>
  );
}
