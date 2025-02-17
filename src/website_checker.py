import requests
import socket
import urllib3

def is_website_online(url, timeout=5):
    """
    Check if a website is online by attempting to connect to it.
    
    Args:
        url (str): The full URL of the website to check (including http:// or https://)
        timeout (int, optional): Connection timeout in seconds. Defaults to 5.
    
    Returns:
        bool: True if the website is online, False otherwise
    """
    # Disable SSL warnings to prevent noise in output
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    try:
        # Attempt to get the URL with a timeout and verify=False to handle various SSL scenarios
        response = requests.get(url, timeout=timeout, verify=False)
        
        # Check if the response was successful (status code 200-299)
        return 200 <= response.status_code < 300
    
    except (requests.ConnectionError, 
            requests.Timeout, 
            requests.RequestException, 
            socket.error):
        # Any connection error means the website is not accessible
        return False