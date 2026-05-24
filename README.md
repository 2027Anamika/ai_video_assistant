
🚀 Live Demo

[Open Live Demo](https://aivideoassistant-production.up.railway.app)

✨ Features

- 🎙️ Local Whisper transcription
- 🧠 AI-generated meeting summaries
- 💬 Chat with your meeting using RAG
- 🌍 Multi-language support
- 📺 YouTube video analysis
- ⚡ Streamlit interactive UI
- ☁️ Railway cloud deployment

## Project Summary

AI Video Assistant is an AI-powered meeting intelligence platform that can transcribe, summarize, and analyze video/audio content using local Whisper models and Retrieval-Augmented Generation (RAG).  

The system allows users to upload audio/video files or provide YouTube links, automatically generating transcripts, intelligent summaries, and contextual question-answering over meeting content.  

The project integrates:
- OpenAI Whisper for speech-to-text
- LangChain for orchestration
- ChromaDB for vector storage
- RAG pipeline for semantic search and Q&A
- Streamlit for interactive UI
- Railway for cloud deployment

# AI Video Assistant

AI-powered meeting intelligence platform for transcription, summarization, and contextual Q&A using Whisper and RAG.



---

# 🖼️ Screenshots

## Home Page

<img width="1874" height="962" alt="Screenshot 2026-05-23 214554" src="https://github.com/user-attachments/assets/096eaf5a-dc57-4685-b549-356e0009e04f" />


---

## Transcription Output

<img width="1903" height="986" alt="Screenshot 2026-05-24 103548" src="https://github.com/user-attachments/assets/4ff4b15b-a818-4298-9f05-d27cd760f0b7" />


---

## AI Summary

<img width="1874" height="961" alt="Screenshot 2026-05-24 103645" src="https://github.com/user-attachments/assets/bba03908-8799-4237-8000-91420cceb166" />


---

## RAG Chat

<img width="1889" height="973" alt="Screenshot 2026-05-24 103923" src="https://github.com/user-attachments/assets/5fc47310-60e8-43b4-8811-c2318c853e81" />


---<img width="1879" height="930" alt="Screenshot 2026-05-24 103951" src="https://github.com/user-attachments/assets/42cdb758-dfeb-45e3-a346-5bccb4390c79" />


# 🛠️ Tech Stack

- Python
- Streamlit
- OpenAI Whisper
- LangChain
- ChromaDB
- yt-dlp
- FFmpeg
- Railway

---

# 📂 Project Structure

```bash
.
├── app.py
├── requirements.txt
├── runtime.txt
├── packages.txt
├── core/
│   ├── rag_engine.py
│   ├── vector_store.py
│   ├── transcriber.py
│   └── summarizer.py
├── data/
├── temp/
└── README.md
