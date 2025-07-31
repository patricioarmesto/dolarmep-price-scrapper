#!/usr/bin/env python3
"""
Example usage of the Dólar MEP scraper
"""

from main import DolarMepScraper


def example_basic_usage():
    """Basic usage example"""
    print("=== Basic Usage Example ===")
    scraper = DolarMepScraper()
    
    # Scrape current year months only
    months = ["enero-2025", "febrero-2025", "marzo-2025", "abril-2025", "mayo-2025", "junio-2025", "julio-2025"]
    scraper.run(months)


def example_multiple_years():
    """Example with multiple years"""
    print("\n=== Multiple Years Example ===")
    scraper = DolarMepScraper()
    
    # Try to scrape multiple years (sample months)
    months = ["enero-2023", "julio-2023", "diciembre-2023", 
              "enero-2024", "julio-2024", "diciembre-2024", 
              "enero-2025", "julio-2025"]
    scraper.run(months)


def example_custom_months():
    """Example with custom months"""
    print("\n=== Custom Months Example ===")
    scraper = DolarMepScraper()
    
    # You can modify this list to scrape different months
    custom_months = ["enero-2025", "febrero-2025", "marzo-2025", "abril-2025", "mayo-2025", "junio-2025", "julio-2025"]
    scraper.run(custom_months)


def example_specific_period():
    """Example for a specific time period"""
    print("\n=== Specific Period Example ===")
    scraper = DolarMepScraper()
    
    # Scrape a specific period (e.g., last 6 months of 2024 and first 6 months of 2025)
    specific_months = [
        "julio-2024", "agosto-2024", "septiembre-2024", "octubre-2024", "noviembre-2024", "diciembre-2024",
        "enero-2025", "febrero-2025", "marzo-2025", "abril-2025", "mayo-2025", "junio-2025"
    ]
    scraper.run(specific_months)


if __name__ == "__main__":
    print("Dólar MEP Scraper Examples")
    print("=" * 40)
    
    # Run examples
    example_basic_usage()
    example_multiple_years()
    example_custom_months()
    example_specific_period()
    
    print("\nExamples completed!")
    print("Check the 'output' directory for CSV files.") 