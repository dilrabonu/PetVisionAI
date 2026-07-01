# Loads all settings from configs
from pathlib import Path
import yaml
import torch

ROOT = Path(__file__).resolve().parent.parent

CONFIG_PATH = ROOT / "configs" / "config.yaml"

def _resolve_device(name: str) -> str:
    if name == "auto":
        return "cuda" if torch.cuda.is_available() else "cpu"
    return name

def load_config(path: Path = CONFIG_PATH) -> dict:
    with open(path) as f:
        cfg = yaml.safe_load(f)
    cfg["train"]["device"] = _resolve_device(cfg["train"]["device"])
    return cfg