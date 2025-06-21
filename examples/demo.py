"""Demonstrate the CLI by running a parallel web search.

This script calls the command-line interface defined in ``backend.main``.
It accepts optional search queries; if none are provided, it uses two
example queries.

Usage::

    python examples/demo.py [query1 query2 ...]
"""
import subprocess
import sys


def main() -> None:
    queries = sys.argv[1:] or ["AI research", "machine learning"]
    cmd = [sys.executable, "-m", "backend.main", "multi-search", *queries]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
