import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Optional

def scrape_webpage(url: str, tag: str = 'p', attr: Optional[Dict[str, str]] = None) -> List[str]:
    """
    Scrape text content from a web page based on specified HTML tag and optional attributes.

    Args:
        url (str): The URL of the webpage to scrape
        tag (str, optional): HTML tag to extract. Defaults to 'p' (paragraphs)
        attr (Dict[str, str], optional): Optional dictionary of attributes to filter tags

    Returns:
        List[str]: List of text content extracted from matching tags

    Raises:
        ValueError: If the URL is invalid or cannot be reached
        ConnectionError: If there's a network connection issue
    """
    try:
        # Send GET request to the URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find tags with optional attribute filtering
        if attr:
            elements = soup.find_all(tag, attrs=attr)
        else:
            elements = soup.find_all(tag)

        # Extract text from elements, strip whitespace
        results = [element.get_text(strip=True) for element in elements if element.get_text(strip=True)]

        return results

    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error accessing webpage: {e}") from e
    except Exception as e:
        raise ValueError(f"Unexpected error during web scraping: {e}") from e