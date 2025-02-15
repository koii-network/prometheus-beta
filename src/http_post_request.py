import requests

def send_http_post_request(url, data=None, headers=None, timeout=10):
    """
    Send an HTTP POST request to the specified URL.

    Args:
        url (str): The URL to send the POST request to.
        data (dict, optional): The payload to send in the request. Defaults to None.
        headers (dict, optional): Custom headers for the request. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        dict: A dictionary containing the response details.
    """
    try:
        # Set default headers if not provided
        if headers is None:
            headers = {'Content-Type': 'application/json'}

        # Send the POST request
        response = requests.post(
            url, 
            json=data, 
            headers=headers, 
            timeout=timeout
        )

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Return a comprehensive response dictionary
        return {
            'status_code': response.status_code,
            'text': response.text,
            'json': response.json() if response.text else None,
            'headers': dict(response.headers)
        }

    except requests.exceptions.RequestException as e:
        # Handle various request-related exceptions
        return {
            'error': str(e),
            'status_code': None,
            'text': None,
            'json': None
        }