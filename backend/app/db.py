import psycopg2
from sentence_transformers import SentenceTransformer
from app.config import DATABASE_URL

model = SentenceTransformer('all-MiniLM-L6-v2')

def conn():
    return psycopg2.connect(DATABASE_URL)

def create_db():
    c = conn()
    cur = c.cursor()

    cur.execute('CREATE EXTENSION IF NOT EXISTS vector;')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS data (
        id SERIAL PRIMARY KEY,
        content TEXT UNIQUE,
        embedding VECTOR(384)
    );
    ''')

    c.commit()
    cur.close()
    c.close()

def insert_data(text):
    c = conn()
    cur = c.cursor()

    embedding = model.encode(text, normalize_embeddings=True).tolist()

    cur.execute('''
    INSERT INTO data (content, embedding)
    VALUES (%s, %s)
    ON CONFLICT (content) DO NOTHING
    ''', (text, embedding))

    c.commit()
    cur.close()
    c.close()

def seed_data():
    docs = [
        "Transformer architecture is the foundation of modern large language models, using self-attention mechanisms to weigh the relevance of every token in a sequence against every other token simultaneously, allowing the model to capture long-range dependencies in text far more effectively than previous recurrent approaches.",
        "Tokenization is the process of breaking raw text into smaller units called tokens before feeding it into a language model, where each token is mapped to a unique integer ID and then converted to an embedding vector that the model can process mathematically.",
        "Fine-tuning is a training technique where a pre-trained foundation model is further trained on a smaller domain-specific dataset, allowing it to adapt its weights to specialized tasks like medical diagnosis, legal reasoning, or code generation without training from scratch.",
        "Prompt engineering is the practice of carefully crafting the input text given to a language model to elicit more accurate, structured, or useful responses, encompassing techniques like few-shot examples, chain-of-thought instructions, and role assignment.",
        "Attention mechanisms allow neural networks to dynamically focus on the most relevant parts of an input sequence when producing each output token, assigning learned weights to different positions so the model prioritizes contextually important information over irrelevant noise.",
        "Quantization is a model compression technique that reduces the numerical precision of a model's weights from 32-bit floats down to 8-bit integers or lower, dramatically shrinking memory requirements and speeding up inference with minimal impact on output quality.",
        "Reinforcement Learning from Human Feedback (RLHF) is a training methodology where a reward model is trained on human preference data to score outputs, and the language model is then optimized using reinforcement learning to produce responses that humans rate more highly.",
        "Context windows define the maximum number of tokens a language model can process in a single forward pass, limiting how much text the model can attend to at once, which directly affects its ability to reason over long documents or maintain coherence in extended conversations.",
        "Retrieval-Augmented Generation (RAG) is a technique that enhances LLM responses by first retrieving relevant documents from a knowledge base using vector similarity search, then injecting that context into the prompt so the model generates more accurate and grounded answers rather than relying solely on its parametric memory.",
        "LangChain is a Python and JavaScript framework that simplifies building applications powered by language models by providing modular abstractions for chains, prompts, memory, tools, and retrievers, allowing developers to compose complex LLM pipelines without reinventing low-level integrations.",
        "LangGraph is an extension of LangChain that models multi-agent workflows as directed graphs, where each node represents an agent or processing function and edges define conditional transitions between them, enabling stateful, cyclical, and parallelizable agentic pipelines.",
        "Vector databases are specialized storage systems designed to efficiently index and query high-dimensional embedding vectors using approximate nearest neighbor algorithms like HNSW or IVFFlat, enabling fast semantic search across millions of documents at scale.",
        "Semantic chunking is a document preprocessing strategy for RAG pipelines that splits text into segments based on meaning and topic boundaries rather than fixed character counts, preserving contextual coherence so retrieved chunks are more useful to the language model.",
        "Agent tool use refers to the ability of a language model to call external functions, APIs, or services during inference by generating structured tool invocation requests, allowing it to retrieve live data, run code, query databases, or interact with the real world beyond its training knowledge.",
        "Memory in agentic systems refers to mechanisms that allow agents to persist and recall information across multiple interactions, ranging from short-term in-context storage within the prompt to long-term external storage in vector databases or key-value stores that can be retrieved on demand.",
        "Ollama is a tool that allows developers to download and run large language models like Llama 3 locally on their own hardware, exposing a simple HTTP API compatible with OpenAI's interface so it can serve as a fully local and private alternative to cloud-hosted model providers."
    ]

    for doc in docs:
        insert_data(doc)