# 📘 ThinkTank AI

**AI-powered research assistant.**

---

## 🚀 Overview
ThinkTank AI is an interactive research assistant that helps you upload academic PDFs, analyze them, and query their content with detailed answers.  
It combines **Streamlit** for a sleek Copilot-style UI, **LangChain** for document handling, **ChromaDB** for vector storage, and **HuggingFace FLAN-T5** for natural language Q&A.

---

## ✨ Features
- 📂 **Upload multiple PDFs** — handle research papers, theses, or notes.
- 🔎 **Automatic text chunking** — split documents into manageable sections.
- 🧠 **Embeddings + ChromaDB** — semantic search with HuggingFace sentence transformers.
- 💬 **Interactive Q&A** — ask questions and get detailed answers.
- 🎨 **Copilot-style UI** — gradient cards, sidebar navigation, quick prompts, and send button.
- 📑 **Session history** — sidebar lists all asked questions for easy navigation.

---

## 📂 Project Structure
ThinkTankAI/
├── app.py                  # Streamlit frontend (UI)
├── backend/
│   ├── pdf_parser.py       # PDF → text extraction
│   ├── embeddings.py       # Embedding + ChromaDB logic
│   └── qa_engine.py        # HuggingFace Q&A pipeline
├── requirements.txt        # Dependencies
├── README.md               # Project overview
├── screenshots/            # UI captures
└── architecture-diagram.png


---

## 🛠 Setup

Clone the repo and install dependencies:

```bash
git clone https://github.com/UmerQureshiiii-svg/ThinkTankAI.git
cd ThinkTankAI
pip install -r requirements.txt
streamlit run app.py
