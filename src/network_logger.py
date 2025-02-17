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
        Dict[str, Any]: A dictionary containing request details and performance metrics
    """
    # Configure logging
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    # Prepare default headers and params
    headers = headers or {}
    params = params or {}
    
    try:
        # Start timing the request
        start_time = time.time()
        
        # Send the request
        response = requests.request(
            method=method, 
            url=url, 
            headers=headers, 
            params=params,
            timeout=timeout
        )
        
        # Calculate response time
        response_time = time.time() - start_time
        
        # Log the request details
        logger.info(f"Network Request: {method} {url}")
        logger.info(f"Response Time: {response_time:.4f} seconds")
        logger.info(f"Status Code: {response.status_code}")
        
        # Return detailed request information
        return {
            'url': url,
            'method': method,
            'status_code': response.status_code,
            'response_time': response_time,
            'headers': dict(response.headers),
            'content': response.text
        }
    
    except requests.RequestException as e:
        logger.error(f"Network Request Error: {e}")
        raise