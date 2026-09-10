import type { Source } from "@/components/research/types";

interface SourcesSectionProps {
  sources: Source[];
}

export function SourcesSection({ sources }: SourcesSectionProps) {
  if (!sources.length) return null;

  return (
    <section className="panel rounded-md">
      <div className="flex items-center justify-between border-b border-border px-4 py-2 font-mono text-[10px] tracking-[0.2em] text-amber sm:px-5 sm:text-[11px]">
        <span>SOURCE MATERIAL</span>
        <span className="text-amber-dim">{sources.length} REFERENCE(S)</span>
      </div>

      <ul className="divide-y divide-border">
        {sources.map((source, index) => (
          <li
            key={`${source.source}-${source.page}-${index}`}
            className="animate-rise group grid gap-3 bg-background/35 p-4 transition-colors hover:bg-amber/5 sm:grid-cols-[6.5rem_1fr_auto] sm:items-center sm:gap-5 sm:px-5"
            style={{ animationDelay: `${index * 90}ms` }}
          >
            <p className="font-mono text-[10px] tracking-[0.18em] text-amber-dim">
              RECORD<br />DOC-{String(index + 1).padStart(2, "0")}
            </p>
            <p className="min-w-0 break-words font-mono text-xs font-medium uppercase leading-relaxed tracking-[0.08em] text-foreground sm:text-sm">
              {source.source.replace(/\.pdf$/i, "").replace(/[_-]+/g, " ")}
            </p>
            <p className="w-fit rounded-sm border border-amber/50 bg-amber/10 px-3 py-2 font-mono text-xs font-semibold tracking-[0.16em] text-amber">
              PAGE {source.page}
            </p>
          </li>
        ))}
      </ul>
    </section>
  );
}
