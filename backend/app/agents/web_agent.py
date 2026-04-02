from app.tools.web_search import web_search

def web_agent(state):
    results = web_search(state['query'])

    return {
        **state,
        'web_context': results
    }