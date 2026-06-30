from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    LLM_MODEL : str = "gpt-5.4-mini"
    VECTORSTORE_PATH : str = "vectorstore/chroma"

    class Config:
        env_file = ".env"

settings = Settings()