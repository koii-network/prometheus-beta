import requests

def is_website_online(url: str, timeout: float = 5.0) -> bool:
    """
    Check if a website is online by attempting to establish a connection.

    Args:
        url (str): The full URL of the website to check (e.g., 'https://www.example.com')
        timeout (float, optional): Maximum time to wait for a response. Defaults to 5.0 seconds.

    Returns:
        bool: True if the website is online and responsive, False otherwise.

    Raises:
        ValueError: If the URL is empty or invalid.
        TypeError: If the URL is not a string.
    """
    # Validate input
    if not isinstance(url, str):
        raise TypeError("URL must be a string")
    
    # Strip whitespace and check if URL is empty
    url = url.strip()
    if not url:
        raise ValueError("URL cannot be empty")
    
    # Ensure URL starts with http:// or https://
    if not url.startswith(('http://', 'https://')):
        url = f'https://{url}'
    
    try:
        # Send a HEAD request with a timeout
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        
        # Check if the response indicates a successful connection
        return response.status_code < 400
    
    except (requests.ConnectionError, requests.Timeout, requests.RequestException):
        # Catch various network-related errors
        return False