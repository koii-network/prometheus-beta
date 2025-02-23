import time
import requests
import logging
from typing import Dict, Any, Optional

class NetworkResponseLogger:
    """
    A utility class for logging network request response times.
    
    This class provides methods to measure and log the response times 
    of network requests with optional custom logging configuration.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize the NetworkResponseLogger.
        
        Args:
            logger (Optional[logging.Logger]): A custom logger. 
                If not provided, a default logger will be used.
        """
        self.logger = logger or logging.getLogger(__name__)
    
    def log_request_time(self, url: str, method: str = 'GET', 
                         headers: Optional[Dict[str, str]] = None, 
                         timeout: float = 10.0) -> Dict[str, Any]:
        """
        Send a network request and log its response time.
        
        Args:
            url (str): The URL to send the request to
            method (str, optional): HTTP method. Defaults to 'GET'
            headers (Optional[Dict[str, str]], optional): Request headers
            timeout (float, optional): Request timeout in seconds. Defaults to 10.0
        
        Returns:
            Dict[str, Any]: A dictionary containing request details and performance metrics
        
        Raises:
            requests.RequestException: For network-related errors
            ValueError: For invalid input
        """
        # Validate inputs
        if not url:
            raise ValueError("URL cannot be empty")
        
        # Prepare headers (use empty dict if None)
        headers = headers or {}
        
        try:
            # Start timing
            start_time = time.time()
            
            # Perform the request
            response = requests.request(
                method=method.upper(), 
                url=url, 
                headers=headers, 
                timeout=timeout
            )
            
            # Calculate total time
            total_time = time.time() - start_time
            
            # Log the details
            log_msg = (f"Request to {url} completed. "
                       f"Method: {method.upper()}, "
                       f"Status: {response.status_code}, "
                       f"Response Time: {total_time:.4f} seconds")
            self.logger.info(log_msg)
            
            # Return comprehensive details
            return {
                'url': url,
                'method': method.upper(),
                'status_code': response.status_code,
                'response_time': total_time,
                'headers': response.headers
            }
        
        except requests.RequestException as e:
            # Log and re-raise network-related exceptions
            error_msg = f"Network request failed: {str(e)}"
            self.logger.error(error_msg)
            raise