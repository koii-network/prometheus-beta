import requests

def is_website_online(url, timeout=5):
    """
    Check if a website is online by attempting to connect to it.
    
    Args:
        url (str): The full URL of the website to check (e.g., 'https://www.example.com')
        timeout (int, optional): Number of seconds to wait before timing out. Defaults to 5.
    
    Returns:
        bool: True if the website is online, False otherwise
    """
    try:
        # Add scheme if not present
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        # Send a HEAD request which is faster than a full GET
        response = requests.head(url, timeout=timeout)
        
        # Check if the response status code is successful (200-299 range)
        return 200 <= response.status_code < 300
    
    except (requests.ConnectionError, requests.Timeout, requests.RequestException):
        return False