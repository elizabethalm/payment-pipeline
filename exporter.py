import pandas as pd 
import os
from datetime import datetime

def export_results(results):
    output_dir = "data/output"
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y_%m")

    results["by_month"].to_csv(f"{output_dir}/by_month_{timestamp}.csv", index=False)
    results["by_type"].to_csv(f"{output_dir}/by_type_{timestamp}.csv", index=False)
    results["failed"].to_csv(f"{output_dir}/failed_transactions_{timestamp}.csv", index=False)  

    print(f"Files saved to {output_dir}/")
    