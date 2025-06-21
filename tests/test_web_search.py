from backend.web_search import search_duckduckgo
import requests
from unittest.mock import patch, Mock


def mocked_get(*args, **kwargs):
    class Response:
        status_code = 200
        text = """
        <html>
        <body>
            <a class='result__a' href='https://example.com/1'>Result 1</a>
            <a class='result__a' href='https://example.com/2'>Result 2</a>
        </body>
        </html>
        """

        def raise_for_status(self):
            pass

    return Response()


def test_search_duckduckgo():
    with patch.object(requests, 'get', side_effect=mocked_get):
        results = search_duckduckgo('test', max_results=2)
    assert results == [
        ('Result 1', 'https://example.com/1'),
        ('Result 2', 'https://example.com/2'),
    ]
