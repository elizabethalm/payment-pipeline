from faker import Faker
import random
from datetime import datetime

fake = Faker('pt_BR')

def generate_transactions(quantity=500):
    transactions = []

    for i in range(quantity):
        transaction = {
            "id": i + 1,
            "type": random.choice(["PIX","TED","boleto"]),
            "amount": round(random.uniform(10.0,5000.0),2),
            "date": fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d"),
            "status": random.choice(["processed","pending","failed"]),  
        }
        transactions.append(transaction)

    return transactions
    
