from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.gemini import Gemini
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")


def get_answer(path, question):
    llm = Gemini(model='models/gemini-1.5-flash')

    documents = SimpleDirectoryReader(path).load_data()
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

    service_context = ServiceContext.from_defaults(
        llm=llm,
        embed_model=embed_model
    )

    index = VectorStoreIndex.from_documents(documents, service_context=service_context)

    query_engine = index.as_query_engine(similarity_top_k=3)

    response = query_engine.query(question)
    return response
