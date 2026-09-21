# 🎓 AI Study Assistant — Mentora AI

> **Learn Smarter. Study Faster. Understand Better.**

Mentora AI is an **AI-powered study assistant** designed to help students learn more efficiently using artificial intelligence. The platform can generate study notes, summarize documents, answer academic questions, and provide an interactive AI tutor experience.

The project combines **Generative AI, Natural Language Processing, document processing, and modern web technologies** to create a personalized digital learning companion.

---

## 🚀 Features

### 📚 AI Notes Generator

Generate structured study notes from:

* Topics
* Chapters
* Subject names
* Study material
* Uploaded documents

The AI organizes information into easy-to-understand sections, key concepts, and important points.

### 📄 PDF Summarizer

Upload a PDF and automatically generate a concise summary.

**Supported workflow:**

```text
PDF Upload
    ↓
Text Extraction
    ↓
Content Processing
    ↓
AI Analysis
    ↓
Structured Summary
```

Useful for:

* Lecture notes
* Textbooks
* Research papers
* Assignments
* Study materials

### 🤖 AI Chat Tutor

Interact with an AI tutor and ask questions related to your studies.

Example:

```text
Student:
Explain normalization in DBMS with an example.

Mentora AI:
Normalization is a database design technique...
```

The system is designed to provide explanations in a student-friendly format.

### 📝 Question Answering

Students can ask questions and receive AI-generated explanations.

Examples:

* "Explain binary search."
* "What is supervised learning?"
* "Explain Bayes theorem."
* "What is normalization in DBMS?"

### 🎯 Personalized Learning

The platform can be extended to provide personalized learning based on:

* Subject
* Difficulty level
* Learning goals
* Previous questions
* Student progress

### 📊 Study Dashboard

A centralized dashboard can provide:

* Study activity
* Recent questions
* Generated notes
* Uploaded documents
* Learning progress
* Saved resources

---

# 🛠️ Technology Stack

## Frontend

* React.js
* JavaScript
* HTML5
* CSS3
* Tailwind CSS

## Backend

* Python
* FastAPI

## AI / Machine Learning

* OpenAI API
* Natural Language Processing
* Generative AI
* Text summarization
* Retrieval-based question answering

## Database

* Supabase / PostgreSQL

## Authentication

* JWT Authentication
* Firebase Authentication *(optional)*

## Payments

* Stripe / Razorpay *(optional for SaaS version)*

## Development Tools

* Git
* GitHub
* VS Code
* Postman
* npm

## Deployment

* Vercel — Frontend
* Render / Railway — Backend
* Supabase — Database

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │      Student        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   React Frontend    │
                    │    + Tailwind CSS   │
                    └──────────┬──────────┘
                               │
                         REST API / JWT
                               │
                               ▼
                    ┌─────────────────────┐
                    │    FastAPI Backend  │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │  AI Engine  │  │  PostgreSQL │  │ PDF Parser  │
       │ OpenAI API  │  │  / Supabase │  │             │
       └─────────────┘  └─────────────┘  └─────────────┘
```

---

# 📁 Project Structure

```text
ai-study-assistant/
│
├── frontend/
│   ├── public/
│   └── src/
│       ├── components/
│       ├── pages/
│       ├── services/
│       ├── hooks/
│       ├── utils/
│       ├── App.jsx
│       └── main.jsx
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env.example
│
├── uploads/
│
├── docs/
│
├── .gitignore
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-study-assistant.git
```

Navigate into the project:

```bash
cd ai-study-assistant
```

---

# 🔹 Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file inside the backend directory.

```env
OPENAI_API_KEY=your_openai_api_key

DATABASE_URL=your_database_url

JWT_SECRET_KEY=your_secret_key

SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

> ⚠️ Never commit your `.env` file or API keys to GitHub.

---

# ▶️ Run Backend

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🔹 Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will usually be available at:

```text
http://localhost:5173
```

---

# 🔄 Application Workflow

### 1. Student Registration

```text
Student
   ↓
Create Account
   ↓
Authentication
   ↓
Student Dashboard
```

### 2. AI Study Assistant

```text
Student Question
       ↓
Frontend
       ↓
FastAPI API
       ↓
AI Processing
       ↓
OpenAI API
       ↓
Generated Response
       ↓
Student
```

### 3. PDF Summarization

```text
Upload PDF
     ↓
Extract Text
     ↓
Clean / Process Text
     ↓
Send Content to AI
     ↓
Generate Summary
     ↓
Display Summary
```

---

# 🧠 AI Capabilities

Mentora AI can be designed to support multiple AI-powered functions.

| Feature               | AI Capability              |
| --------------------- | -------------------------- |
| AI Tutor              | Conversational AI          |
| Notes Generator       | Text Generation            |
| PDF Summarizer        | Text Summarization         |
| Question Answering    | NLP / LLM                  |
| Quiz Generator        | Generative AI              |
| Flashcards            | Generative AI              |
| Study Planner         | Recommendation             |
| Document Q&A          | Retrieval + LLM            |
| Personalized Learning | User-based recommendations |

