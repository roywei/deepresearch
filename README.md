# Deep Research

This project provides a simple backend foundation for a multi-agent research system inspired by the [Anthropic multi-agent blog post](https://www.anthropic.com/engineering/built-multi-agent-research-system). It starts with two basic tools written in Python:

- **PDF reader** using `PyPDF2` to extract text from PDF files.
- **Web search** using DuckDuckGo to retrieve search results.
- **Parallel multi-search** orchestrator that runs several searches concurrently.

The repository also contains placeholders for a Node.js frontend.

## Backend Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

To enable the OpenAI-powered chat mode, set your API key:

```bash
export OPENAI_API_KEY=your-key-here
```

Run the command-line tool:

```bash
python -m backend.main pdf path/to/file.pdf
python -m backend.main search "research topic"
python -m backend.main multi-search "topic one" "topic two"
python -m backend.main chat
python -m backend.main openai-chat
```

## Example Demo

You can run a short demonstration script that invokes the CLI with sample
queries. Run it with ``chat`` to start an interactive conversation:

```bash
python examples/demo.py
python examples/demo.py chat
```

Pass your own queries to override the defaults:

```bash
python examples/demo.py "query one" "query two"
```

## Testing

Tests use `pytest`:

```bash
pytest
```
