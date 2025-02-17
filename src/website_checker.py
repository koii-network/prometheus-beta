import requests

def is_website_online(url, timeout=5):
    """
    Check if a website is online and reachable.
    
    Args:
        url (str): The URL of the website to check
        timeout (int, optional): Number of seconds to wait for a response. Defaults to 5.
    
    Returns:
        bool: True if the website is online, False otherwise
    """
    try:
        # Ensure the URL starts with http:// or https://
        if not url.startswith(('http://', 'https://')):
            url = f'https://{url}'
        
        # Send a GET request with a timeout
        response = requests.get(url, timeout=timeout)
        
        # Check if the response status code is successful (200-299 range)
        return 200 <= response.status_code < 300
    
    except (requests.ConnectionError, requests.Timeout, requests.RequestException):
        # If any connection or request error occurs, the website is considered offline
        return False