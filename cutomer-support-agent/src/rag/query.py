from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from ..config.settings import settings
from langchain_core.documents import Document

embeddings = HuggingFaceEmbeddings(
    model_name=settings.EMBEDDING_MODEL
)

vectorstore = Chroma(
    persist_directory=settings.VECTORSTORE_PATH,
    embedding_function=embeddings
)

vector_retreiver = vectorstore.as_retriever(
    search_kwargs={"k": 6}
)


data = vectorstore.get()

print("========== DEBUG ==========")
print(data.keys())
print("Number of docs:", len(data["documents"]))
print("===========================")

docs = [
    Document(
        page_content=text,
        metadata = meta
    ) for text, meta in zip(
        data["documents"],
        data["metadatas"]
    )
]
bm25_retriever = BM25Retriever.from_documents(docs)

bm25_retriever.k = 6


hybrid_retriever = EnsembleRetriever(
    retrievers=[vector_retreiver, bm25_retriever],
    weights=[0.7, 0.3]
)

llm = ChatOpenAI(
    model=settings.LLM_MODEL,
    temperature=0.3
)

prompt = ChatPromptTemplate.from_template(
    """
    You are a professional University Customer Support Agent.

    Context:
    {Context}

    Question: {question}

    Rules:
        - Give Answer only from the given context
        - Use formal and professional tone
        - If answer is not in the given context, say "I don't have enough information to answer this question."
        - Don't use extra knowledge
        - Clean, polite and structured response only.
    
    """
)

def format_docs (docs):
    return "\n\n".join(document.page_content for document in docs)

rag_chain = (
        {
            "Context": hybrid_retriever | format_docs,
            "question": RunnablePassthrough()
        } | prompt | llm | StrOutputParser()
    )

    
def ask_question(question: str):
    print("Thinking....")
    response = rag_chain.invoke(question)
    return response
    

    
    


