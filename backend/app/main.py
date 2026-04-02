from fastapi import FastAPI
from pydantic import BaseModel

from app.graph import app as research_graph
from app.db import create_db, seed_data

app = FastAPI()

create_db()
seed_data()

class QueryRequest(BaseModel):
    query: str

@app.post('/research')
def research(request: QueryRequest):
    return research_graph.invoke({'query': request.query})