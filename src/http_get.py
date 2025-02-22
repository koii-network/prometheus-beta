import requests

def send_http_get_request(url, headers=None, params=None, timeout=10):
    """
    Send an HTTP GET request to the specified URL.
    
    Args:
        url (str): The URL to send the GET request to.
        headers (dict, optional): Optional headers to include in the request.
        params (dict, optional): Optional query parameters to include in the request.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.
    
    Returns:
        dict: A dictionary containing the response status code and content.
    
    Raises:
        ValueError: If the URL is empty or None.
        requests.RequestException: For network-related errors.
    """
    # Validate URL
    if not url:
        raise ValueError("URL cannot be empty")
    
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
        
        # Return response details
        return {
            'status_code': response.status_code,
            'content': response.text,
            'headers': dict(response.headers)
        }
    
    except requests.RequestException as e:
        # Handle any request-related exceptions
        raise RuntimeError(f"HTTP GET request failed: {str(e)}")