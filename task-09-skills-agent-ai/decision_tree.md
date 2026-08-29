# Skills Agent AI - Autonomous Decision Tree

## Goal

Resolve a multi-step user request requiring live information and synthesis.

## Decision Process

START
  ↓
Analyze User Request
  ↓
Determine Required Information
  ↓
Do we need external information?
  ├── No → Generate final answer
  │
  └── Yes
       ↓
   Select Tool
       ↓
   Execute Tool
       ↓
   Inspect Result
       ↓
   Is information sufficient?
       ├── No → Select another tool / retry
       │
       └── Yes
            ↓
       Synthesize Results
            ↓
       Validate Answer
            ↓
       Final Response

## Example Tool Selection

User asks for current weather and travel advice.

1. Analyze request.
2. Detect requirement for live weather.
3. Select weather/web tool.
4. Execute lookup.
5. Evaluate weather data.
6. Combine weather with travel constraints.
7. Produce final recommendation.

## Agent Loop

Plan → Act → Observe → Evaluate → Repeat if necessary → Final Answer
