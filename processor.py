import pandas as pd

def process_transactions(transactions):
    df = pd.DataFrame(transactions)
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    #Group by month
    by_month = df.groupby("month")["amount"].sum().reset_index()
    by_month.columns = ["month","total_amount"]

    #Group by type
    by_type = df.groupby("type")["amount"].sum().reset_index()
    by_type.columns = ["type","total_amount"]
    
    #Failed transactions
    failed = df[df["status"] == "failed"]
    
    return {
        "by_month": by_month,
        "by_type": by_type,
        "failed": failed

    }