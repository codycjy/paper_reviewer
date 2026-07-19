from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


class JsonCache:
    def __init__(self, root: str | Path, namespace: str):
        self.root = Path(root) / namespace
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, key: str) -> Path:
        digest = hashlib.sha1(key.encode("utf-8")).hexdigest()
        return self.root / f"{digest}.json"

    def get(self, key: str) -> Any | None:
        path = self._path(key)
        if not path.exists():
            return None
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return None

    def set(self, key: str, value: Any) -> None:
        path = self._path(key)
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
