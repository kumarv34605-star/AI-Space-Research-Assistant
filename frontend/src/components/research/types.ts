export interface Source {
  page: number;
  source: string;
}

export interface ResearchResponse {
  question: string;
  answer: string;
  sources: Source[];
}

export interface ResearchError {
  detail: string;
}

export interface ResearchState {
  question: string;
  answer: string | null;
  sources: Source[];
  isLoading: boolean;
  error: string | null;
}
