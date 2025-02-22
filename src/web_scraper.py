import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional

def scrape_webpage(url: str, selector: str) -> List[Dict[str, str]]:
    """
    Scrape data from a web page using a specified CSS selector.
    
    Args:
        url (str): The URL of the webpage to scrape
        selector (str): A CSS selector to find elements
    
    Returns:
        List[Dict[str, str]]: A list of dictionaries containing scraped data
    
    Raises:
        ValueError: If the URL is invalid or cannot be accessed
        RuntimeError: If no elements are found matching the selector
    """
    try:
        # Validate URL
        if not url.startswith(('http://', 'https://')):
            raise ValueError("Invalid URL: Must start with http:// or https://")
        
        # Send GET request
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find elements
        elements = soup.select(selector)
        
        if not elements:
            raise RuntimeError(f"No elements found matching selector: {selector}")
        
        # Extract data
        results = []
        for element in elements:
            # Create a dictionary with text and href (if available)
            item = {
                'text': element.get_text(strip=True),
                'href': element.get('href', '') or ''
            }
            results.append(item)
        
        return results
    
    except requests.RequestException as e:
        raise ValueError(f"Error accessing webpage: {str(e)}") from e