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
        # Use urlparse to validate the basic structure of the URL
        parsed_url = urlparse(url)
        
        # Check for scheme and netloc (essential parts of a valid URL)
        # Use regex to ensure scheme is valid (http, https, ftp, etc.)
        # and netloc contains at least a domain name
        return all([
            re.match(r'^(http|https|ftp|ftps|file|gopher|telnet|nntp|imap|wais|mailto|mms|rtsp|svn)$', parsed_url.scheme, re.IGNORECASE),
            parsed_url.netloc,  # Must have a non-empty network location
            # More flexible regex to support URLs with userinfo, various domain formats
            re.match(r'^(([a-zA-Z0-9_.-]+:?[a-zA-Z0-9_.-]+@)?)(localhost|([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)*[a-zA-Z]{2,}|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$', parsed_url.netloc)
        ])
    except Exception:
        return False