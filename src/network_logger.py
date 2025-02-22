import time
import requests
import logging

def log_network_request_time(url, method='GET', headers=None, timeout=10):
    """
    Log the response time of a network request.
    
    Args:
        url (str): The URL to send the request to
        method (str, optional): HTTP method. Defaults to 'GET'
        headers (dict, optional): HTTP headers. Defaults to None
        timeout (int, optional): Request timeout in seconds. Defaults to 10
    
    Returns:
        dict: A dictionary containing request details and response time
    """
    # Configure logging
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    # Prepare request details
    request_details = {
        'url': url,
        'method': method,
        'headers': headers or {},
        'timeout': timeout
    }
    
    try:
        # Start timing
        start_time = time.time()
        
        # Send the request
        response = requests.request(
            method=method, 
            url=url, 
            headers=headers, 
            timeout=timeout
        )
        
        # Calculate response time
        response_time = time.time() - start_time
        
        # Log the request details and response time
        logger.info(f"Network Request Details: {request_details}")
        logger.info(f"Response Time: {response_time:.4f} seconds")
        logger.info(f"Response Status Code: {response.status_code}")
        
        # Return detailed information
        return {
            'request_details': request_details,
            'response_time': response_time,
            'status_code': response.status_code
        }
    
    except requests.RequestException as e:
        # Log any request-related errors
        logger.error(f"Network Request Error: {e}")
        raise