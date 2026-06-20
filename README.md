# Workflow-CI

Repository ini berisi MLflow Project untuk retraining model otomatis lewat GitHub Actions
(Kriteria 3 - submission Membangun Sistem Machine Learning, Dicoding).

## Struktur

```
Workflow-CI/
├── .github/workflows/ci.yml         # CI: mlflow run -> upload artifact -> build & push Docker image
└── MLProject/
    ├── MLProject                    # entry point MLflow Project
    ├── conda.yaml                   # environment dependencies
    ├── modelling.py                 # script retraining
    └── dataset_preprocessing/
        └── diabetes_preprocessing.csv
```

## Cara menjalankan secara lokal

```bash
cd MLProject
mlflow run . --env-manager=local
```

## Setup GitHub Secrets (wajib untuk level Advance)

Buka repo ini di GitHub -> **Settings > Secrets and variables > Actions**, lalu tambahkan:

| Secret name          | Isi                                            |
|-----------------------|------------------------------------------------|
| `DOCKERHUB_USERNAME`  | username Docker Hub kamu                        |
| `DOCKERHUB_TOKEN`     | access token Docker Hub (bukan password akun)   |

Setelah secrets ditambahkan, push ke branch `main` (atau trigger manual lewat tab Actions ->
"Run workflow") untuk memicu CI. Pastikan job berstatus **success** sebelum submission dikirim,
karena reviewer akan memeriksa log GitHub Actions.
