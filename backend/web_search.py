import requests
from bs4 import BeautifulSoup


USER_AGENT = "Mozilla/5.0 (compatible; DeepResearchBot/1.0; +https://example.com/bot)"
HEADERS = {"User-Agent": USER_AGENT}


def search_duckduckgo(query: str, max_results: int = 5):
    """Perform a DuckDuckGo search and return a list of (title, url) tuples."""
    params = {"q": query}
    response = requests.get("https://duckduckgo.com/html/", params=params, headers=HEADERS, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for a in soup.select("a.result__a"):
        title = a.get_text()
        url = a["href"]
        results.append((title, url))
        if len(results) >= max_results:
            break
    return results
