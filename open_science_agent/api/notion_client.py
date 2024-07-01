import requests

class NotionClient:
    BASE_URL = "https://api.notion.com/v1"

    def __init__(self, api_key, database_id):
        self.api_key = api_key
        self.database_id = database_id

    def create_page(self, title, properties):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2021-05-13"
        }
        data = {
            "parent": {"database_id": self.database_id},
            "properties": {
                "Name": {"title": [{"text": {"content": title}}]},
                **properties
            }
        }
        response = requests.post(f"{self.BASE_URL}/pages", headers=headers, json=data)
        response.raise_for_status()
        return response.json()
