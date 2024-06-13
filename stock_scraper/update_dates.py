import os
import json
from datetime import datetime, timedelta

def update_json_file(file_path):
    # Function to convert days since epoch to date string
    def days_to_date(days):
        epoch = datetime(1970, 1, 1)
        return (epoch + timedelta(days=days)).strftime("%d/%m/%Y")

    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    if file_path.endswith('.json'):
        with open(file_path, 'r+') as f:
            data = json.load(f)
            if "QuoteTab" in data:
                start_date = datetime.strptime("16/06/2014", "%d/%m/%Y")
                current_date = start_date

                for item in data["QuoteTab"]:
                    if "d" in item :
                        item["d"] = days_to_date((current_date - datetime(1970, 1, 1)).days)
                        current_date += timedelta(weeks=1)
                print(data)
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

def main():
    update_json_file("stock_scraper/data/stock_data.json")