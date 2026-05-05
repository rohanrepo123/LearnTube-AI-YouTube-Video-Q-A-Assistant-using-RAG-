# 🎥 YouTube AI Assistant

An intelligent AI-powered application that allows users to interact with YouTube videos through natural language queries. Instead of manually watching long videos, users can simply ask questions and receive accurate, context-aware answers instantly.

## 🚀 Overview

This project leverages **Retrieval-Augmented Generation (RAG)** using the **LangChain framework** to transform YouTube video transcripts into a searchable knowledge base. It combines transcript extraction, intelligent chunking, vector embeddings, and LLM reasoning to deliver precise, context-aware answers.

## ✨ Features

* 🔗 Extracts transcripts directly from YouTube videos
* 🌍 Supports **multilingual videos** and processes content from any language
* 🔄 Generates **responses in English** for consistency
* 🧠 Built using **LangChain for end-to-end pipeline orchestration**
* 🔍 Semantic search using embeddings + vector database
* 💬 Chat-based interface for interactive querying
* ⚡ Optimized with caching and persistent vector storage
* 🎥 Embedded video player for better understanding

## 🛠️ Tech Stack

* **LangChain** – Core framework for RAG pipeline, chaining, and orchestration
* **Google Gemini API** – LLM for response generation & embeddings
* **ChromaDB** – Vector database for similarity search
* **YouTube Transcript API** – Transcript extraction
* **Streamlit** – User interface

## 🧠 How It Works

1. Extract transcript using YouTube Transcript API
2. Process and split text using LangChain text splitters
3. Generate embeddings using Gemini via LangChain
4. Store embeddings in ChromaDB vector store
5. Retrieve relevant chunks using similarity search
6. Use LangChain prompt + LLM chain to generate final answer

## 🌐 Multilingual Capability

The system is designed to handle **videos in any language**:

* Automatically retrieves available transcripts
* Processes multilingual content
* Produces **final answers in English** for better usability

## 📌 Use Cases

* 📚 Learn faster from long lectures
* 🎓 Understand complex topics quickly
* 💻 Simplify coding tutorials
* 🧾 Extract insights from any video content

## 🔮 Future Scope

* 🌍 Multi-language output support (beyond English)
* 🕒 Timestamp-based navigation (jump to exact moment in video)
* 💬 Persistent chat history across sessions
* 📚 Multi-video querying (knowledge base across videos)
* 🧠 Advanced retrieval optimization (hybrid search, reranking)
* 🌐 Full-stack deployment (FastAPI + React)
* 📱 Mobile-friendly interface

## 🏁 Conclusion

This project demonstrates how **LangChain can be effectively used to build real-world RAG applications**, transforming unstructured video data into an interactive and intelligent learning experience.
