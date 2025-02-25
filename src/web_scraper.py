import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Optional

def scrape_webpage(url: str, selector: Optional[str] = None) -> Dict[str, List[str]]:
    """
    Scrape data from a given web page.
    
    Args:
        url (str): The URL of the webpage to scrape
        selector (Optional[str]): CSS selector to extract specific elements. 
                                  If None, returns all text content.
    
    Returns:
        Dict[str, List[str]]: A dictionary containing scraped data
        
    Raises:
        ValueError: If the URL is invalid or webpage cannot be accessed
        RuntimeError: If scraping fails
    """
    try:
        # Validate URL
        if not url.startswith(('http://', 'https://')):
            raise ValueError("Invalid URL. Must start with http:// or https://")
        
        # Send GET request
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract data based on selector or default to all text
        if selector:
            elements = soup.select(selector)
            if not elements:
                return {"data": []}
            
            scraped_data = [elem.get_text(strip=True) for elem in elements]
        else:
            # If no selector, get all text
            scraped_data = [text for text in soup.stripped_strings]
        
        return {
            "data": scraped_data,
            "url": url,
            "status_code": response.status_code
        }
    
    except requests.RequestException as e:
        raise ValueError(f"Error accessing webpage: {str(e)}") from e
    except Exception as e:
        raise RuntimeError(f"Scraping failed: {str(e)}") from e