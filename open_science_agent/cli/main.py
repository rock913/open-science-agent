import argparse
from open_science_agent.api.semantic_scholar_client import SemanticScholarClient
from open_science_agent.api.notion_client import NotionClient
from open_science_agent.data_processing.paper_analyzer import PaperAnalyzer
from open_science_agent.data_processing.paper_organizer import PaperOrganizer

def main():
    parser = argparse.ArgumentParser(description="Open Science Agent CLI")
    parser.add_argument("--query", type=str, required=True, help="Search query for papers")
    parser.add_argument("--semantic-scholar-api-key", type=str, required=True, help="API key for Semantic Scholar")
    parser.add_argument("--notion-api-key", type=str, required=True, help="API key for Notion")
    parser.add_argument("--notion-database-id", type=str, required=True, help="Database ID for Notion")
    args = parser.parse_args()

    # Initialize clients
    semantic_scholar_client = SemanticScholarClient(args.semantic_scholar_api_key)
    notion_client = NotionClient(args.notion_api_key, args.notion_database_id)

    # Search and analyze papers
    papers = semantic_scholar_client.search_papers(args.query)
    paper_analyzer = PaperAnalyzer()

    # Organize papers in Notion
    paper_organizer = PaperOrganizer(notion_client)
    for paper in papers["data"]:
        paper_details = paper_analyzer.analyze_paper(paper)
        paper_organizer.organize_paper(paper_details)

if __name__ == "__main__":
    main()
