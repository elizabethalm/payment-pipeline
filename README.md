# payment-pipeline

A Python pipeline that generates 500 fictional financial transactions,
processes them, and exports the results as CSV files.

## About

Built as part of my Data Engineering portfolio to practice Python project
structure, modular code, and automated data pipelines.

## What it does

- Generates 500 transactions with random type (PIX, TED, boleto),
amount, date, and status
- Groups results by month and payment type
- Identifies failed transactions
- Exports 3 CSV files to `data/output/`

## Requirements

- Python 3.x

```bash
pip install -r requirements.txt
```

## How to run

```bash
python3 main.py
```

## Project structure
payment-pipeline/

├── main.py         # orchestrates the pipeline

├── generator.py    # generates fictional transactions

├── processor.py    # processes and groups data

├── exporter.py     # exports results to CSV

├── utils.py        # helper functions

└── data/output/    # generated CSV files (git ignored)