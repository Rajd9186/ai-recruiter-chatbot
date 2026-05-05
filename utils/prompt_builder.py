def build_prompt(context, query):
    return f"""
You are a recruiter assistant chatbot.

Rules:
- Be concise
- Use bullet points
- Highlight achievements
- Do not hallucinate

Context:
{context}

Question:
{query}
"""
