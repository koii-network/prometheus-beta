import requests

def send_get_request(url, headers=None, params=None, timeout=10):
    """
    Send an HTTP GET request to the specified URL.

    Args:
        url (str): The URL to send the GET request to.
        headers (dict, optional): Optional headers to include in the request. Defaults to None.
        params (dict, optional): Optional query parameters to include in the request. Defaults to None.
        timeout (int, optional): Timeout for the request in seconds. Defaults to 10.

    Returns:
        dict: A dictionary containing the response details:
            - 'status_code': HTTP status code of the response
            - 'content': Response content as text
            - 'headers': Response headers
            - 'json': JSON response (if applicable)

    Raises:
        requests.RequestException: For network-related errors
        ValueError: If the URL is empty or invalid
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string")

    try:
        # Send GET request
        response = requests.get(
            url, 
            headers=headers, 
            params=params, 
            timeout=timeout
        )
        
        # Raise an exception for bad HTTP responses
        response.raise_for_status()

        # Prepare response dictionary
        response_data = {
            'status_code': response.status_code,
            'content': response.text,
            'headers': dict(response.headers),
        }

        # Try to parse JSON if possible
        try:
            response_data['json'] = response.json()
        except ValueError:
            response_data['json'] = None

        return response_data

    except requests.RequestException as e:
        # Handle network-related errors
        raise requests.RequestException(f"Error sending GET request: {str(e)}")