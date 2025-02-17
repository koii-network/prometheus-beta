import requests

def send_http_post_request(url, data=None, headers=None, timeout=10):
    """
    Send an HTTP POST request to the specified URL.

    Args:
        url (str): The target URL to send the POST request to.
        data (dict, optional): The payload to send in the request body. Defaults to None.
        headers (dict, optional): Custom headers to include in the request. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        dict: A dictionary containing the response status code and response JSON (if applicable).

    Raises:
        requests.RequestException: For network-related errors.
        ValueError: If the URL is invalid or empty.
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL. URL must be a non-empty string.")

    # Prepare headers (use empty dict if None)
    request_headers = headers or {}

    try:
        # Send POST request
        response = requests.post(
            url, 
            json=data, 
            headers=request_headers, 
            timeout=timeout
        )

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Try to parse JSON response, return empty dict if parsing fails
        try:
            response_json = response.json()
        except ValueError:
            response_json = {}

        return {
            'status_code': response.status_code,
            'json': response_json
        }

    except requests.RequestException as e:
        # Handle network-related errors
        raise requests.RequestException(f"Error sending POST request: {str(e)}")