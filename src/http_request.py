import requests
from typing import Dict, Any, Optional

def send_get_request(url: str, 
                     params: Optional[Dict[str, Any]] = None, 
                     headers: Optional[Dict[str, str]] = None,
                     timeout: int = 10) -> Dict[str, Any]:
    """
    Send an HTTP GET request to the specified URL.
    
    Args:
        url (str): The URL to send the GET request to.
        params (dict, optional): Optional query parameters to include in the request.
        headers (dict, optional): Optional headers to include in the request.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.
    
    Returns:
        dict: A dictionary containing the response details.
        
    Raises:
        requests.RequestException: For any network-related errors.
    """
    try:
        # Send the GET request with optional parameters and headers
        response = requests.get(
            url, 
            params=params, 
            headers=headers, 
            timeout=timeout
        )
        
        # Raise an exception for bad HTTP responses
        response.raise_for_status()
        
        # Return a dictionary with response details
        return {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'content': response.text,
            'json': response.json() if response.headers.get('content-type', '').startswith('application/json') else None
        }
    except requests.RequestException as e:
        # Handle and re-raise any request-related exceptions
        raise