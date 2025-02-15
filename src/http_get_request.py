import requests
from typing import Dict, Any, Optional

def send_http_get_request(url: str, 
                           headers: Optional[Dict[str, str]] = None, 
                           params: Optional[Dict[str, Any]] = None, 
                           timeout: int = 10) -> Dict[str, Any]:
    """
    Send an HTTP GET request to the specified URL.

    Args:
        url (str): The URL to send the GET request to.
        headers (Optional[Dict[str, str]], optional): Optional headers to include in the request. Defaults to None.
        params (Optional[Dict[str, Any]], optional): Optional query parameters to include in the request. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        Dict[str, Any]: A dictionary containing the response details.
        
    Raises:
        ValueError: If the URL is empty or invalid.
        requests.RequestException: For any network-related errors.
    """
    # Validate URL
    if not url or not url.startswith(('http://', 'https://')):
        raise ValueError("Invalid or empty URL")

    try:
        # Send GET request
        response = requests.get(
            url, 
            headers=headers, 
            params=params, 
            timeout=timeout
        )
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Return a comprehensive response dictionary
        return {
            'status_code': response.status_code,
            'text': response.text,
            'json': response.json() if response.headers.get('content-type', '').startswith('application/json') else None,
            'headers': dict(response.headers)
        }
    
    except requests.RequestException as e:
        # Handle network-related errors
        raise RuntimeError(f"HTTP GET request failed: {str(e)}")