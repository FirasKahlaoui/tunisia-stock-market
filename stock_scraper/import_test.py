# test_imports.py
import sys
import os

# Add stock_scraper directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'stock_scraper'))

from utils.update_dates import update_json_file
from utils.join_data import join_json_data_to_csv

print("Imports successful!")
