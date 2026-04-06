import streamlit as st
from rag_pipeline import *
from dotenv import load_dotenv
load_dotenv()


st.set_page_config(page_title="YouTube AI Assistant", layout="wide")

st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.stTextInput input {
    border-radius: 10px;
}
.stButton button {
    background-color: #FF4B4B;
    color: white;
    border-radius: 10px;
    height: 3em;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("YouTube AI Assistant")
st.caption("Ask anything from any YouTube video")

# Chat memory
if "chat" not in st.session_state:
    st.session_state.chat = []

# Inputs
video_link = st.text_input("🔗 Enter YouTube Video Link")
query = st.chat_input("Ask something about the video...")

# Show video
if video_link:
    st.video(video_link)

# Cache transcript + embeddings
@st.cache_resource
def cached_pipeline(video_id):
    data = youtube_transcript(video_id)
    split = chunking(data)
    vector_store = storing_embedding(split, video_id)
    return vector_store

# Handle query
if query and video_link:

    video_id = extract_link(video_link)

    with st.spinner("Processing video... ⏳"):
        vector_store = cached_pipeline(video_id)
        result = cont_retrieval(query, vector_store)
        response = final_llm_Interfare(query, result)

    # Save chat
    st.session_state.chat.append(("user", query))
    st.session_state.chat.append(("bot", response))

# Display chat
for role, msg in st.session_state.chat:
    if role == "user":
        with st.chat_message("user"):
            st.write(msg)
    else:
        with st.chat_message("assistant"):
            st.write(msg)

# Debug view (VERY useful)
with st.expander("Retrieved Context"):
    if video_link and query:
        for i, doc in enumerate(result):
            st.write(f"Chunk {i+1}")
            st.write(doc.page_content[:300] + "...")