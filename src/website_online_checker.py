import requests

def is_website_online(url: str, timeout: int = 5) -> bool:
    """
    Check if a website is online by attempting to connect to it.
    
    Args:
        url (str): The full URL of the website to check (including http:// or https://)
        timeout (int, optional): Number of seconds to wait before timing out. Defaults to 5.
    
    Returns:
        bool: True if the website is online, False otherwise
    """
    try:
        # Attempt to send a GET request to the URL
        response = requests.get(url, timeout=timeout)
        
        # Check if the response status code is in the 200-299 range (successful responses)
        return 200 <= response.status_code < 300
    
    except (requests.ConnectionError, requests.Timeout, requests.RequestException):
        # If any connection or request error occurs, the website is considered offline
        return False