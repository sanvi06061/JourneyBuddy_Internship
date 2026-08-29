SYSTEM_PROMPT = """
You are a helpful technical assistant.

Answer the user's question using the supplied reference context.
If the answer is not present in the context, clearly state that the
available reference material does not contain the answer.
"""

USER_PROMPT = """
Reference Context:
{context}

User Question:
{question}

Answer:
"""
