# ---------------- backend/qa_engine.py ----------------
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load HuggingFace model once
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

def answer_query(query, db, k=6):
    """Retrieve context from vector DB and generate detailed answer."""
    results = db.similarity_search(query, k=k)
    context = "\n\n".join([res.page_content for res in results]) if results else ""

    prompt = (
        f"You are a research assistant. Read the context and the question carefully.\n\n"
        f"Question: {query}\n\n"
        f"Context:\n{context}\n\n"
        f"Instructions: Provide a detailed explanation in your own words. "
        f"Always give at least 4–6 sentences. Define the concept clearly, explain how it works, "
        f"and expand with reasoning or examples."
    )

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
    outputs = model.generate(**inputs, max_length=600)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer
