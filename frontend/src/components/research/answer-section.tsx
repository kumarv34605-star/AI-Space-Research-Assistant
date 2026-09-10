interface AnswerSectionProps {
  question: string;
  answer: string;
}

export function AnswerSection({ question, answer }: AnswerSectionProps) {
  const paragraphs = answer.split("\n").filter((p) => p.trim().length > 0);

  return (
    <section className="panel animate-response rounded-md">
      <div className="flex items-center justify-between border-b border-border px-4 py-2 font-mono text-[10px] tracking-[0.2em] text-amber sm:px-5 sm:text-[11px]">
        <span>MISSION RESPONSE</span>
        <span className="flex items-center gap-2 text-signal">
          <span
            aria-hidden="true"
            className="inline-block h-1.5 w-1.5 rounded-full bg-signal"
          />
          RESPONSE READY
        </span>
      </div>

      <div className="px-4 py-5 sm:px-6 sm:py-7">
        <p className="font-mono text-[11px] leading-relaxed tracking-[0.08em] text-muted-foreground">
          <span className="text-amber-dim">QUERY // </span>
          {question}
        </p>

        <div className="mt-5 space-y-4 border-l-2 border-amber/40 pl-4 sm:pl-6">
          {paragraphs.map((paragraph, index) => (
            <p
              key={index}
              className="animate-rise text-[15px] leading-7 text-foreground sm:text-base sm:leading-8"
              style={{ animationDelay: `${index * 60}ms` }}
            >
              {paragraph}
            </p>
          ))}
        </div>
      </div>
    </section>
  );
}
