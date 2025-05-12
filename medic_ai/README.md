# 🧠 Clinic AI Engine

**Clinic AI Engine** is a milestone-driven research and product project focused on building an **explainable AI system** for:

- Clinical reasoning  
- Safe treatment planning  
- Medication interaction filtering  

The system integrates **Transformers**, **Graph Neural Networks (GNNs)**, and **Retrieval-Augmented Generation (RAG)** into a unified reasoning pipeline.

---

## 📁 Project Folder Structure Overview

### 🔹 Data

| Folder              | Purpose                                                            |
|---------------------|--------------------------------------------------------------------|
| `data/raw/`         | Raw datasets (DrugBank, PubMed abstracts, symptom-condition CSVs)  |
| `data/processed/`   | Cleaned and structured data for training and evaluation            |
| `data/loaders/`     | Scripts to parse raw files into usable graph/text formats          |

### 🔹 Notebooks

| Folder                                      | Purpose                                         |
|---------------------------------------------|-------------------------------------------------|
| `notebooks_learning/`                       | Learning experiments and course notebooks       |
| └── `ibm_generative_ai/`                    | IBM Gen AI notebooks                            |
| └── `huggingface_transformers/`             | Hugging Face Transformers examples              |
| └── `gnns_youtube_stanford/`                | Stanford CS224W GNN concepts                    |
| `notebooks_research/`                       | Research notebooks (GNNs, RAG, baseline tests)  |

### 🔹 Source Code

| Folder              | Purpose                                                            |
|---------------------|--------------------------------------------------------------------|
| `src/transformer/`  | Fine-tuning (Flan-T5, BioBERT)                                     |
| `src/gnn/`          | Graph construction, GNN training and inference                     |
| `src/rag/`          | RAG indexing and retrieval pipeline                                |
| `src/inference/`    | Unified reasoning engine (Transformer + GNN + RAG)                 |
| `src/utils/`        | Configs, evaluation metrics, logging tools                         |

### 🔹 Application

| Folder              | Purpose                                                            |
|---------------------|--------------------------------------------------------------------|
| `app/`              | Streamlit UI application                                           |
| └── `components/`   | UI components (forms, graphs, treatment tables)                    |
| └── `assets/`       | Custom stylesheets and frontend assets                             |

### 🔹 Other

| Folder              | Purpose                                                            |
|---------------------|--------------------------------------------------------------------|
| `tests/`            | Unit and integration tests                                         |
| `publications/`     | Research papers and milestone drafts                               |
| `docs/`             | Internal documentation, flowcharts, diagrams                       |
| `mvp_demo/`         | Deployment configs (Docker, Streamlit Cloud, Hugging Face Spaces)  |

---

## 🔧 Root Files

| File                | Purpose                                      |
|---------------------|----------------------------------------------|
| `README.md`         | Project overview and folder guide            |
| `LICENSE`           | Open-source license (e.g., MIT)              |
| `Makefile`          | CLI commands: `make train`, `make run`, etc. |
| `.env.example`      | API key and model path template              |
| `requirements.txt`  | Python packages for `pip`                    |
| `environment.yml`   | Conda environment specification (optional)   |
| `.gitignore`        | Excludes logs, dumps, models, secrets        |

---

## 📌 Milestone Highlights

| Milestone                                                   | Timeline     |
|-------------------------------------------------------------|--------------|
| 🔬 Fine-tune Transformer on symptom → diagnosis             | Week 1–2     |
| 📖 Build RAG pipeline with citation-backed reasoning         | Week 3–4     |
| 🌐 Train GNN for allergy-aware medication filtering          | Week 5–8     |
| 🧠 Integrate Transformer + GNN + RAG into a single engine     | Week 9–12    |
| 🚀 Streamlit MVP + academic paper submission                 | Week 13–16   |

---

## 📦 How to Get Started

Clone the repository and run the app locally:

```bash
git clone https://github.com/yourname/clinical-ai-engine.git
cd clinical-ai-engine
make setup        # Optional: creates environment & installs requirements
make run-app      # Launches Streamlit demo locally
