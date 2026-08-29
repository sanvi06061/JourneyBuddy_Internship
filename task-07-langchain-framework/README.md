# LangChain Dynamic Context-Augmented QA Chain

The chain accepts a dynamic user question, retrieves relevant reference material, inserts that context into a prompt, and produces an answer.

## Pipeline

Question
   ↓
Retriever
   ↓
Retrieved Context
   ↓
Prompt Template
   ↓
Language Model
   ↓
Answer

## Dynamic Inputs

The chain should support:

- user question
- retrieved context
- optional conversation history
- system instructions

## Retrieval Injection Point

Retrieved documents are injected into the prompt immediately before the model invocation.

## Parsing

The final model output is converted into a clean string response before being returned to the application.