---

# 📖 Example Use Cases

### Example 1 — Notes

**Input:**

```text
Generate notes about Machine Learning.
```

**Output:**

```text
Machine Learning

1. Introduction
2. Types of Machine Learning
3. Supervised Learning
4. Unsupervised Learning
5. Reinforcement Learning
6. Applications
7. Advantages and Limitations
```

---

### Example 2 — PDF Summary

**Input:**

```text
Upload: Machine_Learning_Chapter_1.pdf
```

**Output:**

```text
Chapter Summary

• Introduction to Machine Learning
• Types of Machine Learning
• Training and Testing Data
• Model Evaluation
• Common ML Algorithms
```

---

### Example 3 — AI Tutor

```text
Student:
What is overfitting?

Mentora AI:
Overfitting occurs when a machine learning model
learns the training data too closely, including noise
and random patterns, resulting in poor performance
on unseen data.
```

---

# 🔒 Security

The application should follow standard security practices:

* JWT-based authentication
* Password hashing
* Environment variables for secrets
* API authentication
* Input validation
* File type validation
* File size restrictions
* CORS configuration
* Secure database queries
* Protection against unauthorized API access

---

# 📈 Future Improvements

The project can be expanded with advanced features.

### 🎤 Voice AI Tutor

Allow students to communicate with Mentora AI using voice.

### 🧠 AI Quiz Generator

Automatically generate:

* MCQs
* True/False questions
* Short-answer questions
* Difficulty-based questions

### 🃏 AI Flashcards

Generate flashcards automatically from:

* PDFs
* Notes
* Chapters
* Topics

### 📅 AI Study Planner

Generate personalized study schedules based on:

* Subjects
* Exam dates
* Available study time
* Difficulty
* Previous progress

### 📊 Learning Analytics

Track:

* Study time
* Questions asked
* Topics studied
* Quiz performance
* Weak areas
* Learning progress

### 🔎 Document-Based AI

Implement RAG (Retrieval-Augmented Generation) so students can ask questions directly from their uploaded documents.

Possible technologies:

```text
Document
   ↓
Text Extraction
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Database
   ↓
Semantic Search
   ↓
LLM
   ↓
Answer
```

Possible vector databases:

* FAISS
* ChromaDB
* Pinecone
* pgvector

---

# 💼 SaaS Roadmap

Mentora AI can eventually be developed into a complete AI education SaaS platform.

### Phase 1 — MVP

* User authentication
* AI Chat Tutor
* Notes Generator
* PDF Summarizer
* Basic dashboard

### Phase 2 — Learning Tools

* Quiz Generator
* Flashcards
* Study Planner
* Progress tracking

### Phase 3 — Advanced AI

* RAG-based document Q&A
* Personalized recommendations
* Voice assistant
* AI-generated learning paths

### Phase 4 — SaaS

* Free plan
* Premium plan
* Usage limits
* Subscription payments
* Student analytics
* Institution accounts

---

# 🎯 Project Objectives

The main objectives of Mentora AI are:

1. Make learning more accessible through AI.
2. Reduce the time required to understand large study materials.
3. Provide personalized academic assistance.
4. Help students summarize and organize learning resources.
5. Provide an interactive AI tutoring experience.
6. Demonstrate practical applications of Generative AI and NLP.
7. Build a scalable AI-powered education platform.

---

# 🎓 Academic Value

This project demonstrates practical knowledge of:

* Python
* FastAPI
* React.js
* REST APIs
* Database Management
* Authentication
* Natural Language Processing
* Generative AI
* Prompt Engineering
* Document Processing
* Data Processing
* Cloud Deployment
* Full-Stack Development

It can therefore serve as a **B.Tech Data Science / AI portfolio project** as well as a potential SaaS product.

---

# 📊 Future Data Science Integration

As the platform grows, data science can be used to analyze anonymous learning activity and improve personalization.

Potential applications include:

```text
Student Activity
       ↓
Data Collection
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Feature Engineering
       ↓
Machine Learning
       ↓
Personalized Recommendations
```

Possible ML applications:

* Student performance prediction
* Topic difficulty prediction
* Learning recommendation
* Dropout-risk analysis
* Study-time optimization
* Quiz performance prediction

---

# 🤝 Contribution

Contributions are welcome.

```bash
# Fork the repository

# Create a new branch
git checkout -b feature/new-feature

# Make your changes

# Commit
git commit -m "Add new feature"

# Push
git push origin feature/new-feature
```

Then open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

# 👨‍💻 Author

**Ranjeet**

B.Tech Data Science Student
AI & Data Science Enthusiast

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

> **Mentora AI — Your Personal AI Study Companion.**
