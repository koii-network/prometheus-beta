import requests
from typing import Dict, Any, Optional

def send_http_post_request(url: str, 
                            data: Optional[Dict[str, Any]] = None, 
                            headers: Optional[Dict[str, str]] = None, 
                            timeout: int = 10) -> Dict[str, Any]:
    """
    Send an HTTP POST request to the specified URL.

    Args:
        url (str): The URL to send the POST request to.
        data (dict, optional): The payload to send with the request. Defaults to None.
        headers (dict, optional): Custom headers to send with the request. Defaults to None.
        timeout (int, optional): Request timeout in seconds. Defaults to 10.

    Returns:
        dict: A dictionary containing the response details.

    Raises:
        requests.RequestException: For any network-related errors.
        ValueError: If the URL is invalid or empty.
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    # Use empty dict if no data/headers provided
    data = data or {}
    headers = headers or {}

    try:
        # Send POST request
        response = requests.post(
            url, 
            json=data, 
            headers=headers, 
            timeout=timeout
        )

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Return response details
        return {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'body': response.json() if response.text else {}
        }

    except requests.RequestException as e:
        # Catch and re-raise any request-related exceptions
        raise requests.RequestException(f"HTTP POST request failed: {str(e)}") from e