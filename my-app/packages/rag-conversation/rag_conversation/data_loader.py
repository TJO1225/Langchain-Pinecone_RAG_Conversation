from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings

PINECONE_INDEX = "langchain-pinecone-rag-converation"

# Load
loader = WebBaseLoader(
    "https://medium.com/databutton/ai-agent-frameworks-for-full-stack-app-development-and-software-engineering-9cad8cd82678"
)
data = loader.load()

# Split
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)

# Add to vectorDB
vectorstore = PineconeVectorStore.from_documents(
    documents=all_splits, embedding=OpenAIEmbeddings(), index_name=PINECONE_INDEX
)
retriever = vectorstore.as_retriever()
