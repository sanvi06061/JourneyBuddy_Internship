# Pinecone & Vector Database Retrieval Schema

## Document Pipeline

Documents
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embedding Model
    ↓
Vector Database
    ↓
Similarity Search
    ↓
Top-K Relevant Chunks

## Example Metadata

{
    "document_id": "doc-001",
    "title": "FastAPI Authentication",
    "category": "backend",
    "source": "technical_article",
    "chunk_id": 4
}

## Query

A user asks:

"How does authentication work in FastAPI?"

The query is converted into an embedding and compared against stored document vectors.

## Similarity

Cosine similarity can be used to measure semantic closeness:

similarity(A,B) = (A · B) / (||A|| ||B||)

Higher similarity means the vectors are semantically closer.
