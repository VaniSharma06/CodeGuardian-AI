from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from analyzers.code_analyzer import analyze_code
from agents.bug_agent import review_for_bugs
from agents.security_agent import review_for_security
from agents.performance_agent import review_for_performance
from agents.quality_agent import review_for_quality
from agents.synthesizer import create_final_review


# Create FastAPI application
app = FastAPI(
    title="CodeGuardian AI",
    description="AI-powered multi-agent code review system",
    version="1.0.0"
)


# Allow React frontend to communicate with FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request model
class CodeRequest(BaseModel):
    code: str


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to CodeGuardian AI!"
    }


# Code review endpoint
@app.post("/review")
def review_code(request: CodeRequest):

    # --------------------------------
    # 1. Static Code Analysis
    # --------------------------------
    static_analysis = analyze_code(request.code)

    # --------------------------------
    # 2. Specialized AI Agents
    # --------------------------------
    bug_review = review_for_bugs(request.code)

    security_review = review_for_security(request.code)

    performance_review = review_for_performance(request.code)

    quality_review = review_for_quality(request.code)

    # --------------------------------
    # 3. AI Final Synthesis
    # --------------------------------
    final_review = create_final_review(
        request.code,
        bug_review,
        security_review,
        performance_review,
        quality_review
    )

    # --------------------------------
    # 4. Return Complete Report
    # --------------------------------
    return {
        "status": "success",

        "static_analysis": static_analysis,

        "agents": {
            "bug": bug_review,
            "security": security_review,
            "performance": performance_review,
            "quality": quality_review
        },

        "final_review": final_review
    }