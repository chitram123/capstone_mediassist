## MediAssist AI – Multi-Agent Healthcare Assistant

## Project Overview

MediAssist AI is an enterprise-grade, multi-agent Generative AI application designed to assist healthcare professionals by providing intelligent document-based question answering, medical image analysis, and database query capabilities.
The application combines Retrieval-Augmented Generation (RAG), Optical Character Recognition (OCR), Model Context Protocol (MCP), and Large Language Models (LLMs) into a unified multi-agent architecture powered by LangGraph.
The system enables users to upload hospital documents such as policies, guidelines, and reports, ask natural language questions, analyze prescription or medical images, and retrieve structured information from enterprise databases. Responses are generated using relevant context from uploaded documents, ensuring accurate and grounded answers while minimizing hallucinations.
To support enterprise deployment, the application is built using a modular architecture with FastAPI as the backend, Streamlit as the frontend, FAISS as the vector database, and Docker for containerized deployment.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Key Objectives

•	Build an enterprise-ready Multi-Agent AI Assistant.
•	Implement Retrieval-Augmented Generation (RAG) for document intelligence.
•	Perform OCR-based medical image analysis.
•	Integrate enterprise database querying through MCP.
•	Evaluate AI responses using an LLM-as-a-Judge evaluation framework.
•	Provide an interactive dashboard with document statistics and evaluation metrics.
•	Deploy the complete application using Docker containers.

--------------------------------------------------------------------------------------------------------------------------------

## Features

 ## - Document Intelligence (RAG)

* Upload PDF, DOCX, and TXT documents through an intuitive web interface.
* Automatically preprocess, chunk, and index documents using FAISS.
* Generate semantic embeddings using the **all-MiniLM-L6-v2** model.
* Perform Retrieval-Augmented Generation (RAG) for context-aware question answering.
* Display source documents used to generate each response for improved transparency.

 ## - Multi-Agent Architecture

The application uses a LangGraph-based multi-agent workflow to intelligently route user requests to specialized agents:

* **RAG Agent** – Answers questions from uploaded documents.
* **OCR Agent** – Extracts and analyzes text from medical images and prescriptions.
* **MCP Agent** – Retrieves structured information from enterprise databases.
* **Router Agent** – Automatically determines the appropriate agent based on the user's query.

## - Medical Image Analysis

* Upload prescription or medical images.
* Perform Optical Character Recognition (OCR) to extract text.
* Generate AI-powered explanations and summaries from extracted content.

## - Conversational AI

* Interactive chat interface built using Streamlit.
* Maintains conversation history during the user session.
* Provides confidence scores and source references where applicable.

## - Analytics Dashboard

* Displays uploaded document statistics.
* Shows indexed chunk count.
* Presents evaluation metrics including Accuracy, Faithfulness, Groundedness, Hallucination, and Response Time.
* Displays recent evaluation results.
* Provides project and deployment information.

## - LLM Evaluation Framework

* Implements an **LLM-as-a-Judge** evaluation pipeline.
* Measures:

  * Accuracy
  * Faithfulness
  * Groundedness
  * Relevance
  * Completeness
  * Hallucination
  * Overall Score
  * Confidence Score
* Stores evaluation results in CSV format for analysis and reporting.

## - Logging & Monitoring

* Centralized application logging.
* Daily log file generation with timestamped entries.
* Logs user interactions and system events for debugging and monitoring.

## - Dockerized Deployment

* Containerized FastAPI backend.
* Containerized Streamlit frontend.
* Docker Compose orchestration.
* Shared persistent volumes for uploaded documents and FAISS indexes.
* Environment variable configuration using `.env`.

## - REST API Support

* FastAPI-based backend services.
* Interactive Swagger documentation.
* Modular API architecture for easy maintenance and scalability.

  ---------------------------------------------------------------------------------------------------------------------------------------

## Technology Stack

| Category                | Technology                               |
| ----------------------- | ---------------------------------------- |
| Programming Language    | Python 3.10                              |
| Backend Framework       | FastAPI                                  |
| Frontend Framework      | Streamlit                                |
| Multi-Agent Framework   | LangGraph                                |
| LLM                     | Groq (GPT-OSS-120B)                      |
| Embedding Model         | Sentence Transformers (all-MiniLM-L6-v2) |
| Vector Database         | FAISS                                    |
| OCR Engine              | EasyOCR & Tesseract OCR                  |
| Database Connectivity   | PostgreSQL (via MCP)                     |
| Evaluation Framework    | LLM-as-a-Judge                           |
| Containerization        | Docker & Docker Compose                  |
| API Documentation       | Swagger UI (OpenAPI)                     |
| Version Control         | Git & GitHub                             |
| Development Environment | Visual Studio Code                       |

-----------------------------------------------------------------------------------------------------------------------------------------

## Project Structure

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8f89fa68-b98c-4856-972a-495b4f0d91ad" />


