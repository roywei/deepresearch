import json
from unittest.mock import patch

import openai

from backend.chat_agent import call_openai_agent


def test_call_openai_agent_function_call(monkeypatch):
    messages = [{"role": "user", "content": "search for ai"}]

    responses = [
        {"choices": [{"message": {"function_call": {"name": "search", "arguments": json.dumps({"query": "ai"})}}}]},
        {"choices": [{"message": {"content": "Here are the results"}}]},
    ]

    def fake_create(**kwargs):
        return responses.pop(0)

    monkeypatch.setattr(openai.ChatCompletion, "create", fake_create)
    with patch("backend.chat_agent.search_duckduckgo", return_value=[("t", "u")]):
        result = call_openai_agent(messages)
    assert result == "Here are the results"
