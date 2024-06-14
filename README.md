# Tunisia_Stock_Market

This project aims to develop a predictive model for forecasting stock prices in the Tunisian stock market using historical data and machine learning techniques.

## Project Structure

The project is organized as follows:

- [`notebooks/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FKahla%2FOneDrive%2FDocuments%2FTunisia_Stock_Market%2Fnotebooks%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\Kahla\OneDrive\Documents\Tunisia_Stock_Market\notebooks\"): Contains Jupyter notebooks for data analysis and preprocessing.
  - `check_data.ipynb`: Notebook for initial data checking.
  - `Data_Preprocessing.ipynb`: Notebook for data cleaning and preprocessing.
  - `data/`: Directory containing various stages of stock market data.
    - `weekly_stock_market.csv`: Raw weekly stock market data.
    - `checked_weekly_stock_market.csv`: Data after initial checks.
    - `cleaned_weekly_stock_market.csv`: Data after cleaning.
    - `normalized_weekly_stock_market.csv`: Data after normalization.
- [`stock_scraper/`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FKahla%2FOneDrive%2FDocuments%2FTunisia_Stock_Market%2Fstock_scraper%2F%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\Kahla\OneDrive\Documents\Tunisia_Stock_Market\stock_scraper\"): Contains the web scraping scripts to collect stock market data.
  - `companies_data/`: JSON files with data for individual companies.
  - `companies.json`: List of companies to scrape.
  - `import_test.py`: Script for testing data import functionality.
  - `scrapy.cfg`: Configuration file for Scrapy.
- [`README.md`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FKahla%2FOneDrive%2FDocuments%2FTunisia_Stock_Market%2FREADME.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\Kahla\OneDrive\Documents\Tunisia_Stock_Market\README.md"): This file, containing project documentation.
- [`requirements.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FKahla%2FOneDrive%2FDocuments%2FTunisia_Stock_Market%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\Kahla\OneDrive\Documents\Tunisia_Stock_Market\requirements.txt"): List of Python libraries required for the project.

## Requirements

To ensure you have all the necessary dependencies for the Tunisia Stock Market Prediction project, you can use the [`requirements.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FKahla%2FOneDrive%2FDocuments%2FTunisia_Stock_Market%2Frequirements.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\Kahla\OneDrive\Documents\Tunisia_Stock_Market\requirements.txt") file provided in the repository. This file includes all the required libraries and frameworks for data analysis, machine learning, deep learning, web scraping, and web development.

### Installation

1. **Clone the Repository:**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/tunisia-stock-market-prediction.git
   cd tunisia-stock-market-prediction
   ```

2. **Create a Virtual Environment:**

   Next, create a new virtual environment using Python 3. You can create a new virtual environment using `venv`:

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install the Required Libraries:**

   You can install the required libraries using the following command:

   ```bash
   pip install -r requirements.txt
   ```