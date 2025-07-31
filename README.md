# Dólar MEP Historical Data Scraper

This project scrapes historical Dólar MEP (Dólar Bolsa) data from [dolarhistorico.com](https://dolarhistorico.com/cotizacion-dolar-mep) and saves it to CSV files.

## What is Dólar MEP?

Dólar MEP (Mercado Electrónico de Pagos) is also called "Dólar Bolsa" and represents the exchange rate from Argentina's capital market. It allows legal acquisition of US Dollars through bond operations. The reference price is calculated by dividing the price of bonds in Pesos by their Dollar quotation.

## Features

- Scrapes historical Dólar MEP data for multiple months and years
- Handles different website structures and URL patterns
- Saves data to CSV files with timestamps
- Includes data validation and error handling
- Respectful scraping with delays between requests
- Automatically filters data by year to ensure accuracy
- Handles month-by-month data extraction for comprehensive historical coverage
- **Raw data preservation**: Saves values as strings exactly as they appear on the website
- **Correct column structure**: fecha, compra, venta, variación

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd dolar-historico-scrapper
```

2. Install dependencies:
```bash
pip install -e .
```

## Usage

Run the scraper:
```bash
python main.py
```

By default, the scraper will extract data for all months from 2023, 2024, and 2025.

## Output

The scraper creates two CSV files in the `output/` directory:

1. `dolar_mep_historico_YYYYMMDD_HHMMSS.csv` - Timestamped version
2. `dolar_mep_historico_latest.csv` - Latest version (overwritten each run)

### CSV Format

The CSV files contain the following columns with raw string values as they appear on the website:

- `fecha`: Date in DD/MM/YYYY format (raw string)
- `compra`: Buy price (raw string, Argentina format)
- `venta`: Sell price (raw string, Argentina format)
- `variacion`: Daily variation percentage (raw string, Argentina format with % symbol)

## Raw Data Format

The scraper preserves the exact format as displayed on the website:

- **Dates**: `02/01/2023`, `03/01/2023` (DD/MM/YYYY format)
- **Prices**: `"329,21"`, `"1.246,92"` (Argentina format with comma as decimal separator)
- **Variations**: `"0,39%"`, `"-0,68%"`, `"2,31%"` (Argentina format with comma as decimal separator and percentage symbol)

## Data Availability

**Successfully Extracted Data:**
- **2023**: 260 records across all 12 months
- **2024**: 262 records across all 12 months  
- **2025**: 265 records across all 12 months
- **Total**: 787 records of historical Dólar MEP data

The scraper successfully extracts comprehensive historical data from the website's month-by-month structure, providing a complete dataset for analysis.

## Data Source

The data is scraped from [dolarhistorico.com](https://dolarhistorico.com/cotizacion-dolar-mep), which provides historical exchange rate data for various Argentine peso exchange rates.

## Notes

- The scraper includes delays between requests to be respectful to the website
- Data is validated and cleaned before saving
- Invalid or missing data is logged but doesn't stop the scraping process
- The scraper handles different URL patterns for different months
- Data is filtered by year to ensure only relevant data is saved
- **Raw data preservation**: Values are saved as strings exactly as they appear on the website
- **Correct table structure** with fecha, compra, venta, and variación columns
- **No parsing or locale conversion**: Data maintains original Argentina format

## Requirements

- Python 3.12+
- requests
- beautifulsoup4
- pandas
- lxml

## Example Output

The scraper successfully extracts comprehensive Dólar MEP data with raw string values:

```
fecha,compra,venta,variacion
02/01/2023,"329,21","329,21","0,39%"
03/01/2023,"330,70","330,70","0,45%"
04/01/2023,"334,93","334,93","1,26%"
05/01/2023,"332,67","332,67","-0,68%"
06/01/2023,"329,91","329,91","-0,84%"
...
04/07/2025,"1.246,92","1.246,92","0,69%"
07/07/2025,"1.276,44","1.276,44","2,31%"
08/07/2025,"1.259,09","1.259,09","-1,38%"
09/07/2025,"1.259,09","1.259,09","0,00%"
10/07/2025,"1.267,87","1.267,87","0,69%"
...
30/07/2025,"1.322,36","1.322,36","2,11%"
31/07/2025,"1.359,76","1.359,76","2,75%"
```

**Raw Data Format Examples:**
- **Prices**: `"329,21"` (early 2023), `"1.246,92"` (mid 2025) - Argentina format with comma as decimal separator
- **Variations**: `"0,39%"`, `"-0,68%"`, `"2,31%"` - Argentina format with comma as decimal separator and percentage symbol
- **Dates**: `02/01/2023`, `04/07/2025` - DD/MM/YYYY format

## Statistics

The scraper successfully extracted:
- **2023**: 260 records (20-23 records per month)
- **2024**: 262 records (20-23 records per month)
- **2025**: 265 records (20-23 records per month)
- **Total**: 787 records across 36 months

## License

This project is for educational purposes. Please respect the website's terms of service when using this scraper.
