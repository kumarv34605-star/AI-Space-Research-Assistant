from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rag import answer_question


app = FastAPI(
    title="AI Space Research Assistant",
    description="A local RAG-based assistant for NASA technical documents",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str


class Source(BaseModel):
    page: int
    source: str


class AskResponse(BaseModel):
    question: str
    answer: str
    sources: list[Source]


@app.get("/")
def root():
    return {
        "message": "AI Space Research Assistant API is running"
    }


@app.post(
    "/ask",
    response_model=AskResponse,
    responses={
        400: {
            "description": "Question cannot be empty"
        }
    }
)
def ask_question(request: QuestionRequest):

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    answer, results = answer_question(question)

    sources = []

    seen_sources = set()

    for result in results:

        source_key = (
            result["source"],
            result["page"]
        )

        if source_key in seen_sources:
            continue

        seen_sources.add(source_key)

        sources.append({
            "page": result["page"],
            "source": result["source"]
        })

    return AskResponse(
        question=question,
        answer=answer,
        sources=sources
    )