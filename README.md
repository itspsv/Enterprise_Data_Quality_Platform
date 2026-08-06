# Enterprise Data Quality Platform

A cloud-enabled data quality platform that validates datasets, separates valid and invalid records, generates execution metadata, stores processed data in Amazon S3, and provides an interactive dashboard for monitoring pipeline health.

---

## Features

- Configuration-driven validation using YAML
- Null, Duplicate, Email, and Range validation rules
- Rule Registry for dynamic rule loading
- Data quality score generation
- Silver and Quarantine data layers
- Incremental processing
- Structured logging with Loguru
- Amazon S3 integration
- Streamlit monitoring dashboard
- AI-generated quality summary
- Unit testing with Pytest
- GitHub Actions CI/CD
- Snowflake connectivity

---

## Architecture

```text
              Amazon S3
                  │
                  ▼
           Raw Dataset (CSV)
                  │
                  ▼
          Ingestion Engine
                  │
                  ▼
         Validation Engine
                  │
         ┌────────┴────────┐
         ▼                 ▼
   Silver Dataset   Quarantine Dataset
         │                 │
         └────────┬────────┘
                  ▼
          Pipeline Metadata
                  │
                  ▼
       Streamlit Dashboard
```

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Data Processing | Polars |
| Cloud Storage | Amazon S3 |
| Data Warehouse | Snowflake |
| Dashboard | Streamlit |
| Logging | Loguru |
| Testing | Pytest |
| CI/CD | GitHub Actions |

---

## Project Structure

```text
Enterprise_Data_Quality_Platform/
│
├── edqp/
├── datasets/
├── metadata/
├── logs/
├── tests/
├── dashboard.py
├── run_pipeline.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository.

```bash
git clone <repository-url>

cd Enterprise_Data_Quality_Platform
```

Create and activate a virtual environment.

```bash
python -m venv .venv

source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root.

```text
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=

SNOWFLAKE_ACCOUNT=
SNOWFLAKE_USER=
SNOWFLAKE_PASSWORD=
SNOWFLAKE_WAREHOUSE=
SNOWFLAKE_DATABASE=
SNOWFLAKE_SCHEMA=
SNOWFLAKE_ROLE=
```

Configure validation rules and dataset paths in:

```text
edqp/config/settings.yaml
```

---

## Usage

Run the pipeline.

```bash
python run_pipeline.py
```

Launch the dashboard.

```bash
streamlit run dashboard.py
```

Run unit tests.

```bash
pytest
```

---

## Dashboard

The Streamlit dashboard provides:

- Data quality score
- Pipeline execution history
- Execution time trend
- Rule failure analysis
- AI-generated quality summary

> Add a dashboard screenshot here after deployment.

---

## Future Improvements

- Snowflake data loading
- Additional validation rules
- Docker support
- Apache Airflow orchestration
- Data profiling
- Multi-dataset processing

---

## License

This project is licensed under the MIT License.