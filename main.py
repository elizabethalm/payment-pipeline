from generator import generate_transactions
from processor import process_transactions

transactions = generate_transactions()
results = process_transactions(transactions)

print(f"Total transactions: {len(transactions)}")
print(f"\nBy month:\n{results['by_month']}")
print(f"\nBy type:\n{results['by_type']}")
print(f"\nFailed transactions: {len(results['failed'])}")
