import requests

def send_http_get_request(url, headers=None, params=None, timeout=10):
    """
    Send an HTTP GET request to the specified URL.

    Args:
        url (str): The URL to send the GET request to.
        headers (dict, optional): Optional headers to include in the request. Defaults to None.
        params (dict, optional): Optional query parameters to include in the request. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        dict: A dictionary containing the response details.
            - 'status_code': HTTP status code of the response
            - 'content': Response content as text
            - 'headers': Response headers

    Raises:
        ValueError: If the URL is empty or None.
        requests.RequestException: For network-related errors.
    """
    # Validate input URL
    if not url:
        raise ValueError("URL cannot be empty or None")

    try:
        # Send GET request with optional headers, params, and timeout
        response = requests.get(
            url, 
            headers=headers, 
            params=params, 
            timeout=timeout
        )
        
        # Raise an exception for bad HTTP responses
        response.raise_for_status()

        # Return a comprehensive response dictionary
        return {
            'status_code': response.status_code,
            'content': response.text,
            'headers': dict(response.headers)
        }

    except requests.RequestException as e:
        # Handle network-related errors
        raise RuntimeError(f"HTTP GET request failed: {str(e)}")