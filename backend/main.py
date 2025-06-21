import argparse
from .pdf_reader import read_pdf_text
from .web_search import search_duckduckgo


def main():
    parser = argparse.ArgumentParser(description="Deep Research Tool")
    subparsers = parser.add_subparsers(dest="command")

    pdf_parser = subparsers.add_parser("pdf", help="Read text from a PDF file")
    pdf_parser.add_argument("path", help="Path to PDF file")

    search_parser = subparsers.add_parser("search", help="Search the web")
    search_parser.add_argument("query", help="Search query")

    args = parser.parse_args()

    if args.command == "pdf":
        text = read_pdf_text(args.path)
        print(text)
    elif args.command == "search":
        results = search_duckduckgo(args.query)
        for title, url in results:
            print(f"{title}\n{url}\n")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
