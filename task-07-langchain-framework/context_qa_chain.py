from typing import Callable, List


def build_context(documents: List[str]) -> str:
    return "\n\n".join(documents)


def build_prompt(question: str, context: str) -> str:
    return f"""
Reference Context:
{context}

Question:
{question}

Answer using the reference context:
"""


def context_qa_chain(
    question: str,
    retriever: Callable[[str], List[str]],
    model: Callable[[str], str],
) -> str:
    documents = retriever(question)

    context = build_context(documents)

    prompt = build_prompt(question, context)

    result = model(prompt)

    return str(result).strip()
