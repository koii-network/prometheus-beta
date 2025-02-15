import requests

def send_http_post_request(url, data=None, headers=None, timeout=10):
    """
    Send an HTTP POST request to the specified URL.

    Args:
        url (str): The URL to send the POST request to.
        data (dict, optional): The payload to send in the request. Defaults to None.
        headers (dict, optional): Custom headers for the request. Defaults to None.
        timeout (int, optional): Timeout for the request in seconds. Defaults to 10.

    Returns:
        dict: A dictionary containing the response details.
            - 'status_code': HTTP status code of the response
            - 'json': JSON response body (if applicable)
            - 'text': Raw text response body
            - 'headers': Response headers

    Raises:
        requests.RequestException: For network-related errors
        ValueError: For invalid input parameters
    """
    # Validate input parameters
    if not isinstance(url, str) or not url:
        raise ValueError("URL must be a non-empty string")

    # Set default headers if not provided
    if headers is None:
        headers = {'Content-Type': 'application/json'}

    try:
        # Send the POST request
        response = requests.post(
            url, 
            json=data, 
            headers=headers, 
            timeout=timeout
        )

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Prepare response details
        response_details = {
            'status_code': response.status_code,
            'text': response.text,
            'headers': dict(response.headers)
        }

        # Try to parse JSON if possible
        try:
            response_details['json'] = response.json()
        except ValueError:
            response_details['json'] = None

        return response_details

    except requests.RequestException as e:
        # Handle network-related errors
        raise requests.RequestException(f"Error sending POST request: {str(e)}")