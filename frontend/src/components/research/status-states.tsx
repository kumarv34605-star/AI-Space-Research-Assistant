import * as React from "react";

export function EmptyState() {
  return (
    <section className="panel animate-rise flex flex-col items-center rounded-md px-6 py-14 text-center sm:py-20">
      <div
        aria-hidden="true"
        className="relative flex h-24 w-24 items-center justify-center rounded-full border border-amber/30"
      >
        <div className="absolute inset-3 rounded-full border border-amber/20" />
        <div className="absolute inset-0 animate-blink rounded-full border border-amber/10" />
        <svg
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="1"
          className="h-9 w-9 text-amber"
        >
          <path d="M4 4h10l6 6v10a0 0 0 0 1 0 0H4z" />
          <path d="M14 4v6h6" />
          <path d="M7.5 13.5h7M7.5 17h4.5" />
        </svg>
      </div>
      <h2 className="mt-7 font-mono text-sm tracking-[0.28em] text-amber">
        AWAITING QUERY
      </h2>
      <p className="mt-3 max-w-sm text-sm leading-relaxed text-muted-foreground">
        Enter a question to search the NASA technical archive.
      </p>
    </section>
  );
}

interface LoadingStateProps {
  status: string;
}

export function LoadingState({ status }: LoadingStateProps) {

  return (
    <section
      className="panel animate-rise rounded-md px-6 py-12 sm:py-16"
      aria-live="polite"
    >
      <div className="mx-auto flex max-w-md flex-col items-center text-center">
        <div className="relative h-px w-full overflow-hidden bg-border">
          <div className="animate-sweep absolute inset-y-0 left-0 w-1/4 bg-amber" />
        </div>
        <p key={status} className="mt-7 animate-rise font-mono text-xs tracking-[0.2em] text-amber sm:text-sm">
          {status}
        </p>
        <p className="mt-3 font-mono text-[10px] tracking-[0.2em] text-muted-foreground">
          LINK ACTIVE <span className="animate-blink">▋</span>
        </p>
      </div>
    </section>
  );
}

interface ErrorAlertProps {
  message: string;
}

export function ErrorAlert({ message }: ErrorAlertProps) {
  return (
    <section
      role="alert"
      className="animate-rise rounded-md border border-destructive/50 bg-destructive/10 p-5 sm:p-6"
    >
      <div className="flex items-center gap-3">
        <span
          aria-hidden="true"
          className="h-2 w-2 animate-blink rounded-full bg-destructive"
        />
        <h2 className="font-mono text-xs tracking-[0.24em] text-destructive sm:text-sm">
          QUERY FAILED
        </h2>
      </div>
      <p className="mt-3 text-sm leading-relaxed text-foreground/90">{message}</p>
      <p className="mt-2 font-mono text-[10px] tracking-[0.18em] text-muted-foreground">
        VERIFY LOCAL ARCHIVE LINK AND RETRANSMIT.
      </p>
    </section>
  );
}
