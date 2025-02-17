import requests

def is_website_online(url, timeout=5):
    """
    Check if a website is online by attempting to connect to it.
    
    Args:
        url (str): The URL of the website to check
        timeout (int, optional): Connection timeout in seconds. Defaults to 5.
    
    Returns:
        bool: True if website is online, False otherwise
    
    Raises:
        ValueError: If the URL is invalid or empty
    """
    # Validate input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL provided")
    
    # Ensure URL starts with http:// or https://
    if not url.startswith(('http://', 'https://')):
        url = f'https://{url}'
    
    try:
        # Send a HEAD request to check website availability
        response = requests.head(url, timeout=timeout)
        
        # Check if request was successful (status code 200-299)
        return 200 <= response.status_code < 300
    except (requests.ConnectionError, requests.Timeout):
        # Connection failed or timed out
        return False
    except requests.RequestException:
        # Any other request-related exception
        return False