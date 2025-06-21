import json
import os
from typing import Dict, List

import openai

from .pdf_reader import read_pdf_text
from .web_search import search_duckduckgo
from .orchestrator import compile_results

openai.api_key = os.getenv("OPENAI_API_KEY")

_FUNCTIONS = [
    {
        "name": "read_pdf",
        "description": "Read text from a PDF file",
        "parameters": {
            "type": "object",
            "properties": {"path": {"type": "string", "description": "Path to PDF file"}},
            "required": ["path"],
        },
    },
    {
        "name": "search",
        "description": "Search the web and return formatted results",
        "parameters": {
            "type": "object",
            "properties": {"query": {"type": "string", "description": "Search query"}},
            "required": ["query"],
        },
    },
]


def _call_function(name: str, arguments: Dict[str, str]) -> str:
    if name == "read_pdf":
        return read_pdf_text(**arguments)
    if name == "search":
        results = search_duckduckgo(**arguments)
        return compile_results(results)
    return f"Unknown function: {name}"


def call_openai_agent(messages: List[Dict[str, str]]) -> str:
    """Send messages to OpenAI and handle function calls."""
    while True:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            functions=_FUNCTIONS,
            function_call="auto",
        )
        message = response["choices"][0]["message"]
        if message.get("function_call"):
            func_name = message["function_call"]["name"]
            args = json.loads(message["function_call"]["arguments"])
            result = _call_function(func_name, args)
            messages.append({"role": "function", "name": func_name, "content": result})
            continue
        return message.get("content", "")


def agent_chat_loop() -> None:
    """Interactive conversation powered by OpenAI with tool calls."""
    messages: List[Dict[str, str]] = [
        {
            "role": "system",
            "content": "You help with research. You may search the web or read PDFs when helpful.",
        }
    ]
    print("Type a message and press enter. Type 'exit' to quit.")
    while True:
        try:
            text = input("> ").strip()
        except EOFError:
            break
        if not text:
            continue
        if text.lower() in {"exit", "quit"}:
            break
        messages.append({"role": "user", "content": text})
        reply = call_openai_agent(messages)
        messages.append({"role": "assistant", "content": reply})
        print(reply)
        print()
