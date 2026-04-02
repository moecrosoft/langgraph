from app.tools.embedder import embed
from app.vector_store import search_memory

def retrieval_agent(state):
    emb = embed(state['query'])
    context = search_memory(emb)

    return {
        **state,
        'vector_context': context
    }