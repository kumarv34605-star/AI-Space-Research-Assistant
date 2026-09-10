import { createFileRoute } from "@tanstack/react-router";
import { useResearchQuery } from "@/hooks/use-research-query";
import { StatusBar } from "@/components/research/status-bar";
import { MissionHeader } from "@/components/research/mission-header";
import { QuestionForm } from "@/components/research/question-form";
import { AnswerSection } from "@/components/research/answer-section";
import { SourcesSection } from "@/components/research/sources-section";
import {
  EmptyState,
  LoadingState,
  ErrorAlert,
} from "@/components/research/status-states";

const DESCRIPTION =
  "A mission-control style research terminal for the NASA Systems Engineering Handbook, returning grounded answers with source-page citations.";

export const Route = createFileRoute("/")({
  head: () => ({
    meta: [
      { title: "AI Space Research Assistant — NASA Research Terminal" },
      { name: "description", content: DESCRIPTION },
      {
        property: "og:title",
        content: "AI Space Research Assistant — NASA Research Terminal",
      },
      { property: "og:description", content: DESCRIPTION },
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
    ],
  }),
  component: ResearchAssistantPage,
});

function ResearchAssistantPage() {
  const { question, answer, sources, isLoading, error, requestStatus, askQuestion } =
    useResearchQuery();

  return (
    <div className="crt-overlay min-h-screen bg-background">
      <div className="grid-field min-h-screen">
        <StatusBar />

        <main className="mx-auto max-w-4xl px-4 py-12 sm:px-6 sm:py-16 lg:py-20">
          <MissionHeader />

          <div className="mt-8 sm:mt-10">
            <QuestionForm onAsk={askQuestion} isLoading={isLoading} />
          </div>

          <div className="mt-8 space-y-4 sm:mt-10">
            {isLoading && <LoadingState status={requestStatus} />}
            {!isLoading && error && <ErrorAlert message={error} />}
            {!isLoading && !error && !answer && <EmptyState />}
            {!isLoading && !error && answer && (
              <>
                <AnswerSection question={question} answer={answer} />
                <SourcesSection sources={sources} />
              </>
            )}
          </div>
        </main>

        <footer className="border-t border-border">
          <div className="mx-auto flex max-w-4xl flex-col gap-1 px-4 py-6 font-mono text-[10px] tracking-[0.18em] text-muted-foreground sm:flex-row sm:items-center sm:justify-between sm:px-6">
            <span>END OF TRANSMISSION</span>
            <span className="text-amber-dim">LOCAL RETRIEVAL // NO EXTERNAL UPLINK</span>
          </div>
        </footer>
      </div>
    </div>
  );
}
