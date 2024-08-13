import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

import os
import requests

class SemanticScholarClient:
    BASE_URL = "https://api.semanticscholar.org/graph/v1"

    def __init__(self, timeout=(10, 30)):  # Default timeout of 10 seconds for connect and 30 seconds for read
        self.api_key = os.getenv('SEMANTIC_SCHOLAR_API_KEY')
        self.timeout = timeout

    def search_papers(self, query, limit=10):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        params = {"query": query, "limit": limit}
        response = requests.get(f"{self.BASE_URL}/paper/search", headers=headers, params=params, timeout=self.timeout)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            print(f"Response content: {response.content}")
            raise
        return response.json()

    def get_paper_details(self, paper_id):
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(f"{self.BASE_URL}/paper/{paper_id}", headers=headers, timeout=self.timeout)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            print(f"Response content: {response.content}")
            raise
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
            "minCitationCount": 0
        }
        response = requests.get(f"{self.BASE_URL}/paper/search", headers=headers, params=params, timeout=self.timeout)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            print(f"Response content: {response.content}")
            raise
        return response.json()

    def get_search_results_with_retries(self, query, max_retries=5, sleep_time=2):
        for attempt in range(max_retries):
            try:
                # Attempt to call the search_papers_by_relevance function
                results = self.search_papers_by_relevance(query)
                return results  # Return the results if successful
            except requests.exceptions.RequestException as e:
                # Catch exceptions related to the request
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    print(f"Retrying in {sleep_time} seconds...")
                    time.sleep(sleep_time)
                else:
                    print("Max retries reached. Failing gracefully.")
                    raise  # Re-raise the exception if max retries are reached
