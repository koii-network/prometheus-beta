import re
from urllib.parse import urlparse

def is_valid_url(url: str) -> bool:
    """
    Check if a given string is a valid URL.
    
    Args:
        url (str): The URL string to validate
    
    Returns:
        bool: True if the URL is valid, False otherwise
    """
    # Check if the input is a string and not empty
    if not isinstance(url, str) or not url:
        return False
    
    try:
        # Use urlparse to break down the URL
        result = urlparse(url)
        
        # Check if the URL has a valid scheme (protocol) and network location (domain)
        return all([
            result.scheme in ['http', 'https', 'ftp', 'sftp'],  # Common valid schemes
            result.netloc,  # Must have a domain/network location
            # Optional: Additional regex validation for domain format
            re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', result.netloc) is not None
        ])
    except Exception:
        return False