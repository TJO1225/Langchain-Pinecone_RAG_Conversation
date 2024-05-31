import os
from pinecone import Pinecone
import pinecone

pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

# Connect to your index
index = pinecone.Index(
    "langchain-pinecone-rag-converation",
    host="https://langchain-pinecone-rag-converation-kjdpfzi.svc.gcp-starter.pinecone.io",
)

# Check index statistics
index_stats = index.describe_index_stats()

print(index_stats)

# # Perform a query with a sample vector
# query_results = index.query(vectors=[[0.1, 0.2, 0.3]], top_k=1)

# print(query_results)
