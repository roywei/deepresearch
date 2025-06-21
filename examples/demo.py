"""Demonstrate the CLI.

This script calls the command-line interface defined in ``backend.main``.
With the ``chat`` argument it starts an interactive session. Otherwise it
runs a parallel search using example queries.

Usage::

    python examples/demo.py chat
    python examples/demo.py [query1 query2 ...]
"""
import subprocess
import sys


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "chat":
        cmd = [sys.executable, "-m", "backend.main", "chat"]
        subprocess.run(cmd, check=True)
        return

    queries = sys.argv[1:] or ["AI research", "machine learning"]
    cmd = [sys.executable, "-m", "backend.main", "multi-search", *queries]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
