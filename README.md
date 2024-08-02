# FAQ-QnAbot-Llamaindex

<img width="1439" alt="result1" src="https://github.com/user-attachments/assets/fe48f392-f530-4629-adef-d5f7129fa6b0">


## Streamlit QnA app to answer FAQs
- Developed a QnA bot with Gemini-1.5 model capable of answering questions based on information from CSV, Text, and PDFs
- Employed **Llamaindex** to vectorize text embeddings, ensuring efficient retrieval of relevant information via indexing
- Built a query engine and retriever system to extract context based on similarity search to answer questions with the help of LLM

## Project Description:
Developed an advanced question-answering system utilizing state-of-the-art machine learning models and techniques to extract and synthesize information from a corpus of text documents. This project integrated LlamaIndex, Gemini models, and Hugging Face’s embeddings to create a dynamic system capable of understanding and responding to user queries on 6 topics: Amazon Sagemaker, Aadhar card, Air India, HDFC bank, Sevenhills Hospital, and TATA communications. Look into [data](https://github.com/RakeshJV2000/FAQ-QnAbot-Llamaindex/tree/main/data) folder for more details

### Technologies Used:
- Gemini Model: Leveraged the Gemini-1.5-flash model for efficient retrieval-augmented generation, facilitating sophisticated question-answering capabilities.
- Hugging Face Embeddings: Employed BAAI/bge-base-en-v1.5 model to transform text into high-dimensional vector spaces, enabling semantic similarity assessments between documents and queries.
- LlamaIndex: Integrated LlamaIndex for creating and managing a vector-based document index that supports complex retrieval tasks.

### Project Execution:

- Document Processing: Implemented SimpleDirectoryReader for systematic extraction of text data from files, preparing the corpus for indexing and retrieval.
- Vector Embedding: Utilized Hugging Face’s transformer-based embeddings to convert text data into vectors, ensuring that semantic relationships within the corpus were captured and preserved
- Indexing and Retrieval: Constructed a VectorStoreIndex to organize the embedded vectors in a manner optimized for query processing.
- Query Handling: Designed the system to handle natural language queries, processing them through the query engine to identify and retrieve the top three most relevant documents based on vector similarity.
- Response Generation: Synthesized responses from retrieved documents, providing users with precise and contextually relevant information.
