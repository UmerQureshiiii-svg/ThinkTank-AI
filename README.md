# 📘 ThinkTank AI

**AI‑Powered Research Assistant** built with **Streamlit**, **LangChain**, **HuggingFace**, and **ChromaDB**.  
ThinkTank AI helps researchers, students, and professionals analyze documents, extract insights, and answer complex queries with intelligent embeddings and LLM‑powered reasoning.

---

## 🚀 Features
- **PDF Parsing**: Upload research papers and instantly parse them with `PyPDFLoader`.
- **Vector Database**: Build embeddings using HuggingFace models and store them in ChromaDB.
- **Question Answering**: Query documents with natural language and get precise answers.
- **Adaptive Workflow**: Modular backend (`pdf_parser.py`, `embeddings.py`, `qa_engine.py`) for scalability.
- **Streamlit UI**: Clean, interactive interface with wide layout and dashboard‑style results.
- **Deployment Ready**: Runs seamlessly on Streamlit Cloud with Conda environment management.

---

## 🛠 Project Structure
ThinkTank-AI/
│
├── app.py                  # Streamlit frontend
├── backend/
│   ├── pdf_parser.py       # PDF loading & parsing
│   ├── embeddings.py       # HuggingFace embeddings + ChromaDB
│   └── qa_engine.py        # Query answering logic
├── screenshots/            # UI screenshots
├── temp_uploads/           # Temporary file storage
├── architecture_diagram.png# System workflow diagram
├── README.md               # Documentation
└── environment.yml         # Conda environment dependencies


---

## ⚙️ Setup & Installation

### Local Setup
```bash
# Clone the repo
git clone https://github.com/UmerQureshiiii-svg/ThinkTank-AI.git
cd ThinkTank-AI

# Create environment
conda env create -f environment.yml
conda activate thinktank-ai

# Run the app
streamlit run app.py
