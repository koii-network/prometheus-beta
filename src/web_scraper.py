import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional

def scrape_webpage(url: str, tag: str = 'p', class_name: Optional[str] = None) -> List[str]:
    """
    Scrape text content from a specified web page.

    Args:
        url (str): The URL of the webpage to scrape
        tag (str, optional): HTML tag to extract. Defaults to 'p' (paragraphs)
        class_name (str, optional): Specific class to filter elements. Defaults to None.

    Returns:
        List[str]: A list of text content extracted from the specified elements

    Raises:
        ValueError: If the URL is invalid or the request fails
        ConnectionError: If there's a network-related error
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=10)
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find elements based on tag and optional class
        if class_name:
            elements = soup.find_all(tag, class_=class_name)
        else:
            elements = soup.find_all(tag)
        
        # Extract and return text from elements
        return [element.get_text(strip=True) for element in elements if element.get_text(strip=True)]
    
    except requests.RequestException as e:
        raise ValueError(f"Error fetching webpage: {e}") from e
    except Exception as e:
        raise ValueError(f"Unexpected error during scraping: {e}") from e