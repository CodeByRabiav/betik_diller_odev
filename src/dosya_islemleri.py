# src/dosya_islemleri.py
from pathlib import Path
from .dekorator import timer
import csv
import json
from typing import List, Dict, Any

@timer
def read_csv(path: str) -> List[Dict[str, str]]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"CSV bulunamadı: {path}")
    with p.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

@timer
def write_json(path: str, obj: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

@timer
def write_text(path: str, text: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
