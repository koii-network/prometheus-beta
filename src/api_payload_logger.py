import logging
import json

def log_api_response_payload_size(response, logger=None):
    """
    Log the size of an API response payload.
    
    Args:
        response: The API response object
        logger: Optional custom logger. If not provided, uses the root logger.
    
    Returns:
        int: Size of the response payload in bytes
    """
    # If no logger is provided, use the root logger
    if logger is None:
        logger = logging.getLogger()
    
    # Try to get the response content/payload
    try:
        # If response is a string or bytes, get its size directly
        if isinstance(response, (str, bytes)):
            payload = response
        # If response has a text or content attribute, use that
        elif hasattr(response, 'text'):
            payload = response.text
        elif hasattr(response, 'content'):
            payload = response.content
        # If response is a dict/list, convert to JSON string
        elif isinstance(response, (dict, list)):
            payload = json.dumps(response)
        else:
            logger.warning(f"Unable to determine payload type: {type(response)}")
            return 0
        
        # Convert payload to bytes if it's not already
        if not isinstance(payload, bytes):
            payload = payload.encode('utf-8')
        
        # Get payload size
        payload_size = len(payload)
        
        # Log the payload size
        logger.info(f"API Response Payload Size: {payload_size} bytes")
        
        return payload_size
    
    except Exception as e:
        logger.error(f"Error logging payload size: {str(e)}")
        return 0