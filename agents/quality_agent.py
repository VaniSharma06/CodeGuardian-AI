from services.gemini_service import ask_gemini


def review_for_quality(code):
    prompt = f"""
You are a software quality agent.

Analyze this Python code:

{code}

Review:
- Readability
- Naming
- Structure
- Documentation
- Maintainability
- Best practices

Give practical improvements.

If there are no obvious quality issues, say:
"No obvious quality issues found."
"""

    return ask_gemini(prompt)