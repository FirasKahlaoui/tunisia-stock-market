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

## Data Collection and Scraping Approach

The data for the Tunisian stock market is visualized on the website through canvas graphs, which do not allow for direct scraping of the data from the webpage's HTML. To overcome this challenge, we adopted a more technical approach by inspecting the network traffic to identify the server requests that fetch the stock data.

### Steps to Scrape Data from Canvas Graphs

1. **Inspect Network Traffic:**
   - Open the website where the stock market data is displayed.
   - Use the browser's Developer Tools (usually accessible by pressing `F12` or right-clicking and selecting "Inspect") to monitor the network traffic.
   - Navigate to the "Network" tab and filter by XHR (XMLHttpRequest) to observe the API calls made by the webpage.

2. **Identify Data Requests:**
   - Look for requests that fetch the stock data. These requests are often made to an API endpoint and return data in JSON format.
   - Analyze the request headers, method (GET or POST), and any query parameters or payloads used to retrieve the data.

3. **Craft Custom Requests with Scrapy:**
   - Using Scrapy, a popular web scraping framework in Python, create a spider to mimic the identified requests that fetch the stock data.
   - Ensure to include any required headers, cookies, or parameters identified in the previous step. This can involve setting custom headers or cookies in your Scrapy spider to ensure the server accepts and processes your request as if it were coming from a legitimate user.

4. **Parse and Save the Data:**
   - Once the data is retrieved, parse the JSON response to extract the necessary information.
   - Save the parsed data into a structured format like CSV or a database for further analysis or processing. This step is crucial for transforming the raw data into a usable format for data analysis, machine learning models, or any other intended use case.
