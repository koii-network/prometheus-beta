import logging
import sys

def log_api_response_payload_size(response, logger=None):
    """
    Log the size of an API response payload.
    
    Args:
        response: An object with a response body/content that supports size measurement
        logger: Optional custom logger. If not provided, uses the root logger.
    
    Returns:
        int: Size of the payload in bytes
    
    Raises:
        TypeError: If response is None or does not have a way to measure size
        ValueError: If payload size cannot be determined
    """
    # Validate input
    if response is None:
        raise TypeError("Response cannot be None")
    
    # Use provided logger or default to root logger
    log = logger or logging.getLogger()
    
    try:
        # Try different methods to get payload size
        if hasattr(response, 'content'):
            payload_size = len(response.content)
        elif hasattr(response, 'text'):
            payload_size = len(response.text.encode('utf-8'))
        elif hasattr(response, 'read'):
            payload_size = len(response.read())
        else:
            raise ValueError("Cannot determine payload size")
        
        # Log the payload size
        log.info(f"API Response Payload Size: {payload_size} bytes")
        
        return payload_size
    
    except Exception as e:
        log.error(f"Error measuring payload size: {e}")
        raise ValueError(f"Could not measure payload size: {e}")