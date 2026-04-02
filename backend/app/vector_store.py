import psycopg2
from app.config import DATABASE_URL

def conn():
    return psycopg2.connect(DATABASE_URL)

def search_memory(embedding, k=3):
    c = conn()
    cur = c.cursor()

    cur.execute(
        '''
        SELECT content
        FROM data
        ORDER BY embedding <=> %s::vector
        LIMIT %s
        ''',
        (embedding, k)
    )

    res = [r[0] for r in cur.fetchall()]
    cur.close()
    c.close()

    return res