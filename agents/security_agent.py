from services.gemini_service import ask_gemini


def review_for_security(code):
    prompt = f"""
You are a cybersecurity code review agent.

Analyze this Python code:

{code}

Find potential security vulnerabilities.

Focus on:
1. Dangerous functions or operations
2. Unsafe input handling
3. Injection risks
4. Hardcoded secrets or credentials
5. Other security weaknesses

For every issue, explain:
- What the security problem is
- Where it occurs
- How to fix it

If there are no obvious security issues, say:
"No obvious security issues found."
"""

    return ask_gemini(prompt)