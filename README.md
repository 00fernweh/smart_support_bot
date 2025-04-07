# 🤖 Smart Support Bot – LLM-basierter FAQ-Chatbot

Ein intelligenter, deutschsprachiger FAQ-Bot, der auf Large Language Models (LLMs) basiert und für technische Supportanfragen entwickelt wurde. Das Projekt simuliert einen realitätsnahen Industriekontext wie z. B. technische Dokumentation bei Siemens.

## 🔍 Projektübersicht

**Smart Support Bot** verwendet vortrainierte Transformer-Modelle zur semantischen Suche und Antwortgenerierung. Die Anwendung bietet eine benutzerfreundliche Streamlit-Oberfläche, um FAQ-Fragen auf Deutsch interaktiv zu stellen.

---

## 💡 Funktionen

- 🧠 Semantische Suche mit `sentence-transformers`
- ✍️ Optional: Generative Antworten mit einem BERT2BERT-Modell (HuggingFace)
- 🌐 Sprache: Deutsch
- 🖥️ Einfache Web-Oberfläche mit Streamlit
- 📄 Verwendung realer FAQ-Dokumentationen (Siemens, PDF-basiert)

---

## 🧱 Verwendete Technologien

- Python 3.11
- [Hugging Face Transformers](https://huggingface.co/)
- [Sentence Transformers](https://www.sbert.net/)
- Streamlit
- Scikit-learn

---

## 🚀 Lokale Ausführung

```bash
git clone https://github.com/00fernweh/smart_support_bot.git
cd smart_support_bot
python -m venv venv
venv\Scripts\activate   # Für Windows
pip install -r requirements.txt
streamlit run app.py
