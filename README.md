# Open Science Agent

Open Science Agent is an open-source Python toolkit designed to explore and analyze academic papers. Leveraging the Semantic Scholar API for retrieving and analyzing papers, and the Notion API for organizing related papers and codes, this toolkit aims to streamline research and documentation processes for researchers.

## Features

- **Retrieve academic papers** from Semantic Scholar using search queries.
- **Analyze papers** to extract essential information such as title, authors, and abstract.
- **Organize papers** in Notion databases, categorizing and storing key details.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/open_science_agent.git
   cd open_science_agent
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Install the package:
   ```sh
   pip install .
   ```

## Usage

### Command-Line Interface (CLI)

The Open Science Agent provides a CLI for interacting with the toolkit. 

Example usage:
```sh
open-science-agent --query "machine learning in atmospheric science" \
                   --semantic-scholar-api-key YOUR_SEMANTIC_SCHOLAR_API_KEY \
                   --notion-api-key YOUR_NOTION_API_KEY \
                   --notion-database-id YOUR_NOTION_DATABASE_ID
```

### Jupyter Notebook Demo

A Jupyter Notebook (`demo.ipynb`) is included to demonstrate the usage of the toolkit.

1. Navigate to the `notebooks` directory:
   ```sh
   cd notebooks
   ```

2. Launch Jupyter Notebook:
   ```sh
   jupyter notebook
   ```

3. Open and run `demo.ipynb` to see the toolkit in action.

## Project Structure

```
open_science_agent/
│
├── open_science_agent/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── semantic_scholar_client.py
│   │   └── notion_client.py
│   ├── data_processing/
│   │   ├── __init__.py
│   │   ├── paper_analyzer.py
│   │   └── paper_organizer.py
│   └── cli/
│       ├── __init__.py
│       └── main.py
│
├── notebooks/
│   ├── demo.ipynb
│
├── tests/
│   ├── __init__.py
│   ├── test_semantic_scholar_client.py
│   ├── test_notion_client.py
│   ├── test_paper_analyzer.py
│   └── test_paper_organizer.py
│
├── requirements.txt
├── setup.py
└── README.md
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Semantic Scholar](https://www.semanticscholar.org/)
- [Notion](https://www.notion.so/)

---