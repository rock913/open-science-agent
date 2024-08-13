import json

def map_paper_to_notion_properties(paper):
    properties = {
        "Title": {
            "title": [
                {
                    "text": {
                        "content": paper.get("title", "Untitled")
                    }
                }
            ]
        },
        "Authors": {
            "rich_text": [
                {
                    "text": {
                        "content": ", ".join([author["name"] for author in paper.get("authors", [])])
                    }
                }
            ]
        },
        "Year": {
            "number": paper.get("year", None)
        },
        "Journal": {
            "rich_text": [
                {
                    "text": {
                        "content": paper.get("journal", {}).get("name", "Unknown")
                    }
                }
            ]
        },
        "URL": {
            "url": paper.get("url", "")
        },
        "Abstract": {
            "rich_text": [
                {
                    "text": {
                        "content": paper.get("abstract") if paper.get("abstract") else "No abstract available."
                    }
                }
            ]
        },
        "CitationCount": {
            "number": paper.get("citationCount", 0)
        },
        "ExternalIds": {
            "rich_text": [
                {
                    "text": {
                        "content": json.dumps(paper.get("externalIds", {}))
                    }
                }
            ]
        },
        "PaperId": {
            "rich_text": [
                {
                    "text": {
                        "content": paper.get("paperId", "N/A")
                    }
                }
            ]
        },
        "PublicationVenue": {
            "rich_text": [
                {
                    "text": {
                        "content": json.dumps(paper.get("publicationVenue", {}))
                    }
                }
            ]
        },
        "Venue": {
            "rich_text": [
                {
                    "text": {
                        "content": paper.get("venue", "Unknown")
                    }
                }
            ]
        },
        "ReferenceCount": {
            "number": paper.get("referenceCount", 0)
        },
        "InfluentialCitationCount": {
            "number": paper.get("influentialCitationCount", 0)
        },
        "IsOpenAccess": {
            "rich_text": [
                {
                    "text": {
                        "content": str(paper.get("isOpenAccess", False))
                    }
                }
            ]
        },
        "OpenAccessPdf": {
            "rich_text": [
                {
                    "text": {
                        "content": paper.get("openAccessPdf", {}).get("url", "N/A") if paper.get("openAccessPdf") else "N/A"
                    }
                }
            ]
        },
        "FieldsOfStudy": {
            "rich_text": [
                {
                    "text": {
                        "content": json.dumps(paper.get("fieldsOfStudy", []))
                    }
                }
            ]
        },
        "S2FieldsOfStudy": {
            "rich_text": [
                {
                    "text": {
                        "content": json.dumps(paper.get("s2FieldsOfStudy", []))
                    }
                }
            ]
        },
        "Tldr": {
            "rich_text": [
                {
                    "text": {
                        "content": paper.get("tldr", {}).get("text", "N/A") if paper.get("tldr") else "N/A"
                    }
                }
            ]
        },
        "PublicationTypes": {
            "rich_text": [
                {
                    "text": {
                        "content": json.dumps(paper.get("publicationTypes", []))
                    }
                }
            ]
        },
        "PublicationDate": {
            "rich_text": [
                {
                    "text": {
                        "content": paper.get("publicationDate", "N/A")
                    }
                }
            ]
        },
        "CitationStyles": {
            "rich_text": [
                {
                    "text": {
                        "content": json.dumps(paper.get("citationStyles", {}))
                    }
                }
            ]
        }
    }
    return properties