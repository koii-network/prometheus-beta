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
    if not isinstance(url, str) or not url.strip():
        return False
    
    try:
        # Use urlparse to break down the URL
        parsed_url = urlparse(url)
        
        # Check for required components
        # Require scheme (http, https, etc.) and netloc (domain)
        return all([
            parsed_url.scheme,  # Must have a scheme
            parsed_url.netloc,  # Must have a domain/network location
            # Optional: Additional regex for more strict validation
            re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*://', url)  # Validate scheme syntax
        ])
    except Exception:
        return False