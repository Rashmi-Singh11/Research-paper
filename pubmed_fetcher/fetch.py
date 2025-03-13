import requests
import pandas as pd
import re
from typing import List, Dict

# PubMed API Endpoints
PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

# List of common academic keywords to exclude
ACADEMIC_KEYWORDS = ["university", "college", "institute", "lab", "hospital", "school", "research center"]

def fetch_papers(query: str, max_results: int = 10) -> List[str]:
    """Fetches PubMed IDs for research papers matching the query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }

    response = requests.get(PUBMED_SEARCH_URL, params=params)
    if response.status_code != 200:
        raise Exception("❌ Error fetching data from PubMed API")

    data = response.json()
    paper_ids = data.get("esearchresult", {}).get("idlist", [])
    return paper_ids

def get_paper_details(paper_id: str) -> Dict:
    """Fetches details of a research paper using PubMed ID."""
    params = {
        "db": "pubmed",
        "id": paper_id,
        "retmode": "json"
    }

    response = requests.get(PUBMED_SUMMARY_URL, params=params)
    if response.status_code != 200:
        return None  # Skip if API call fails

    paper_data = response.json()
    result = paper_data.get("result", {}).get(paper_id, {})

    title = result.get("title", "Unknown Title")
    pub_date = result.get("pubdate", "Unknown Date")
    authors = result.get("authors", [])
    corresponding_email = result.get("corresponding_author", "N/A")

    # Filter non-academic authors and detect company affiliations
    non_academic_authors, company_affiliations = extract_non_academic_authors(authors)

    return {
        "PubmedID": paper_id,
        "Title": title,
        "Publication Date": pub_date,
        "Non-academic Author(s)": ", ".join(non_academic_authors),
        "Company Affiliation(s)": ", ".join(company_affiliations),
        "Corresponding Author Email": corresponding_email
    }

def extract_non_academic_authors(authors: List[Dict]) -> (List[str], List[str]):
    """Extracts authors affiliated with non-academic institutions."""
    non_academic_authors = []
    company_affiliations = []

    for author in authors:
        affiliation = author.get("affiliation", "").strip()

        # Skip if no affiliation is provided
        if not affiliation:
            continue

        # Exclude academic institutions
        if not any(keyword in affiliation.lower() for keyword in ACADEMIC_KEYWORDS):
            non_academic_authors.append(author.get("name", "Unknown"))
            company_affiliations.append(affiliation)

    return non_academic_authors, company_affiliations

def save_to_csv(data: List[Dict], filename: str) -> None:
    """Save fetched data to a CSV file with required columns."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"✅ Results saved to {filename}")
