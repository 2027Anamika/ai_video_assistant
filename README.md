
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



---

## AI Summary



---

## RAG Chat



---

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
