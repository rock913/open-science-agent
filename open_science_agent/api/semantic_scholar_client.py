import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class SemanticScholarClient:
    BASE_URL = "https://api.semanticscholar.org/graph/v1"

    def __init__(self):
        self.api_key = os.getenv('SEMANTIC_SCHOLAR_API_KEY')

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

    def search_papers_by_relevance(self, query, offset=0, limit=20):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {
            "query": query,
            "offset": offset,
            "limit": limit,
            "fields": "corpusId,url,title,venue,publicationVenue,year,authors,externalIds,abstract,"
                      "referenceCount,citationCount,influentialCitationCount,isOpenAccess,openAccessPdf,"
                      "fieldsOfStudy,s2FieldsOfStudy,publicationTypes,publicationDate,journal,citationStyles,tldr",
            "publicationTypes": "Review,JournalArticle",
            "minCitationCount": 5
        }
        response = requests.get(f"{self.BASE_URL}/paper/search", headers=headers, params=params)
        response.raise_for_status()  # Raises an HTTPError if the request was unsuccessful
        return response.json()