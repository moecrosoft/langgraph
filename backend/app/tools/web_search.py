import requests

def web_search(query):
    res = requests.post(
        'https://api.tavily.com/search',
        json={'query': query, 'max_results': 5}
    )

    data = res.json()
    return [r['content'] for r in data.get('results',[])]