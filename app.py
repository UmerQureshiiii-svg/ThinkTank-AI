# ---------------- app.py ----------------
import streamlit as st
import os
from backend.pdf_parser import load_pdf
from backend.embeddings import build_vector_db
from backend.qa_engine import answer_query

st.set_page_config(page_title="ThinkTank AI", layout="wide")

# Global CSS for Copilot-style UI
st.markdown(
    """
    <style>
    .main-header {
        background: linear-gradient(90deg, #4A90E2, #9013FE);
        padding: 20px;
        border-radius: 12px;
        color: white;
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 25px;
    }
    .question-card {
        background: linear-gradient(135deg, #43CBFF, #9708CC);
        padding: 12px;
        border-radius: 10px;
        color: white;
        font-size: 16px;
        margin-bottom: 10px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
    }
    .answer-card {
        background: linear-gradient(135deg, #FF9A8B, #FF6A88, #FF99AC);
        padding: 18px;
        border-radius: 12px;
        color: white;
        font-size: 15px;
        margin-bottom: 20px;
        line-height: 1.5;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.25);
    }
    .send-btn {
        background-color: #4A90E2;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1em;
        border: none;
        cursor: pointer;
    }
    </style>
    <div class="main-header">📘 ThinkTank AI — AI-powered Research Assistant</div>
    """,
    unsafe_allow_html=True
)

# Session state for Q&A feed
if "qa_feed" not in st.session_state:
    st.session_state["qa_feed"] = []

# Upload PDFs
uploaded_files = st.file_uploader("Upload research papers (PDF)", type=["pdf"], accept_multiple_files=True)

db = None
if uploaded_files:
    documents = []
    for file in uploaded_files:
        temp_path = os.path.join("temp_uploads", file.name)
        os.makedirs("temp_uploads", exist_ok=True)
        with open(temp_path, "wb") as f:
            f.write(file.getbuffer())
        docs = load_pdf(temp_path)
        documents.extend(docs)

    st.success(f"✅ Loaded {len(documents)} pages from {len(uploaded_files)} file(s).")
    db = build_vector_db(documents)
    st.success("✅ Vector database ready.")

# Input bar with send button inside a form
with st.form(key="qa_form", clear_on_submit=True):
    col1, col2 = st.columns([8,1])
    with col1:
        query = st.text_input("Ask a research question:", key="user_query")
    with col2:
        send = st.form_submit_button("➤")

if send and query and db:
    answer = answer_query(query, db)
    st.session_state["qa_feed"].append({"question": query, "answer": answer})


# Suggested quick prompts
if db:
    st.markdown("### Suggested questions:")
    suggestions = ["Summarize the abstract", "Explain the methodology", "What are the key findings?", "Limitations of this paper"]
    cols = st.columns(len(suggestions))
    for i, s in enumerate(suggestions):
        if cols[i].button(s, key=f"suggest_{i}"):
            answer = answer_query(s, db)
            st.session_state["qa_feed"].append({"question": s, "answer": answer})

# Display stacked Q&A feed
for i, qa in enumerate(st.session_state["qa_feed"], 1):
    st.markdown(f"<div class='question-card'><b>Q{i}:</b> {qa['question']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='answer-card'>{qa['answer']}</div>", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📑 Questions Asked")
for i, qa in enumerate(st.session_state["qa_feed"], 1):
    if st.sidebar.button(f"Q{i}: {qa['question']}"):
        st.write(f"Jumped to Question {i}: {qa['question']}")
