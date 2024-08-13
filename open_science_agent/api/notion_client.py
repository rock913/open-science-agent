import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class NotionClient:
    BASE_URL = "https://api.notion.com/v1"

    def __init__(self):
        self.api_key = os.getenv('NOTION_API_KEY')

    def create_page(self, database_id, properties):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
        data = {
            "parent": {"database_id": database_id},
            "properties": properties
        }
        
        try:
            response = requests.post(f"{self.BASE_URL}/pages", headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            print(f"Response content: {response.content}")
        except Exception as err:
            print(f"An error occurred: {err}")
            if 'response' in locals():
                print(f"Response content: {response.content}")