------------------------------------------------------------------------------------------------------------------------------------------

## System Architecture

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/46785a12-2c94-4c4e-8b9f-9bc1452878a4" />

                
 -----------------------------------------------------------------------------------------------------------------------------------------

## Installation & Local Setup


  ## - Prerequisites

Ensure the following software is installed:

* Python 3.10+
* Git
* Docker Desktop (optional, for containerized deployment)
* Visual Studio Code (recommended)

 ## - Clone the Repository

```bash
git clone <repository-url>
cd final_capstone_project
```

## - Create Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

## -Install Dependencies

```bash
pip install -r requirements.txt
```

## - Configure Environment Variables

Create a `.env` file and configure the required variables:

```text
GROQ_API_KEY=your_api_key
MODEL=openai/gpt-oss-120b

DB_HOST=...
DB_PORT=...
DB_NAME=...
DB_USER=...
DB_PASSWORD=...
```

## - Run the Backend

```bash
uvicorn app.backend.api.main:app --reload
```

Backend will be available at:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

## - Run the Frontend

Open another terminal and execute:

```bash
streamlit run app/frontend/streamlit_app.py
```

The Streamlit application will be available at:

```
http://localhost:8501
```
---------------------------------------------------------------------------------------------------------------------------------------------------

 ## Docker Deployment

MediAssist AI is fully containerized using Docker and Docker Compose, enabling consistent deployment across development and production environments.

 ## - Prerequisites

Ensure Docker Desktop is installed and running.

Verify the installation:

```bash
docker --version
docker compose version
```

 ## - Build Docker Images

From the project root directory, build the backend and frontend images:

```bash
docker compose build
```

## - Start the Application

Launch both backend and frontend containers:

```bash
docker compose up
```

To run the containers in detached mode:

```bash
docker compose up -d
```

## - Stop the Application

To stop all running containers:

```bash
docker compose down
```

## - Verify Running Containers

Check the status of the containers:

```bash
docker ps
```

Expected containers:

* mediassist_backend
* mediassist_frontend

## - Access the Application

| Service                   | URL                        |
| ------------------------- | -------------------------- |
| Streamlit Frontend        | http://localhost:8501      |
| FastAPI Backend           | http://localhost:8000      |


## - Docker Components

| Component           | Description                                       |
| ------------------- | ------------------------------------------------- |
| Dockerfile.backend  | Builds the FastAPI backend image.                 |
| Dockerfile.frontend | Builds the Streamlit frontend image.              |
| docker-compose.yml  | Orchestrates the backend and frontend containers. |

## - Persistent Volumes

Docker volumes are used to persist application data outside the containers.

| Host Folder           | Mounted Container Path | Purpose                                      |
| --------------------- | ---------------------- | -------------------------------------------- |
| `./data`              | `/app/data`            | Stores uploaded documents and medical images |
| `./vector_store`      | `/app/vector_store`    | Stores FAISS index and chunk metadata        |


This ensures uploaded files, vector indexes remain available even after containers are recreated.

-------------------------------------------------------------------------------------------------------------------------

## API Endpoints

The backend is implemented using **FastAPI** and exposes REST APIs for document processing, conversational AI, image analysis, and health monitoring.

| Method   | Endpoint         | Description                                                               |
| -------- | ---------------- | ------------------------------------------------------------------------- |
| **GET**  | `/health`        | Checks the health status of the application.                              |
| **POST** | `/upload`        | Uploads and indexes documents into the FAISS vector database.             |
| **POST** | `/chat`          | Processes user queries using the Multi-Agent workflow (RAG, OCR, or MCP). |
| **POST** | `/analyze-image` | Uploads and analyzes medical images using OCR and AI.                     |


<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3b6d0397-8d6d-4137-aa0d-0c721e56ab35" />

----------------------------------------------------------------------------------------------------------------------------------------------------

## Future Enhancements

The following enhancements can be incorporated to further improve MediAssist AI:

* Integrate multiple Large Language Models (LLMs) with dynamic model selection.
* Support additional document formats such as Excel, PowerPoint, and scanned PDFs.
* Implement user authentication and role-based access control (RBAC).
* Add multilingual support for document processing and conversations.
* Enable conversation memory for long-running chat sessions.
* Replace the local FAISS vector store with a scalable vector database such as Pinecone or Milvus.
* Implement real-time monitoring, analytics, and alerting using Grafana and Prometheus.
* Enhance the evaluation framework with automated benchmark datasets and continuous model performance monitoring.

-----------------------------------------------------------------------------------------------------------------------------------------------------

## Author

**Chitra Mehendale**

**Project:** MediAssist AI – Multi-Agent Healthcare Assistant

This project was developed as a capstone project to demonstrate the practical application of Generative AI, Retrieval-Augmented Generation (RAG), Multi-Agent Systems, OCR, Model Context Protocol (MCP), FastAPI, Streamlit, Docker, and enterprise AI application development.




