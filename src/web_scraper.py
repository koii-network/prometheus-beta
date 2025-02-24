import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Optional

def scrape_webpage(url: str, selectors: Dict[str, str]) -> Optional[Dict[str, List[str]]]:
    """
    Scrape data from a given webpage using CSS selectors.
    
    Args:
        url (str): The URL of the webpage to scrape
        selectors (Dict[str, str]): A dictionary of data keys and their corresponding CSS selectors
    
    Returns:
        Optional[Dict[str, List[str]]]: A dictionary of scraped data or None if scraping fails
    
    Raises:
        ValueError: If URL is invalid or empty
        requests.RequestException: For network-related errors
    """
    # Validate input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL provided")
    
    if not selectors:
        raise ValueError("No selectors provided")
    
    try:
        # Send a GET request to the webpage
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Scrape data based on selectors
        scraped_data = {}
        for key, selector in selectors.items():
            elements = soup.select(selector)
            scraped_data[key] = [elem.get_text(strip=True) for elem in elements]
        
        return scraped_data
    
    except requests.RequestException as e:
        # Handle network-related errors
        print(f"Error fetching webpage: {e}")
        return None
    except Exception as e:
        # Handle other unexpected errors
        print(f"Unexpected error during scraping: {e}")
        return None