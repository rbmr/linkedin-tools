import json
import os
from typing import Dict, List, Any, Optional
from pathlib import Path

class DataManager:
    def __init__(self, output_dir: Optional[Path] = None):
        if output_dir is None:
            output_dir = Path.cwd() / "linkedin_data"
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def save_domain(self, domain: str, data: List[Dict[str, Any]]):
        filename = self.output_dir / f"{domain}.json"
        with filename.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Saved {len(data)} items to {filename}")

    def load_domain(self, domain: str) -> List[Dict[str, Any]]:
        filename = self.output_dir / f"{domain}.json"
        if not filename.exists():
            return []
        with filename.open("r", encoding="utf-8") as f:
            return json.load(f)