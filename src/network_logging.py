import time
import requests
import logging

def log_network_request_response_time(url, method='GET', **kwargs):
    """
    Log the response time of a network request.
    
    Args:
        url (str): The URL to send the request to
        method (str, optional): HTTP method. Defaults to 'GET'
        **kwargs: Additional arguments to pass to requests.request()
    
    Returns:
        requests.Response: The response from the network request
    
    Raises:
        ValueError: If an invalid HTTP method is provided
    """
    # Configure logging
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - Network Request Response Time - %(message)s')
    logger = logging.getLogger(__name__)
    
    # Validate method
    valid_methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS']
    if method.upper() not in valid_methods:
        raise ValueError(f"Invalid HTTP method. Must be one of {valid_methods}")
    
    # Start timing
    start_time = time.time()
    
    try:
        # Perform the request
        response = requests.request(method, url, **kwargs)
        
        # Calculate response time
        response_time = time.time() - start_time
        
        # Log the response time
        logger.info(f"URL: {url}, Method: {method}, Response Time: {response_time:.4f} seconds, Status Code: {response.status_code}")
        
        return response
    
    except requests.RequestException as e:
        # Log any request exceptions
        logger.error(f"Request to {url} failed: {str(e)}")
        raise