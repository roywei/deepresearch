from backend.orchestrator import run_parallel_search
from backend.web_search import search_duckduckgo
import requests
from unittest.mock import patch


def mocked_get(*args, **kwargs):
    class Response:
        status_code = 200
        text = """
        <html>
        <body>
            <a class='result__a' href='https://example.com/1'>Result 1</a>
        </body>
        </html>
        """

        def raise_for_status(self):
            pass

    return Response()


def test_run_parallel_search():
    with patch.object(requests, 'get', side_effect=mocked_get):
        queries = ['alpha', 'beta']
        results = run_parallel_search(queries, max_results=1)
    assert set(results.keys()) == set(queries)
    for res in results.values():
        assert res == [('Result 1', 'https://example.com/1')]
