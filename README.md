# Deep Research

This project provides a simple backend foundation for a multi-agent research system inspired by the [Anthropic multi-agent blog post](https://www.anthropic.com/engineering/built-multi-agent-research-system). It starts with two basic tools written in Python:

- **PDF reader** using `PyPDF2` to extract text from PDF files.
- **Web search** using DuckDuckGo to retrieve search results.

The repository also contains placeholders for a Node.js frontend.

## Backend Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the command-line tool:

```bash
python -m backend.main pdf path/to/file.pdf
python -m backend.main search "research topic"
```

## Testing

Tests use `pytest`:

```bash
pytest
```
