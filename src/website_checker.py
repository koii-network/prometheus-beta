import requests

def is_website_online(url: str, timeout: float = 5.0) -> bool:
    """
    Check if a website is online and accessible.

    Args:
        url (str): The URL of the website to check
        timeout (float, optional): Connection timeout in seconds. Defaults to 5.0.

    Returns:
        bool: True if the website is online, False otherwise

    Raises:
        ValueError: If the URL is invalid or empty
    """
    # Validate input
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string")

    # Ensure URL has a scheme
    if not url.startswith(('http://', 'https://')):
        url = f'https://{url}'

    try:
        # Send a HEAD request to check website availability
        response = requests.head(url, timeout=timeout)
        
        # Check if the response status code indicates success
        return 200 <= response.status_code < 400
    
    except (requests.ConnectionError, requests.Timeout, requests.RequestException):
        # Any connection or request errors indicate the website is not online
        return False