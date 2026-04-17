from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import FakeEmbeddings

def create_vectorstore(chunks):
    embeddings = FakeEmbeddings(size=384)  # lightweight, no torch required
    db = Chroma.from_documents(chunks, embeddings)
    return db