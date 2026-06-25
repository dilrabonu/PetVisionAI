# 🐱🐶 CatDog Vision API

> A production-grade image classification service: drag in a photo → CNN decides
> **cat or dog** → an LLM agent explains the result → served over a REST API.

[![CI](https://github.com/YOUR_USERNAME/catdog-vision-api/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/catdog-vision-api/actions)

This is **not a notebook project**. The model is one layer of six. The value is in
the engineering around it: preprocessing, an API, an agent, a frontend, tests,
containerization, and CI.

---

## 🏗️ Architecture

```
Upload → OpenCV preprocess → CNN (PyTorch) → prediction → LLM agent → report
                                                                 │
        Production layer:  FastAPI · Docker · frontend · logging · CI
```

| Layer       | Tech                 | Role                              |
|-------------|----------------------|-----------------------------------|
| Preprocess  | OpenCV               | Resize, normalize, tensor-ify     |
| Model       | PyTorch              | CNN scratch + ResNet18 transfer   |
| Agent       | Anthropic Claude     | Explains the prediction           |
| API         | FastAPI              | `/health`, `/predict` endpoints   |
| Frontend    | HTML/CSS/JS          | Drag-and-drop UI                  |
| Ops         | Docker · GitHub CI   | Containerized, tested on push     |

---

## 📂 Structure

```
catdog-vision-api/
├── notebooks/      # 01_train_classifier.ipynb — research & training
├── src/
│   ├── models/     # architectures.py (scratch CNN + ResNet18)
│   ├── data/       # dataset.py (loaders, transforms)
│   ├── inference/  # preprocess.py, predictor.py
│   ├── agent/      # explainer.py (Claude)
│   ├── api/        # main.py, schemas.py (FastAPI)
│   ├── config.py   # loads configs/config.yaml
│   └── train.py    # training entry point
├── app/            # frontend (templates + static)
├── tests/          # pytest
├── configs/        # config.yaml
├── scripts/        # split_data.py
├── docker/         # Dockerfile + compose
├── .github/workflows/  # ci.yml
└── data/ models/ logs/
```

---

## 🚀 Quickstart

```bash
# 1. Environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2. Data — download Kaggle "Dogs vs. Cats", then:
python scripts/split_data.py --source data/raw

# 3. Train (scratch to learn, resnet18 for production)
python -m src.train --arch scratch
python -m src.train --arch resnet18

# 4. Serve
cp .env.example .env             # add your ANTHROPIC_API_KEY
uvicorn src.api.main:app --reload
# open http://localhost:8000
```

---

## 🧪 Tests

```bash
pytest -v
```

## 🐳 Docker

```bash
docker compose -f docker/docker-compose.yml up --build
```

---

## 📊 Dataset

Kaggle [Dogs vs. Cats](https://www.kaggle.com/c/dogs-vs-cats/data) — 25,000 labeled
images. Place the extracted files in `data/raw/` and run the split script.

---

## 📝 License

MIT