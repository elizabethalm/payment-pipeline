from generator import generate_transactions

transactions = generate_transactions()
print(f"Total transactions generated: {len(transactions)}")
print(f"First transaction: {transactions[0]}")