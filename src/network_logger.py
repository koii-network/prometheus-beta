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
    
    try:
        # Start timing
        start_time = time.time()
        
        # Send the request
        response = requests.request(method, url, timeout=timeout)
        
        # Calculate response time
        response_time = time.time() - start_time
        
        # Log the details
        log_entry = {
            'url': url,
            'method': method,
            'status_code': response.status_code,
            'response_time_ms': round(response_time * 1000, 2)
        }
        
        logger.info(f"Network Request: {log_entry}")
        
        return log_entry
    
    except requests.RequestException as e:
        logger.error(f"Network request error: {e}")
        raise