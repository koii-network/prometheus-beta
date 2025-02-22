import logging
import sys

def log_api_response_payload_size(response, logger=None):
    """
    Log the size of an API response payload.
    
    Args:
        response: The API response object (assumed to have a .content or .text attribute)
        logger: Optional custom logger. If not provided, uses root logger.
    
    Returns:
        int: Size of the payload in bytes
    
    Raises:
        ValueError: If response is None or lacks content/text attribute
    """
    # Validate input
    if response is None:
        raise ValueError("Response cannot be None")
    
    # Determine payload size
    try:
        # Try to get payload size from .content first (preferred for binary responses)
        if hasattr(response, 'content'):
            payload_size = len(response.content)
        elif hasattr(response, 'text'):
            payload_size = len(response.text.encode('utf-8'))
        else:
            raise ValueError("Response object lacks content or text attribute")
    except Exception as e:
        raise ValueError(f"Could not determine payload size: {str(e)}")
    
    # Use provided logger or root logger
    log = logger or logging.getLogger()
    
    # Log the payload size
    log.info(f"API Response Payload Size: {payload_size} bytes")
    
    return payload_size