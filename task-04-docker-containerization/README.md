# Docker Containerization Demo

This project demonstrates how a web service can be packaged into a Docker container with reproducible runtime dependencies.

## Architecture

Client
  ↓
Docker Container
  ↓
FastAPI Application
  ↓
Port 8000

## Build

docker build -t journeybuddy-docker .

## Run

docker run -p 8000:8000 journeybuddy-docker

## Test

Open:

http://localhost:8000

## Environment Variables

The application accepts configuration through environment variables instead of hardcoding deployment-specific values.
