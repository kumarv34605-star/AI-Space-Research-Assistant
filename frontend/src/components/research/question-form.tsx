import * as React from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";

interface QuestionFormProps {
  onAsk: (question: string) => void;
  isLoading: boolean;
}

export function QuestionForm({ onAsk, isLoading }: QuestionFormProps) {
  const [value, setValue] = React.useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onAsk(value);
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) {
      e.preventDefault();
      onAsk(value);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="console-panel animate-rise rounded-md">
      <div className="flex items-center justify-between border-b border-amber/30 bg-amber/5 px-4 py-3 font-mono text-[10px] tracking-[0.2em] text-amber sm:px-6 sm:text-[11px]">
        <span className="flex items-center gap-2.5">
          <span aria-hidden="true" className="h-1.5 w-1.5 rounded-full bg-amber" />
          QUERY INPUT
        </span>
        <span className="text-amber-dim">CH-01 / SECURE</span>
      </div>

      <div className="px-4 py-5 sm:px-6 sm:py-7">
        <label htmlFor="question" className="sr-only">
          Question about the NASA Systems Engineering Handbook
        </label>
        <Textarea
          id="question"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="> Enter a question about the NASA Systems Engineering Handbook..."
          className="min-h-[148px] resize-none border-0 bg-transparent p-0 font-mono text-base leading-7 text-foreground shadow-none placeholder:text-muted-foreground/85 focus-visible:ring-0 sm:text-[17px]"
          disabled={isLoading}
        />
      </div>

      <div className="flex flex-col gap-3 border-t border-amber/25 bg-background/25 px-4 py-4 sm:flex-row sm:items-center sm:justify-between sm:px-6">
        <p className="font-mono text-[10px] tracking-[0.16em] text-muted-foreground">
          {isLoading ? "TRANSMITTING…" : "PRESS ⌘/CTRL + ENTER TO TRANSMIT"}
        </p>
        <Button
          type="submit"
          disabled={isLoading || !value.trim()}
          variant="outline"
          className="group h-12 rounded-sm border-amber/70 bg-amber/15 px-6 font-mono text-xs font-semibold tracking-[0.18em] text-amber shadow-none hover:bg-amber/25 hover:text-foreground focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background disabled:border-border disabled:bg-transparent disabled:text-muted-foreground sm:px-7"
        >
          <span
            aria-hidden="true"
            className="h-1.5 w-1.5 rounded-full bg-current opacity-80"
          />
          TRANSMIT QUESTION
        </Button>
      </div>
    </form>
  );
}
