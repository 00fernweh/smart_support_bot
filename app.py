import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from transformers import pipeline

# Titel der Anwendung
st.title("🤖 Smart Support Bot (DE)")

# FAQ-Daten aus Datei laden
with open("faq_data.txt", "r", encoding="latin-1") as f:
    raw_data = f.read().strip().split("\n\n")

# Listen für Fragen und Antworten vorbereiten
questions, answers = [], []
for block in raw_data:
    lines = block.strip().split("\n")
    if len(lines) == 2:
        q = lines[0].replace("Frage: ", "").strip()
        a = lines[1].replace("Antwort: ", "").strip()
        questions.append(q)
        answers.append(a)

# Einbettungsmodell laden
model = SentenceTransformer("distiluse-base-multilingual-cased-v1")

# Vektor-Repräsentationen für die Fragen berechnen
embeddings = model.encode(questions)

# FAISS Index erstellen und Einbettungen hinzufügen
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Texteingabe vom Benutzer
user_input = st.text_input("Bitte geben Sie Ihre Frage ein:")

# Aehnlichste Antwort anzeigen
if user_input:
    query_vec = model.encode([user_input])
    D, I = index.search(np.array(query_vec), k=1)

    # LLM für natürlichere Antwort
    summarizer = pipeline("text2text-generation", model="t5-small", tokenizer="t5-small")

    # Rohantwort (aus FAISS)
    rohantwort = answers[I[0][0]]

    # Kombiniere Nutzerfrage + Rohantwort als Kontext
    input_text = f"summarize: Frage: {user_input}. Antwort: {rohantwort}"

    # LLM generiert elegant formulierte Antwort
    st.markdown("**Antwort (mit LLM optimiert):**")
    antwort_llm = summarizer(input_text, max_length=60, do_sample=False)[0]["generated_text"]
    st.success(antwort_llm)

