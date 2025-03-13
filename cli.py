# import argparse
# import sys
# from pubmed_fetcher.fetch import fetch_papers, save_to_csv

# def main():
#     """Command-line interface for fetching research papers."""
#     parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")

#     # Command-line arguments
#     parser.add_argument("query", nargs="?", type=str, help="Search query for PubMed")
#     parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
#     parser.add_argument("-f", "--file", type=str, help="Save output to a file (CSV)")

#     args = parser.parse_args()

#     # Handle case when query is not provided
#     if args.query is None:
#         print("\n❌ Error: No query provided.")
#         print("🔹 Usage: python cli.py '<search query>' [-d] [-f output.csv]")
#         print("🔹 Example: python cli.py 'cancer treatment' -f results.csv")
#         sys.exit(1)

#     query = args.query
#     debug = args.debug
#     filename = args.file if args.file else None

#     print(f"🔍 Fetching papers for query: {query}")

#     # Fetch data (Simulated API call)
#     results = fetch_papers(query)

#     if debug:
#         print("🛠 Debug Mode: Printing full results")
#         print(results)

#     # Save to CSV or print results
#     if filename:
#         save_to_csv(results, filename)
#     else:
#         print(results)

# if __name__ == "__main__":
#     main()
import argparse
import sys
from pubmed_fetcher.fetch import fetch_papers, get_paper_details, save_to_csv

def main():
    """Command-line interface for fetching research papers."""
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", nargs="?", type=str, help="Search query for PubMed")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-f", "--file", type=str, help="Save output to a file (CSV)")

    args = parser.parse_args()

    if args.query is None:
        print("\n❌ Error: No query provided.")
        print("🔹 Usage: python cli.py '<search query>' [-d] [-f output.csv]")
        print("🔹 Example: python cli.py 'cancer treatment' -f results.csv")
        sys.exit(1)

    query = args.query
    debug = args.debug
    filename = args.file if args.file else None

    print(f"🔍 Fetching papers for query: {query}")

    paper_ids = fetch_papers(query)
    if debug:
        print(f"📌 Found {len(paper_ids)} papers")

    papers = []
    for paper_id in paper_ids:
        details = get_paper_details(paper_id)
        if details:
            papers.append(details)

    if filename:
        save_to_csv(papers, filename)
    else:
        print(papers)

if __name__ == "__main__":
    main()
