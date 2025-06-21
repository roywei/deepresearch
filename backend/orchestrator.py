from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Tuple

from .web_search import search_duckduckgo


def run_parallel_search(queries: List[str], max_results: int = 5) -> Dict[str, List[Tuple[str, str]]]:
    """Run web searches in parallel for a list of queries."""
    results: Dict[str, List[Tuple[str, str]]] = {}
    with ThreadPoolExecutor() as executor:
        future_to_query = {
            executor.submit(search_duckduckgo, q, max_results): q for q in queries
        }
        for future in future_to_query:
            query = future_to_query[future]
            results[query] = future.result()
    return results
