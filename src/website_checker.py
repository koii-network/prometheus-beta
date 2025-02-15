import requests

def is_website_online(url: str, timeout: int = 5) -> bool:
    """
    Check if a website is online by attempting to connect to it.
    
    Args:
        url (str): The full URL of the website to check (including http:// or https://)
        timeout (int, optional): Connection timeout in seconds. Defaults to 5.
    
    Returns:
        bool: True if the website is online, False otherwise
    
    Raises:
        ValueError: If the URL is invalid or empty
    """
    # Validate URL input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")
    
    # Ensure URL starts with http:// or https://
    if not url.startswith(('http://', 'https://')):
        url = f'https://{url}'
    
    try:
        # Send a HEAD request to check website availability
        response = requests.head(url, timeout=timeout)
        
        # Check if the response status code indicates success
        return response.status_code < 400
    
    except (requests.ConnectionError, requests.Timeout, requests.RequestException):
        # Any connection-related error means the website is not accessible
        return False