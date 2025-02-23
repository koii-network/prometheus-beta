import requests
from typing import Dict, Any, Optional

def send_http_post_request(
    url: str, 
    data: Optional[Dict[str, Any]] = None, 
    headers: Optional[Dict[str, str]] = None, 
    timeout: int = 10
) -> Dict[str, Any]:
    """
    Send an HTTP POST request to the specified URL.

    Args:
        url (str): The target URL for the POST request.
        data (dict, optional): JSON payload to send. Defaults to None.
        headers (dict, optional): Additional HTTP headers. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        dict: Response from the server as a dictionary.

    Raises:
        ValueError: If URL is empty or invalid.
        requests.RequestException: For network-related errors.
    """
    # Validate URL
    if not url or not url.startswith(('http://', 'https://')):
        raise ValueError("Invalid or empty URL")

    # Set default headers if not provided
    if headers is None:
        headers = {'Content-Type': 'application/json'}

    try:
        # Send POST request
        response = requests.post(
            url, 
            json=data, 
            headers=headers, 
            timeout=timeout
        )
        
        # Raise an exception for bad HTTP responses
        response.raise_for_status()
        
        # Return JSON response if possible, else return text
        return response.json() if response.text else {}
    
    except requests.RequestException as e:
        # Propagate request-related exceptions
        raise