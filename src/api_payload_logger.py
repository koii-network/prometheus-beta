import logging
import json

def log_api_response_payload_size(response, logger=None):
    """
    Log the payload size of an API response.
    
    Args:
        response: The API response object (e.g., from requests library)
        logger: Optional custom logger. If not provided, uses root logger.
    
    Returns:
        int: Size of the response payload in bytes
    
    Raises:
        ValueError: If response is None or invalid
    """
    # Validate input
    if response is None:
        raise ValueError("Response cannot be None")
    
    # Determine logger
    log = logger or logging.getLogger()
    
    # Get payload size
    try:
        # Try to get content length from headers
        if hasattr(response, 'headers'):
            content_length = response.headers.get('Content-Length')
            if content_length:
                payload_size = int(content_length)
                log.info(f"API Response Payload Size: {payload_size} bytes (from headers)")
                return payload_size
        
        # If no headers, try to get payload size from text/content
        if hasattr(response, 'text'):
            payload_size = len(response.text.encode('utf-8'))
        elif hasattr(response, 'content'):
            payload_size = len(response.content)
        else:
            payload_size = 0
        
        log.info(f"API Response Payload Size: {payload_size} bytes")
        return payload_size
    
    except Exception as e:
        log.error(f"Error logging API response payload size: {str(e)}")
        raise