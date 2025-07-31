import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
from datetime import datetime
import os


class DolarMepScraper:
    def __init__(self):
        self.base_url = "https://dolarhistorico.com/cotizacion-dolar-mep/mes"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def get_page_content(self, url):
        """Fetch page content with error handling"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def parse_table_data(self, soup, month_year):
        """Extract data from the main table on the page"""
        data = []
        
        # Extract year from month_year string (e.g., "enero-2023" -> 2023)
        year = int(month_year.split('-')[1])
        
        # First, try to find the table with id "dataTable" as mentioned in the request
        table = soup.find('table', id='dataTable')
        if table:
            print(f"  Found table with id 'dataTable' for {month_year}")
        else:
            # Look for any table on the page
            tables = soup.find_all('table')
            print(f"  Found {len(tables)} tables on the page for {month_year}")
            
            # Try to find the most relevant table
            for i, table in enumerate(tables):
                rows = table.find_all('tr')
                if len(rows) >= 2:
                    header_row = rows[0]
                    header_cells = header_row.find_all(['td', 'th'])
                    header_text = ' '.join([cell.get_text(strip=True) for cell in header_cells])
                    print(f"    Table {i+1} headers: {header_text}")
        
        # Look for tables on the page
        tables = soup.find_all('table')
        
        for table in tables:
            rows = table.find_all('tr')
            if len(rows) < 2:  # Need at least header + 1 data row
                continue
                
            # Check if this table has the expected structure
            header_row = rows[0]
            header_cells = header_row.find_all(['td', 'th'])
            
            # Look for tables with fecha, compra, venta, and variación columns
            if len(header_cells) >= 4:
                for row in rows[1:]:  # Skip header row
                    cells = row.find_all(['td', 'th'])
                    if len(cells) >= 4:
                        fecha = cells[0].get_text(strip=True)
                        compra = cells[1].get_text(strip=True)
                        venta = cells[2].get_text(strip=True)
                        variacion = cells[3].get_text(strip=True)
                        
                        # Save raw string values as-is
                        if fecha:
                            data.append({
                                'fecha': fecha,
                                'compra': compra,
                                'venta': venta,
                                'variacion': variacion
                            })
        
        return data
    
    def scrape_month_data(self, month_year):
        """Scrape data for a specific month"""
        print(f"Scraping data for {month_year}...")
        
        # Construct URL for the specific month
        url = f"{self.base_url}/{month_year}"
        
        print(f"  Trying URL: {url}")
        content = self.get_page_content(url)
        if not content:
            print(f"  No content found for {month_year}")
            return []
        
        soup = BeautifulSoup(content, 'html.parser')
        data = self.parse_table_data(soup, month_year)
        
        if data:
            print(f"  Found {len(data)} records from {url}")
        else:
            print(f"  No data found from {url}")
        
        return data
    
    def scrape_all_months(self, months):
        """Scrape data for multiple months"""
        all_data = []
        
        for month in months:
            month_data = self.scrape_month_data(month)
            all_data.extend(month_data)
            
            # Add a small delay to be respectful to the server
            time.sleep(1)
        
        return all_data
    
    def save_to_csv(self, data, filename):
        """Save data to CSV file"""
        if not data:
            print("No data to save")
            return
        
        df = pd.DataFrame(data)
        
        # Reorder columns
        df = df[['fecha', 'compra', 'venta', 'variacion']]
        
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"Data saved to {filename}")
        print(f"Total records: {len(df)}")
    
    def run(self, months):
        """Main method to run the scraper"""
        print("Starting Dólar MEP scraper...")
        print(f"Target months: {len(months)} months")
        print("Note: Historical data availability depends on the website structure.")
        print("The scraper will attempt to extract available data for each month.")
        
        all_data = self.scrape_all_months(months)
        
        if all_data:
            # Create output directory if it doesn't exist
            os.makedirs('output', exist_ok=True)
            
            # Save to CSV
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"output/dolar_mep_historico_{timestamp}.csv"
            self.save_to_csv(all_data, filename)
            
            # Also save a version without timestamp
            filename_latest = "output/dolar_mep_historico_latest.csv"
            self.save_to_csv(all_data, filename_latest)
            
            print("Scraping completed successfully!")
        else:
            print("No data was scraped. Please check the website structure.")


def main():
    scraper = DolarMepScraper()
    
    months = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    years = ["2023","2024","2025"]

    target_months = []

    for year in years:
        for month in months:
            target_months.append(f"{month}-{year}")
    
    scraper.run(target_months)


if __name__ == "__main__":
    main()
