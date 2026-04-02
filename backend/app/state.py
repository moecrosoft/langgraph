from typing import TypedDict, List

class ResearchState(TypedDict):
    query: str
    vector_context: List[str]
    web_content: List[str]
    final_answer: str