# Loads all settings from configs
from pathlib import Path
import yaml
import torch

ROOT = Path(__file__).resolve().parent.parent

CONFIG_PATH = ROOT / "configs" / "config.yaml"
