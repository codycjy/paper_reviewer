from __future__ import annotations

import re


SUSPICIOUS_PATTERNS = (
    r"ignore (?:all )?(?:previous|prior|above) instructions",
    r"give this paper a positive review",
    r"you are (?:chatgpt|an ai|a language model)",
    r"instructions? (?:for|to) (?:the )?(?:llm|ai|reviewer|agent)",
    r"do not mention",
    r"system prompt",
)


def prompt_injection_warnings(text: str, source_label: str) -> list[str]:
    warnings: list[str] = []
    lower = text.lower()
    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, lower):
            warnings.append(f"{source_label}: suspicious instruction-like text matched /{pattern}/")
    if "\u200b" in text or "\ufeff" in text:
        warnings.append(f"{source_label}: hidden zero-width text detected")
    return warnings
