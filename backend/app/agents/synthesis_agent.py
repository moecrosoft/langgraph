from langchain_ollama import ChatOllama

llm = ChatOllama(
    model='llama3',
    base_url='http://ollama:11434'
)

def synthesis_agent(state):
    context = state.get('vector_context',[]) + state.get('web_context',[])

    prompt = f'''
You are a research assistant.

Question:
{state['query']}

Sources:
{context}

Return:
    - clear explanation
    - key insights
    - final summary

Output only the answer.
'''
    
    response = llm.invoke(prompt).content

    return {
        **state,
        'final_answer': response
    }