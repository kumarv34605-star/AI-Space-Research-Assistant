const META = [
  { label: "MISSION", value: "SE-6105" },
  { label: "DOCUMENT", value: "NASA SYSTEMS ENGINEERING HANDBOOK" },
  { label: "MODE", value: "LOCAL RAG" },
];

export function MissionHeader() {
  return (
    <section className="animate-rise">
      <h1 className="text-3xl font-semibold uppercase leading-none tracking-normal text-foreground text-glow sm:text-5xl lg:text-[3.5rem]">
        AI Space
        <br />
        <span className="text-amber">Research Assistant</span>
      </h1>
      <p className="mt-5 max-w-xl text-base leading-relaxed text-muted-foreground">
        Ask questions. Explore systems engineering. Grounded in NASA technical
        documentation.
      </p>

      <dl className="mt-7 grid gap-x-8 gap-y-2 border-t border-border pt-4 font-mono text-[11px] sm:grid-cols-3">
        {META.map((item) => (
          <div key={item.label} className="flex flex-col gap-1">
            <dt className="tracking-[0.2em] text-amber-dim">{item.label} //</dt>
            <dd className="tracking-[0.08em] text-muted-foreground">{item.value}</dd>
          </div>
        ))}
      </dl>
    </section>
  );
}
