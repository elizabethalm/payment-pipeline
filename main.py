import logging
from generator import generate_transactions
from processor import process_transactions
from exporter import export_results

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

transactions = generate_transactions()
logging.info(f"Generated {len(transactions)} transactions")

results = process_transactions(transactions)
logging.info("Transactions processed")

export_results(results)
logging.info("Pipeline complete")
