from services.gemini_service import ask_gemini


def review_for_performance(code):
    prompt = f"""
You are a performance optimization agent.

Analyze this Python code:

{code}

Find performance problems such as:
- Unnecessary loops
- Inefficient algorithms
- Repeated calculations
- Poor data-structure choices

For each issue, explain the problem and a better approach.

If there are no obvious performance issues, say:
"No obvious performance issues found."
"""

    return ask_gemini(prompt)