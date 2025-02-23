import time
import requests
import logging

def log_network_request_response_time(url, method='GET', **kwargs):
    """
    Log the response time of a network request.
    
    Args:
        url (str): The URL to send the request to
        method (str, optional): HTTP method to use. Defaults to 'GET'
        **kwargs: Additional arguments to pass to requests.request()
    
    Returns:
        requests.Response: The response from the network request
    
    Raises:
        ValueError: If an invalid HTTP method is provided
        requests.RequestException: For network-related errors
    """
    # Configure logging
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    # Validate method
    valid_methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'PATCH', 'OPTIONS']
    if method.upper() not in valid_methods:
        raise ValueError(f"Invalid HTTP method. Must be one of {valid_methods}")
    
    # Start timing the request
    start_time = time.time()
    
    try:
        # Send the request
        response = requests.request(method, url, **kwargs)
        
        # Calculate response time
        response_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        
        # Log the response time and status
        logger.info(f"Request to {url} using {method} method completed in {response_time:.2f} ms "
                    f"(Status Code: {response.status_code})")
        
        return response
    
    except requests.RequestException as e:
        # Log any network-related errors
        logger.error(f"Network request to {url} failed: {str(e)}")
        raise