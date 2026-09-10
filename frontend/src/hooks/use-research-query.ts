import { useState, useCallback } from "react";
import type {
  ResearchResponse,
  ResearchError,
  Source,
} from "@/components/research/types";

const API_URL =
  (import.meta.env["VITE_API_URL"] as string | undefined) ||
  "http://127.0.0.1:8000/ask";

export interface UseResearchQueryReturn {
  question: string;
  answer: string | null;
  sources: Source[];
  isLoading: boolean;
  error: string | null;
  requestStatus: string;
  askQuestion: (question: string) => Promise<void>;
}

const REQUEST_PHASES = [
  "QUERY RECEIVED",
  "SEARCHING DOCUMENT ARCHIVE...",
  "RETRIEVING RELEVANT PASSAGES...",
  "ANALYZING CONTEXT...",
];

export function useResearchQuery(): UseResearchQueryReturn {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState<string | null>(null);
  const [sources, setSources] = useState<Source[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [requestStatus, setRequestStatus] = useState("");

  const askQuestion = useCallback(async (inputQuestion: string) => {
    const trimmed = inputQuestion.trim();
    if (!trimmed) {
      setError("Please enter a question before asking.");
      return;
    }

    setIsLoading(true);
    setError(null);
    setQuestion(trimmed);
    setRequestStatus("QUERY RECEIVED");

    let phaseIndex = 0;
    const phaseTimer = window.setInterval(() => {
      phaseIndex = Math.min(phaseIndex + 1, REQUEST_PHASES.length - 1);
      setRequestStatus(
        REQUEST_PHASES[phaseIndex] ?? "ANALYZING CONTEXT...",
      );
      if (phaseIndex === REQUEST_PHASES.length - 1) {
        window.clearInterval(phaseTimer);
      }
    }, 900);

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: trimmed }),
      });

      if (!response.ok) {
        const errorData = (await response.json().catch(() => ({}))) as ResearchError;
        throw new Error(
          errorData.detail || `Request failed with status ${response.status}`
        );
      }

      const data = (await response.json()) as ResearchResponse;
      setAnswer(data.answer);
      setSources(data.sources || []);
      setRequestStatus("RESPONSE READY");
    } catch (err) {
      const message =
        err instanceof Error ? err.message : "An unexpected error occurred";
      setError(message);
      setAnswer(null);
      setSources([]);
    } finally {
      window.clearInterval(phaseTimer);
      setIsLoading(false);
    }
  }, []);

  return { question, answer, sources, isLoading, error, requestStatus, askQuestion };
}
