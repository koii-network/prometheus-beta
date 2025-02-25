import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional

def scrape_webpage(url: str, tag: str, class_name: Optional[str] = None) -> List[str]:
    """
    Scrape specific elements from a given web page.
    
    Args:
        url (str): The URL of the webpage to scrape
        tag (str): HTML tag to extract (e.g., 'div', 'p', 'a')
        class_name (Optional[str]): Optional class name to filter elements
    
    Returns:
        List[str]: List of text contents of the scraped elements
    
    Raises:
        ValueError: If the URL is invalid or cannot be accessed
        RuntimeError: If no elements are found
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find elements based on tag and optional class
        if class_name:
            elements = soup.find_all(tag, class_=class_name)
        else:
            elements = soup.find_all(tag)
        
        # Extract text from elements
        if not elements:
            raise RuntimeError(f"No {tag} elements found on the page")
        
        return [element.get_text(strip=True) for element in elements]
    
    except requests.RequestException as e:
        raise ValueError(f"Error accessing URL: {e}") from e