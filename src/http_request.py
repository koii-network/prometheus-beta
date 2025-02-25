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
        dict: A dictionary containing the response details:
            - 'status_code': HTTP status code of the response
            - 'content': Response content as text
            - 'headers': Response headers
            - 'json': JSON response (if applicable, else None)

    Raises:
        requests.RequestException: For any network-related errors
    """
    try:
        # Send the GET request
        response = requests.get(
            url, 
            headers=headers, 
            params=params, 
            timeout=timeout
        )
        
        # Raise an exception for bad status codes
        response.raise_for_status()
        
        # Prepare response dictionary
        response_data = {
            'status_code': response.status_code,
            'content': response.text,
            'headers': dict(response.headers),
            'json': response.json() if response.headers.get('content-type', '').startswith('application/json') else None
        }
        
        return response_data
    
    except requests.RequestException as e:
        # Handle and re-raise any request-related exceptions
        raise