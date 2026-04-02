def router_agent(state):
    if state.get('vector_context'):
        return 'synthesis_agent'
    return 'web_agent'