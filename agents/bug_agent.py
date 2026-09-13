from services.gemini_service import ask_gemini


def review_for_bugs(code):
    prompt = f"""
You are a bug detection agent.

Analyze this Python code:

{code}

Find possible bugs or logical errors.

Explain:
1. What the bug is
2. Where it occurs
3. How to fix it

If there are no obvious bugs, say:
"No obvious bugs found."
"""

    return ask_gemini(prompt)
