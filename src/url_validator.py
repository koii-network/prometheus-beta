import re
from urllib.parse import urlparse

def is_valid_url(url: str) -> bool:
    """
    Check if a given string is a valid URL.
    
    Args:
        url (str): The URL string to validate.
    
    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    if not isinstance(url, str):
        return False
    
    # Remove leading/trailing whitespace
    url = url.strip()
    
    # Check if the URL is empty
    if not url:
        return False
    
    try:
        # Use urlparse to check basic URL structure
        result = urlparse(url)
        
        # Check if scheme and netloc are present
        # Schemes like http, https, ftp are valid
        # Also allow custom schemes like mailto:, file:, etc.
        return all([result.scheme, result.netloc])
    
    except Exception:
        return False