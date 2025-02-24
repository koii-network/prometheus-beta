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

        # Extract unique data from elements
        scraped_data = []
        seen = set()  # To track unique entries
        for element in elements:
            # Skip elements that have already been processed
            if element in seen:
                continue

            # Extract text and href, using empty string if no href
            href = element.get('href', '') or ''
            text = element.get_text(strip=True)

            # Create a unique key to prevent duplicates
            key = (text, href)
            
            if key not in seen:
                item = {
                    'text': text,
                    'href': href
                }
                scraped_data.append(item)
                seen.add(key)

        return scraped_data

    except requests.RequestException as e:
        raise ConnectionError(f"Error fetching web page: {e}")
    except Exception as e:
        raise RuntimeError(f"Error parsing web page: {e}")