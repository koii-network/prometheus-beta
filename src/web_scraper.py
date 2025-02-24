import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional


def scrape_web_page(url: str, selector: Optional[str] = None) -> List[Dict[str, str]]:
    """
    Scrape data from a given web page using optional CSS selector.

    Args:
        url (str): The URL of the web page to scrape.
        selector (Optional[str], optional): CSS selector to target specific elements. 
                                            Defaults to None (scrape entire page).

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing scraped data.
                               Each dictionary represents an element with its text and href.

    Raises:
        ValueError: If the URL is invalid or empty.
        ConnectionError: If there's a network-related error.
        RuntimeError: If the page cannot be parsed.
    """
    # Validate input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL provided")

    try:
        # Send a GET request with a user agent to mimic browser behavior
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        # Raise an exception for bad status codes
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Select elements based on the provided selector or use default
        elements = soup.select(selector) if selector else soup.find_all()

        # Extract data from elements
        scraped_data = []
        for element in elements:
            item = {
                'text': element.get_text(strip=True),
                'href': element.get('href', '')
            }
            scraped_data.append(item)

        return scraped_data

    except requests.RequestException as e:
        raise ConnectionError(f"Error fetching web page: {e}")
    except Exception as e:
        raise RuntimeError(f"Error parsing web page: {e}")