import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Optional

def scrape_webpage(url: str, selector: Optional[str] = None) -> Dict[str, List[str]]:
    """
    Scrape data from a given web page.
    
    Args:
        url (str): The URL of the webpage to scrape
        selector (Optional[str]): CSS selector to extract specific elements. 
                                  If None, extracts all text from the page.
    
    Returns:
        Dict[str, List[str]]: A dictionary containing scraped data
        
    Raises:
        ValueError: If the URL is invalid or cannot be accessed
        ConnectionError: If there's a network-related error
    """
    # Validate URL
    if not url.startswith(('http://', 'https://')):
        raise ValueError("Invalid URL. Must start with http:// or https://")
    
    try:
        # Send GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract data based on selector or whole page
        if selector:
            elements = soup.select(selector)
            # Extract text from selected elements
            scraped_data = [elem.get_text(strip=True) for elem in elements]
        else:
            # If no selector, extract all text
            scraped_data = [text for text in soup.stripped_strings]
        
        return {
            'url': url,
            'data': scraped_data
        }
    
    except requests.RequestException as e:
        raise ConnectionError(f"Error accessing webpage: {str(e)}")