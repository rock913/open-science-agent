import requests

class SemanticScholarClient:
    BASE_URL = "https://api.semanticscholar.org/graph/v1"

    def __init__(self, api_key):
        self.api_key = api_key

    def search_papers(self, query, limit=10):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"query": query, "limit": limit}
        response = requests.get(f"{self.BASE_URL}/paper/search", headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_paper_details(self, paper_id):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(f"{self.BASE_URL}/paper/{paper_id}", headers=headers)
        response.raise_for_status()
        return response.json()
