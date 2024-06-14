import csv
import json
import os

def join_json_data_to_csv(directory, csv_filename):
    data_rows = []

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                company_name = data['Name']
                for quote in data['QuoteTab']:
                    row = (
                        company_name,
                        quote['d'],
                        quote['o'],
                        quote['h'],
                        quote['l'],
                        quote['c'],
                        quote['v']
                    )
                    data_rows.append(row)

    with open(csv_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        header = ['companyName', 'date', 'openingPrice', 'highestPrice', 'lowestPrice', 'closingPrice', 'volume']
        csvwriter.writerow(header)
        csvwriter.writerows(data_rows)
