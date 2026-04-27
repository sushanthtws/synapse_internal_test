# 🚀 AI Skill Repository (Local-first Intelligence System)

A local-first AI-powered skill ingestion and discovery platform that transforms raw Markdown files into structured, tagged, UI-ready skill cards using FastAPI, PostgreSQL, and AI-based normalization.

The system is designed as a foundation for a semantic knowledge marketplace for engineering skills.

---

# 🧠 Core Concept

Raw Markdown → AI Understanding → Structured Skill → Tagged Knowledge Unit → UI Card

Each “skill” becomes a standardized reusable knowledge module.

---

# 🏗️ Architecture Overview
Streamlit UI (Frontend)
│
▼
FastAPI Backend (REST API)
├── /upload-md → AI Skill Normalizer
├── /skills → Skill Repository API
├── /skills/:id → Skill Detail API
│
▼
AI Processing Layer
├── Title extraction
├── Description generation
├── Tag inference
├── Tech detection
├── Domain classification
│
▼
PostgreSQL Database
├── skills
├── tags
├── skill_tags


---

# 📂 Project Structure

skill_repo/
│
├── app/
│ ├── main.py # FastAPI entrypoint
│ ├── ai/
│ │ └── skill_normalizer.py # AI extraction engine
│ ├── db/
│ │ ├── database.py # DB engine + session manager
│ │ ├── models/
│ │ │ ├── skill_model.py
│ │ │ ├── tag_model.py
│ │ │ └── skill_tag_model.py
│ │ └── repositories/
│ │ └── skill_repository.py
│ ├── ingestion/
│ │ ├── ingestion_pipeline.py
│ │ └── folder_scanner.py
│ └── config/
│ └── settings.py
│
├── ui/
│ └── app.py # Streamlit frontend
│
├── data/
│ └── skills/ # Markdown files input
│
├── scripts/
│ └── init_db.py
│
├── tests/
├── requirements.txt
└── README.md


---

# ⚙️ Core Components

## 1. FastAPI Backend

### Responsibilities
- Upload markdown files
- Run AI normalization
- Store structured skills in PostgreSQL
- Maintain tag relationships
- Serve data to UI

### Endpoints

- `POST /upload-md` → Upload & process skill
- `GET /skills` → List all skills
- `GET /skills/{id}` → Skill details

---

## 2. AI Skill Normalizer

Transforms raw markdown into structured skill objects:

### Output Schema
{
"title": "Skill Name",
"description": "Short summary",
"tech": ["React", "FastAPI"],
"tags": ["auth", "backend"],
"domain": "Backend Security",
"verified": true
}

### Capabilities
- Title extraction
- Summary generation
- Tech detection
- Tag inference
- Domain classification

---

## 3. Database Layer

### Tables

#### skills
- id
- title
- summary
- raw_markdown

#### tags
- id
- name

#### skill_tags
- skill_id
- tag_id

---

## 4. Streamlit UI

### Features
- GitHub-style skill cards
- Upload markdown files
- Search skills
- Filter by tags
- Skill detail view
- Voting system (placeholder)

---

# 🔄 Full System Flow

## Step 1: Upload
User uploads `.md` file

## Step 2: API Call
Streamlit → FastAPI `/upload-md`

## Step 3: AI Processing
SkillNormalizer extracts:
- title
- description
- tags
- tech
- domain

## Step 4: Database Storage
- Skill inserted
- Tags created if missing
- Skill-tag mapping stored

## Step 5: Retrieval
Frontend calls `/skills`

## Step 6: UI Rendering
Skills shown as GitHub-style cards

---

# 🖥️ How to Run

## 1. Start PostgreSQL (Docker)
docker run -d
--name skills-db
-e POSTGRES_USER=postgres
-e POSTGRES_PASSWORD=postgres
-e POSTGRES_DB=skills_db
-p 5432:5432 postgres


## 2. Initialize DB
python scripts/init_db.py


## 3. Start Backend
PYTHONPATH=. uvicorn app.main:app --reload --port 8001


## 4. Start UI
streamlit run ui/app.py


## 5. Open App

http://localhost:8501

---

# 📊 What is Completed

## Backend
- FastAPI setup
- Upload pipeline
- Skill storage
- Tag system
- Many-to-many relationships

## AI Layer
- Rule-based SkillNormalizer
- Title extraction
- Description generation
- Tag inference
- Domain classification

## UI Layer
- Streamlit interface
- GitHub-style cards
- Upload system
- Search + filter
- Detail view

## Database
- PostgreSQL schema
- FK constraints working
- Tag normalization

---

# 🚧 What is Pending

## 1. Semantic AI Tagging
Replace rules with embeddings + LLM classification

## 2. Semantic Search
"find skills like auth system"

## 3. Recommendation Engine
"users also used"

## 4. Trending System
votes + usage + recency

## 5. Vector Database
Store embeddings for similarity search

## 6. Knowledge Graph UI
Skill-to-skill relationships

## 7. Advanced UI
- better cards
- badges
- recommendations panel

---

# 🎯 Final Outcome

This system is evolving into:

AI-native engineering knowledge platform where:

- Skills behave like reusable software modules
- AI structures unstructured engineering knowledge
- Developers discover reusable patterns instantly

---

# 🚀 Next Phase

Move into:

Semantic Search + Embedding-based Intelligence Layer