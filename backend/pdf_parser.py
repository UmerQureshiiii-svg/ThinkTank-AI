# ---------------- backend/pdf_parser.py ----------------
from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file):
    """Load PDF into LangChain Document objects."""
    loader = PyPDFLoader(file)
    documents = loader.load()
    return documents
