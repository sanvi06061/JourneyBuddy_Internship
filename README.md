# JourneyBuddy Internship Tasks

This repository contains the tasks and projects completed as part of my **JourneyBuddy Internship**.

The repository is organized task-by-task, with each task containing its own source code, documentation, and setup instructions.

## 📂 Repository Structure

```text
JourneyBuddy_Internship/
│
├── task-01-node-middleware/
│   ├── .gitignore
│   ├── README.md
│   ├── package.json
│   ├── package-lock.json
│   └── server.js
│
└── task-02-...
    └── ...
```

## 🚀 Internship Tasks

| Task    | Topic                                    | Status      |
| ------- | ---------------------------------------- | ----------- |
| Task 01 | Node.js Middleware / Request Interceptor | ✅ Completed |
| Task 02 | Coming Soon                              | ⏳ Pending   |
| Task 03 | Coming Soon                              | ⏳ Pending   |

---

# Task 01 — Node.js Middleware Architecture

## 📌 Objective

Design and implement a request pipeline using **Node.js and Express.js**.

The task focuses on creating middleware that acts as an interceptor between the incoming HTTP request and the final route handler.

The middleware captures request telemetry, logs the information to standard output, and forwards the request using `next()`.

## 🛠️ Technologies Used

* Node.js
* Express.js
* JavaScript
* HTTP/REST

## 🔄 Request Flow

```text
Client Request
      │
      ▼
┌──────────────────────┐
│ Request Middleware   │
│ / Interceptor        │
├──────────────────────┤
│ • Timestamp          │
│ • HTTP Method        │
│ • Request URL        │
│ • Request Headers    │
│ • Query Parameters   │
│ • Console Logging    │
└──────────┬───────────┘
           │
         next()
           │
           ▼
┌──────────────────────┐
│ /info Route Handler  │
└──────────┬───────────┘
           │
           ▼
      HTTP Response
           │
           ▼
         Client
```

## ✨ Features

The middleware performs the following operations:

* Captures the exact request timestamp.
* Identifies the HTTP request method.
* Records the requested URL.
* Inspects the User-Agent header.
* Reads incoming query parameters.
* Logs request information to the terminal.
* Uses `next()` to continue the request pipeline.

## 📡 API Endpoint

### GET `/info`

Returns an informational response.

Example:

```text
http://localhost:3000/info
```

Response:

```json
{
  "message": "This is the informational route"
}
```

### GET `/info` with query parameters

Example:

```text
http://localhost:3000/info?topic=node&section=middleware
```

The middleware captures the parameters:

```text
{
  topic: "node",
  section: "middleware"
}
```

## 📝 Example Middleware Output

```text
----- Incoming Request -----
Timestamp: 2026-08-19T16:59:11.921Z
Method: GET
URL: /info?topic=node&section=middleware
User-Agent: Mozilla/5.0 ...
Parameters: { topic: 'node', section: 'middleware' }
```

## 📁 Task Structure

```text
task-01-node-middleware/
│
├── .gitignore
├── README.md
├── package.json
├── package-lock.json
└── server.js
```

`node_modules/` is intentionally excluded from the repository using `.gitignore`.

## ⚙️ Installation

Clone the repository and navigate to the Task 01 directory:

```bash
cd task-01-node-middleware
```

Install the required dependencies:

```bash
npm install
```

## ▶️ Running the Application

Start the server:

```bash
node server.js
```

The application will run at:

```text
http://localhost:3000
```

Open the following URL in a browser:

```text
http://localhost:3000/info
```

You can also test query parameters:

```text
http://localhost:3000/info?topic=node&section=middleware
```

Request information will be displayed in the terminal.

## 🧠 Key Concept

Express middleware provides a mechanism for processing requests before they reach the final route handler.

In this task, the middleware acts as a **request telemetry interceptor**. It collects information about each incoming request, logs the collected metrics, and calls `next()` to allow the request to continue to the `/info` route.

## ✅ Task Status

**Task 01 — Completed**

---

## 👩‍💻 Internship Progress

This repository will be continuously updated as additional internship tasks are completed.

| Task | Description                     | Status      |
| ---- | ------------------------------- | ----------- |
| 01   | Node.js Middleware Architecture | ✅ Completed |
| 02   | —                               | ⏳ Pending   |
| 03   | —                               | ⏳ Pending   |
| 04   | —                               | ⏳ Pending   |

---

## 📄 Author

**Sanvi Rai**

JourneyBuddy Internship — 2026
---

## Task 04 – Docker Containerization

Containerized a FastAPI application using Docker.

### Key Concepts
- Dockerfile
- Docker image
- Docker container
- Port mapping
- Environment variables
- Health endpoint

The container was successfully built and tested locally.

---

## Task 05 – Google Cloud Platform

Designed a Google Cloud Storage architecture with separate public and private resources.

### Key Concepts
- Cloud Storage
- Bucket organization
- IAM
- Least-privilege access
- Public assets
- Private authenticated documents

---

## Task 06 – Pinecone & Vector Database

Implemented a semantic retrieval demonstration using vector embeddings and cosine similarity.

### Key Concepts
- Vector databases
- Embeddings
- Semantic search
- Similarity search
- Metadata
- Top-K retrieval

---

## Task 07 – LangChain Framework

Designed a dynamic context-augmented question-answering chain.

### Pipeline

Question → Retriever → Context → Prompt → Language Model → Answer

### Key Concepts
- Dynamic context
- Retrieval
- Prompt templates
- Context injection
- Answer generation

---

## Task 08 – Google ADK

Designed a state-driven asynchronous client-server interaction flow.

### Key Concepts
- UI events
- Application state
- Async network requests
- Loading state
- Success state
- Error state
- UI re-rendering

---

## Task 09 – Skills Agent AI

Implemented a conceptual autonomous tool-calling agent.

### Agent Loop

Plan → Act → Observe → Evaluate → Repeat → Final Answer

### Key Concepts
- Tool selection
- Tool execution
- Observation
- Evaluation
- Multi-step reasoning
- Response synthesis
