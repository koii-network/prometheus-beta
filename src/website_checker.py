import requests

def is_website_online(url):
    """
    Check if a website is online by attempting to connect to it.
    
    Args:
        url (str): The URL of the website to check (should include protocol, e.g., 'https://')
    
    Returns:
        bool: True if the website is online, False otherwise
    
    Raises:
        ValueError: If the URL is invalid or empty
    """
    # Validate input
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string")
    
    # Ensure URL has a protocol
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    try:
        # Send a HEAD request with a short timeout
        response = requests.head(url, timeout=5)
        
        # Check if the response status code indicates success
        return response.status_code < 400
    
    except (requests.ConnectionError, requests.Timeout, requests.RequestException):
        # If there's any connection error, the website is considered offline
        return False