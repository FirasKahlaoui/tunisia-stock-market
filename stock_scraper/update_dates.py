import os
import json
from datetime import datetime, timedelta

def update_json_file(file_path):
    def days_to_date(days):
        epoch = datetime(1970, 1, 1)
        return (epoch + timedelta(days=days)).strftime("%d/%m/%Y")

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
                    if "d" in item:
                        item["d"] = days_to_date((current_date - datetime(1970, 1, 1)).days)
                        current_date += timedelta(weeks=1)
                print(data)
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()

def main():
    folder_path = 'stock_scraper\companies_data'
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_path.endswith('.json'):
            update_json_file(file_path)

if __name__ == "__main__":
    main()