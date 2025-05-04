import os

# Define the folder structure as a dictionary
structure = {
    "medic_ai": {
        "data": {
            "raw": {},
            "processed": {},
            "loaders": {
                "prepare_pubmed.py": "",
                "build_graph_from_drugbank.py": ""
            }
        },
        "notebooks_learning": {
            "ibm_generative_ai": {
                "01_llm_intro.ipynb": "",
                "02_prompting.ipynb": "",
                "03_rag_pipeline.ipynb": ""
            },
            "huggingface_transformers": {},
            "gnns_youtube_stanford": {},
            "extra_notes.md": ""
        },
        "notebooks_research": {
            "test_gnn_drug_filtering.ipynb": "",
            "rag_vs_baseline_qa.ipynb": "",
            "multi_condition_inference.ipynb": ""
        },
        "src": {
            "inference": {
                "predict_plan.py": ""
            },
            "transformer": {
                "fine_tune_flan.py": "",
                "diagnosis_model.py": ""
            },
            "gnn": {
                "build_graph.py": "",
                "train_gnn.py": "",
                "filter_drugs.py": ""
            },
            "rag": {
                "build_index.py": "",
                "retrieve.py": "",
                "generate_answer.py": ""
            },
            "utils": {
                "config.py": "",
                "eval_metrics.py": "",
                "logger.py": ""
            }
        },
        "app": {
            "streamlit_app.py": "",
            "components": {
                "patient_form.py": "",
                "graph_view.py": "",
                "treatment_table.py": ""
            },
            "assets": {
                "style.css": ""
            }
        },
        "devops": {
            "deploy_hf_space.sh": "",
            "nginx.conf": "",
            "gunicorn_config.py": ""
        },
        "tests": {
            "test_transformer.py": "",
            "test_gnn.py": "",
            "test_rag.py": ""
        },
        "publications": {
            "milestone_1_rag_transformer": {},
            "milestone_2_gnn_safety": {},
            "milestone_3_full_engine": {},
            "final_mvp_paper": {
                "main.tex": "",
                "figures": {},
                "bibtex.bib": "",
                "pdf_draft.pdf": ""
            }
        },
        "docs": {
            "architecture_v1.png": "",
            "weekly_plan.pdf": "",
            "system_flow.md": ""
        },
        "mvp_demo": {
            "docker-compose.prod.yml": "",
            "Procfile": "",
            "app_config.yaml": ""
        },
        "README.md": "",
        "LICENSE": "",
        "Makefile": "",
        ".env.example": "",
        "requirements.txt": "",
        "environment.yml": "",
        ".gitignore": ""
    }
}

# Function to recursively create folders and files
def create_structure(base_path, tree):
    for name, content in tree.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content)

# Create the directory structure in the working directory
base_directory = "."
create_structure(base_directory, structure)

"✅ Folder structure created at /mnt/data/clinical-ai-engine"

