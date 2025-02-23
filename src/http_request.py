import requests
from typing import Optional, Dict, Any

def send_http_get_request(url: str, 
                           headers: Optional[Dict[str, str]] = None, 
                           timeout: float = 10.0) -> Dict[str, Any]:
    """
    Send an HTTP GET request to the specified URL.

    Args:
        url (str): The URL to send the GET request to.
        headers (Optional[Dict[str, str]], optional): Optional headers to include. Defaults to None.
        timeout (float, optional): Request timeout in seconds. Defaults to 10.0.

    Returns:
        Dict[str, Any]: A dictionary containing response details.

    Raises:
        ValueError: If the URL is empty or None.
        requests.RequestException: For network-related errors.
    """
    # Validate URL
    if not url:
        raise ValueError("URL cannot be empty")

    try:
        # Send the GET request
        response = requests.get(
            url, 
            headers=headers, 
            timeout=timeout
        )

        # Raise an exception for bad HTTP responses
        response.raise_for_status()

        # Return a comprehensive response dictionary
        return {
            'status_code': response.status_code,
            'text': response.text,
            'json': response.json() if response.headers.get('content-type', '').startswith('application/json') else None,
            'headers': dict(response.headers)
        }

    except requests.RequestException as e:
        # Handle and re-raise request-related exceptions
        raise RuntimeError(f"HTTP GET request failed: {str(e)}") from e