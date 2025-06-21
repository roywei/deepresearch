import argparse
from .pdf_reader import read_pdf_text
from .web_search import search_duckduckgo
from .orchestrator import run_parallel_search


def main():
    parser = argparse.ArgumentParser(description="Deep Research Tool")
    subparsers = parser.add_subparsers(dest="command")

    pdf_parser = subparsers.add_parser("pdf", help="Read text from a PDF file")
    pdf_parser.add_argument("path", help="Path to PDF file")

    search_parser = subparsers.add_parser("search", help="Search the web")
    search_parser.add_argument("query", help="Search query")

    multi_search_parser = subparsers.add_parser(
        "multi-search", help="Run multiple web searches in parallel"
    )
    multi_search_parser.add_argument("queries", nargs="+", help="List of queries")

    args = parser.parse_args()

    if args.command == "pdf":
        text = read_pdf_text(args.path)
        print(text)
    elif args.command == "search":
        results = search_duckduckgo(args.query)
        for title, url in results:
            print(f"{title}\n{url}\n")
    elif args.command == "multi-search":
        results = run_parallel_search(args.queries)
        for q, res in results.items():
            print(f"Results for: {q}")
            for title, url in res:
                print(f"  {title}\n  {url}")
            print()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
