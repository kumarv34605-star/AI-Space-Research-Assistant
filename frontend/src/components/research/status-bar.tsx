interface StatusLightProps {
  label: string;
  tone?: "signal" | "amber";
}

function StatusLight({ label, tone = "signal" }: StatusLightProps) {
  return (
    <span className="flex items-center gap-2 whitespace-nowrap">
      <span
        aria-hidden="true"
        className={`animate-blink inline-block h-1.5 w-1.5 rounded-full ${
          tone === "signal" ? "bg-signal" : "bg-amber"
        }`}
      />
      <span className="text-[10px] tracking-[0.18em] text-muted-foreground sm:text-[11px]">
        {label}
      </span>
    </span>
  );
}

export function StatusBar() {
  return (
    <header className="sticky top-0 z-40 border-b border-border bg-background/85 backdrop-blur-sm">
      <div className="mx-auto flex max-w-6xl flex-col gap-2 px-4 py-3 font-mono sm:flex-row sm:items-center sm:justify-between sm:px-6">
        <p className="text-[10px] tracking-[0.22em] text-amber sm:text-[11px]">
          NATIONAL AERONAUTICS <span className="text-amber-dim">//</span> RESEARCH TERMINAL
        </p>
        <div className="flex flex-wrap items-center gap-x-5 gap-y-1">
          <StatusLight label="LOCAL MODEL" />
          <StatusLight label="VECTOR DATABASE" />
          <StatusLight label="SYSTEM READY" />
        </div>
      </div>
    </header>
  );
}
