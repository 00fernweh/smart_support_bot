from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Datendatei lesen
with open("faq_data.txt", "r", encoding="latin-1") as f:
    raw_data = f.read().strip().split("\n\n")

questions = []
answers = []

# Fragen und Antworten sind getrennt
for block in raw_data:
    lines = block.strip().split("\n")
    if len(lines) == 2:
        q = lines[0].replace("Frage: ", "").strip()
        a = lines[1].replace("Antwort: ", "").strip()
        questions.append(q)
        answers.append(a)

# Embedding Modell
model = SentenceTransformer("distiluse-base-multilingual-cased-v1")

# Erstellt Vektoren
embeddings = model.encode(questions)

# Erstellt FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Abfrageschleife
print("Fragebot gestartet. Schreibe 'exit', um zu beenden.")
while True:
    user_input = input("\nIhre Frage: ")
    if user_input.lower() == "exit":
        break

    query_embedding = model.encode([user_input])
    D, I = index.search(np.array(query_embedding), k=1)

    best_match = answers[I[0][0]]
    print("\nAntwort:", best_match)
