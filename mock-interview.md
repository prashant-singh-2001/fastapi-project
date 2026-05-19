# Mock Interview Coach

AI-powered interview preparation platform that transforms your resume into a personalized mock interview experience.

Built with **Next.js 14**, **FastAPI**, **LLMs**, **PostgreSQL**, and **Redis**.

---

# 🚀 Overview

Mock Interview Coach helps candidates prepare for interviews using AI-generated questions based on their real experience, projects, and technical background.

Instead of generic interview prompts, the platform generates contextual questions like:

> “You mentioned building 9 GHCP agents — walk me through the architecture decisions behind them.”

The system evaluates responses, scores communication quality, and provides improved sample answers for comparison.

---

# 🏗️ System Architecture

```text
Next.js 14+ (App Router, SSR, Streaming UI)
      ↕ REST / Server-Sent Events (Streaming)
FastAPI (Python 3.11+, async, StreamingResponse)
      ↕
LLM APIs (OpenAI GPT-4o / Claude / Ollama)
      ↕
PostgreSQL (profiles, sessions, analytics)
Redis (cache, rate limiting, queues)
```

---

# ✨ Features

## 📄 Resume-Based Interview Generation

- Upload resume (PDF/DOCX)
- Extract skills, projects, and experience
- Generate:
  - Technical questions
  - Behavioral questions
  - System design prompts
  - Follow-up deep dive questions

---

## 🎯 Role-Specific Interviews

Generate interviews for:

- Backend Developer
- Full Stack Engineer
- Data Scientist
- DevOps Engineer
- AI/ML Engineer
- Custom Job Descriptions

---

## 🧠 AI Answer Evaluation

Evaluate answers on:

- Clarity
- STAR format
- Technical depth
- Communication quality
- Confidence
- Completeness

---

## 📊 Performance Dashboard

Track interview improvement over time:

- Session history
- Score analytics
- Weak areas
- Progress tracking
- Replay previous sessions

---

## 🔥 Difficulty Modes

Choose interview intensity:

- Easy
- Medium
- Brutal

Brutal mode includes:

- Aggressive follow-ups
- Architecture challenges
- Edge-case questioning
- Time-pressure prompts

---

## ⚡ Streaming Interview Experience

Real-time AI responses using:

- Server-Sent Events (SSE)
- Streaming UI in Next.js
- Incremental rendering

---

# 🛠️ Tech Stack

## Frontend

- Next.js 14+
- React Server Components
- TypeScript
- Tailwind CSS
- Streaming UI
- Zustand / Context API

## Backend

- FastAPI
- Python 3.11+
- AsyncIO
- Pydantic
- SQLAlchemy
- StreamingResponse

## AI / LLM

- OpenAI GPT-4o
- Anthropic Claude
- Ollama (local model support)

## Database & Infrastructure

- PostgreSQL
- Redis
- Docker
- Nginx (planned)

---

# 📂 Project Structure

```bash
mock-interview-coach/
│
├── frontend/                 # Next.js application
│   ├── app/
│   ├── components/
│   ├── hooks/
│   ├── lib/
│   └── services/
│
├── backend/                  # FastAPI application
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── llm/
│   │   ├── models/
│   │   ├── services/
│   │   └── utils/
│   │
│   ├── requirements.txt
│   └── main.py
│
├── docker/
├── docs/
└── README.md
```

---

# 🔄 Core Workflow

```text
1. User uploads resume
2. Resume parser extracts structured information
3. LLM generates personalized interview questions
4. User answers in chat interface
5. Backend evaluates answers
6. Scores and feedback stored in PostgreSQL
7. Dashboard tracks improvement over time
```

---

# 📡 API Responsibilities

## FastAPI Backend

Responsible for:

- Resume parsing
- Question generation
- Answer evaluation
- Session management
- LLM orchestration
- Streaming responses
- Rate limiting

---

## Next.js Frontend

Responsible for:

- Resume upload UI
- Interview chat interface
- Streaming AI responses
- Dashboard analytics
- Session replay
- Authentication (planned)

---

# ⚙️ Local Development

## Prerequisites

- Node.js 20+
- Python 3.11+
- PostgreSQL
- Redis

---

# 🖥️ Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

---

# ⚙️ Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

# 🔐 Environment Variables

## Frontend

Create `.env.local`

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## Backend

Create `.env`

```env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=

DATABASE_URL=
REDIS_URL=
```

---

# 🧪 Planned Features

- Voice interview mode
- AI interviewer avatars
- Real-time speech confidence analysis
- Company-specific interview packs
- LeetCode-style coding rounds
- Multi-agent interviewers
- Export interview reports as PDF
- Team/company mock interview mode

---

# 📌 MVP Goals

- Resume upload
- AI-generated interview questions
- Streaming interview chat
- Answer evaluation
- Session persistence
- Dashboard analytics

---

# 🤝 Contributing

Contributions, ideas, and feedback are welcome.

```bash
# Fork the repository
# Create a feature branch
# Commit your changes
# Open a pull request
```

---

# 📄 License

MIT License

---

# 💡 Vision

Mock Interview Coach aims to become a personalized AI interview trainer that adapts to each candidate’s experience, communication style, and career goals — making interview preparation realistic, measurable, and deeply personalized.