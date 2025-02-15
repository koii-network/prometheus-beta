import requests

def is_website_online(url):
    """
    Check if a website is online by sending a GET request.
    
    Args:
        url (str): The full URL of the website to check (including http:// or https://)
    
    Returns:
        bool: True if the website is online (returns a 200 OK status), False otherwise
    
    Raises:
        ValueError: If the URL is empty or None
        TypeError: If the URL is not a string
    """
    # Validate input
    if url is None:
        raise ValueError("URL cannot be None")
    
    if not isinstance(url, str):
        raise TypeError("URL must be a string")
    
    # Remove any whitespace and check if URL is empty
    url = url.strip()
    if not url:
        raise ValueError("URL cannot be empty")
    
    try:
        # Send a GET request with a timeout to prevent hanging
        response = requests.get(url, timeout=5)
        
        # Check if the response status code is in the 200-299 range (successful responses)
        return 200 <= response.status_code < 300
    
    except (requests.ConnectionError, requests.Timeout, requests.RequestException):
        # If there's any connection error, the website is considered offline
        return False