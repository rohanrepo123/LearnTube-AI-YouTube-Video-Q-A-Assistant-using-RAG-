from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from langchain_text_splitters import TextSplitter,CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings,GoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import re
from dotenv import load_dotenv
load_dotenv()
model = GoogleGenerativeAI(model='gemini-2.5-flash')
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
    )
template = PromptTemplate(template="You have the right explaination to the user for the question.\n" \
"{query} from the given context .\n {context} these are the lists of the information from out transcript, if the there is insufficient knowledge from the context simply tell him the info you are talking about not talked in the video"  
 , input_variables=['query','context'])

def extract_link(url):
    pattern = r'(?:youtu\.be/|youtube\.com(?:/watch\?v=|/embed/|/shorts/))([0-9A-Za-z_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None

parser = StrOutputParser()

def youtube_transcript(id):
    api = YouTubeTranscriptApi()
    try:
        # Get all transcripts
        transcript_list = api.list(video_id='fHF22Wxuyw4')

        # Try English manually created
        try:
            transcript = transcript_list.find_manually_created_transcript(['en'])
        except:
            # Try auto English
            try:
                transcript = transcript_list.find_generated_transcript(['en'])
            except:
                # Fallback: ANY language
                transcript = list(transcript_list)[0]

        data = " ".join(x.text for x in transcript.fetch())
        return data
    except Exception as e:
        return f"No transcript available: {str(e)}"
    
def chunking(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=900,chunk_overlap=30)
    return splitter.split_text(text)

def storing_embedding(x,id):
    vector_store = Chroma(
    embedding_function=GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001'),
    persist_directory='my_chroma_youtube_rattlesnake'+id,
    collection_name='transcript1'
    )
    vector_store.add_texts(x)
    return vector_store


def cont_retrieval(Query,vector_store):
    result = vector_store.similarity_search(
    query=Query,
    k=5     #how much similar doc
    )
    return result

def final_llm_Interfare(Query,result):
    result1 =[]
    for i in result:
        result1.append(i.page_content)
    # result1 = 
    chain = template | model | parser
    to_be_presented = chain.invoke({"query":Query,"context":result1})
    return to_be_presented
