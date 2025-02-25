import time
import requests
import logging
from typing import Dict, Any, Optional

def log_network_request_response_time(
    url: str, 
    method: str = 'GET', 
    headers: Optional[Dict[str, str]] = None, 
    params: Optional[Dict[str, Any]] = None,
    timeout: float = 10.0
) -> Dict[str, Any]:
    """
    Send a network request and log its response time.

    Args:
        url (str): The URL to send the request to
        method (str, optional): HTTP method. Defaults to 'GET'
        headers (dict, optional): Request headers. Defaults to None
        params (dict, optional): Request parameters. Defaults to None
        timeout (float, optional): Request timeout in seconds. Defaults to 10.0

    Returns:
        Dict[str, Any]: A dictionary containing request details and response time

    Raises:
        ValueError: If URL is empty
        requests.RequestException: For network-related errors
    """
    # Validate input
    if not url:
        raise ValueError("URL cannot be empty")

    # Setup logging
    logger = logging.getLogger(__name__)
    
    # Prepare request parameters
    request_params = {
        'url': url,
        'method': method,
        'timeout': timeout
    }
    if headers:
        request_params['headers'] = headers
    if params:
        request_params['params'] = params

    try:
        # Start timing
        start_time = time.time()

        # Send request
        response = requests.request(**request_params)

        # Calculate response time
        response_time = time.time() - start_time

        # Log the response time
        logger.info(f"Network Request to {url}: Response Time = {response_time:.4f} seconds")

        # Return detailed information
        return {
            'url': url,
            'method': method,
            'status_code': response.status_code,
            'response_time': response_time,
            'response_length': len(response.content)
        }

    except requests.RequestException as e:
        # Log and re-raise network-related exceptions
        logger.error(f"Network Request Error: {e}")
        raise