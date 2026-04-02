from langgraph.graph import StateGraph, END

from app.state import ResearchState

from app.agents.retrieval_agent import retrieval_agent
from app.agents.web_agent import web_agent
from app.agents.synthesis_agent import synthesis_agent
from app.agents.router_agent import router_agent

graph = StateGraph(ResearchState)

graph.add_node('retrieval_agent', retrieval_agent)
graph.add_node('web_agent', web_agent)
graph.add_node('synthesis_agent', synthesis_agent)

graph.set_entry_point('retrieval_agent')

graph.add_conditional_edges(
    'retrieval_agent',
    router_agent,
    {
        'synthesis_agent': 'synthesis_agent',
        'web_agent': 'web_agent'
    }
)

graph.add_edge('web_agent', 'synthesis_agent')
graph.add_edge('synthesis_agent', END)

app = graph.compile()