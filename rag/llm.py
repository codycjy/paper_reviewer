from __future__ import annotations

import json
import re
from typing import Any

from agents import create_llm_client, format_llm_error


def parse_json_object(text: str) -> dict[str, Any]:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            return json.loads(text[start:end + 1])
        raise


class RAGLLMAgent:
    def __init__(self, provider: str, api_key: str, model: str = "", client=None):
        self.provider = (provider or "cmu").lower()
        self.model = model
        self.client = client or create_llm_client(provider=self.provider, api_key=api_key, model=model)

    def complete_json(self, system_prompt: str, user_prompt: str) -> dict[str, Any]:
        try:
            reply = self.client.complete(system_prompt, [{"role": "user", "content": user_prompt}])
        except Exception as exc:
            raise RuntimeError(format_llm_error(self.provider, exc)) from exc
        return parse_json_object(reply)
