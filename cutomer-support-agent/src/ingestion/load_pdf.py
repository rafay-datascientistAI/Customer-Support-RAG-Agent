from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from ..config.settings import settings
import os

def load_and_process_pdf(pdf_path : str):

    print("Loading PDF")

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    
    print(f"Loaded {len(documents)} documents")

    print("Splitting documents into chunks")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 750,
        chunk_overlap = 150,
        length_function = len,
        separators = ["\n\n", "\n", ".", " "]
    )
    
    chunks = text_splitter.split_documents(documents)

    print(f"Split into {len(chunks)} chunks")

    print("Creating embeddings")

    embeddings = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)

    print("Creating vectorstore")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=settings.VECTORSTORE_PATH
    )

    print("Vectorstore created successfully")

    return vectorstore

if __name__ == "__main__":
    load_and_process_pdf("data/NexGen_University_Info.pdf")

    print("Done")