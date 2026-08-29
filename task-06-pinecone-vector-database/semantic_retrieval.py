from dataclasses import dataclass
from math import sqrt
from typing import List


@dataclass
class Document:
    text: str
    embedding: List[float]


def cosine_similarity(a: List[float], b: List[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = sqrt(sum(x * x for x in a))
    norm_b = sqrt(sum(x * x for x in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot / (norm_a * norm_b)


def rank_documents(query_embedding, documents):
    ranked = [
        (document, cosine_similarity(query_embedding, document.embedding))
        for document in documents
    ]

    return sorted(ranked, key=lambda item: item[1], reverse=True)


if __name__ == "__main__":
    query = [1.0, 0.0, 0.0]

    documents = [
        Document("FastAPI authentication", [0.9, 0.1, 0.0]),
        Document("Cooking recipes", [0.0, 0.1, 0.9]),
        Document("FastAPI middleware", [0.8, 0.2, 0.0]),
    ]

    results = rank_documents(query, documents)

    for document, score in results:
        print(f"{score:.4f} - {document.text}")
