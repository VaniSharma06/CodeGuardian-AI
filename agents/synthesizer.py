from services.gemini_service import ask_gemini


def create_final_review(code, bug_review, security_review,
                        performance_review, quality_review):

    prompt = f"""
You are the lead AI code reviewer for CodeGuardian AI.

Analyze the following Python code:

{code}

Here are the reports from specialized agents.

BUG AGENT:
{bug_review}

SECURITY AGENT:
{security_review}

PERFORMANCE AGENT:
{performance_review}

QUALITY AGENT:
{quality_review}

Create one concise final code review.

Return ONLY valid JSON in this exact structure:

{{
    "summary": "",
    "severity": "LOW",
    "bugs": [],
    "security": [],
    "performance": [],
    "quality": [],
    "recommendations": []
}}

Severity must be one of:
LOW, MEDIUM, HIGH, CRITICAL

Do not use markdown.
Do not add text outside the JSON.
"""

    return ask_gemini(prompt)