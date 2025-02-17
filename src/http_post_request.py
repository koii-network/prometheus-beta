import requests

def send_http_post_request(url, data=None, headers=None, timeout=10):
    """
    Send an HTTP POST request to the specified URL.

    Args:
        url (str): The URL to send the POST request to.
        data (dict, optional): The payload to send with the request. Defaults to None.
        headers (dict, optional): Custom headers to include with the request. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        dict: A dictionary containing the response status code and JSON response body.

    Raises:
        requests.RequestException: If there's an error during the request.
    """
    try:
        # Set default headers if not provided
        if headers is None:
            headers = {'Content-Type': 'application/json'}

        # Send POST request
        response = requests.post(url, json=data, headers=headers, timeout=timeout)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()

        return {
            'status_code': response.status_code,
            'json': response.json() if response.content else None
        }
    except requests.RequestException as e:
        # Handle request exceptions
        return {
            'status_code': getattr(e.response, 'status_code', None),
            'error': str(e)
        }