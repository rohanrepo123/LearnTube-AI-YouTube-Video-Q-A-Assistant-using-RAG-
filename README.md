# 🎥 YouTube AI Assistant

An intelligent AI-powered application that allows users to interact with YouTube videos through natural language queries. Instead of manually watching long videos, users can simply ask questions and receive accurate, context-aware answers instantly.

## 🚀 Overview

This project leverages Retrieval-Augmented Generation (RAG) to transform YouTube video transcripts into a searchable knowledge base. By combining transcript extraction, text chunking, vector embeddings, and a large language model, the system delivers precise answers grounded in video content.

## ✨ Features

* 🔗 Extracts transcripts directly from YouTube videos
* 🌍 Supports **multilingual videos** and processes content from any language
* 🔄 Automatically adapts and provides **responses in English** for consistency
* 🧠 Uses embeddings + vector search for accurate context retrieval
* 💬 Interactive chat-based interface for seamless user experience
* ⚡ Fast responses with caching and persistent vector database
* 🎥 Embedded video player for better context understanding

## 🛠️ Tech Stack

* **LangChain** – Pipeline orchestration
* **Google Gemini API** – LLM + Embeddings
* **ChromaDB** – Vector storage
* **YouTube Transcript API** – Transcript extraction
* **Streamlit** – Interactive UI

## 🧠 How It Works

1. Extract video transcript using YouTube Transcript API
2. Split transcript into smaller chunks
3. Convert text into embeddings using Gemini
4. Store embeddings in Chroma vector database
5. Retrieve relevant chunks based on user query
6. Generate accurate answers using LLM with context

## 🌐 Multilingual Capability

The system is designed to work with videos in **any language**.

* It retrieves transcripts regardless of the original language
* Processes them through the pipeline
* Generates responses **in English**, ensuring accessibility and consistency

## 📌 Use Cases

* 📚 Learn concepts quickly from long lectures
* 🎓 Summarize educational videos
* 💻 Understand coding tutorials faster
* 🧾 Extract key insights from any content

## 🔮 Future Scope

* 🌍 Support answers in **multiple output languages** (not just English)
* 🕒 Add **timestamp-based navigation** (jump to exact video moment)
* 💬 Maintain **chat history across sessions**
* 📚 Multi-video knowledge base (query across multiple videos)
* 🧠 Improved semantic search and ranking
* 🌐 Deploy as a scalable web application (FastAPI + React)
* 📱 Mobile-friendly or app-based interface

## 🏁 Conclusion

This project simplifies the way users consume video content by turning passive watching into an interactive learning experience. It demonstrates the power of combining LLMs with retrieval systems to build practical, real-world AI applications.
