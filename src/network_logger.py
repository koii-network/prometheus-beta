import time
import requests
import logging

def log_network_request_time(url, method='GET', timeout=10):
    """
    Log the response time of a network request.
    
    Args:
        url (str): The URL to send the request to
        method (str, optional): HTTP method. Defaults to 'GET'
        timeout (int, optional): Request timeout in seconds. Defaults to 10
    
    Returns:
        dict: A dictionary containing request details and response time
    """
    # Configure logging
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    # Record start time
    start_time = time.time()
    
    try:
        # Perform the network request based on the specified method
        if method.upper() == 'GET':
            response = requests.get(url, timeout=timeout)
        elif method.upper() == 'POST':
            response = requests.post(url, timeout=timeout)
        elif method.upper() == 'PUT':
            response = requests.put(url, timeout=timeout)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, timeout=timeout)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        
        # Calculate response time
        response_time = time.time() - start_time
        
        # Log the request details
        log_message = (f"URL: {url}, Method: {method}, "
                       f"Status Code: {response.status_code}, "
                       f"Response Time: {response_time:.4f} seconds")
        logger.info(log_message)
        
        # Return detailed information
        return {
            'url': url,
            'method': method,
            'status_code': response.status_code,
            'response_time': response_time,
            'success': response.ok
        }
    
    except requests.RequestException as e:
        # Log any request-related exceptions
        response_time = time.time() - start_time
        logger.error(f"Request to {url} failed: {str(e)}")
        
        return {
            'url': url,
            'method': method,
            'error': str(e),
            'response_time': response_time,
            'success': False
        }