import logging
import json

def log_api_response_payload_size(response, logger=None):
    """
    Log the size of an API response payload.

    Args:
        response: API response object with a .text or .content attribute
        logger: Optional custom logger. If not provided, uses default logging.

    Returns:
        int: Size of the payload in bytes

    Raises:
        ValueError: If response is None or invalid
        TypeError: If response doesn't have a text/content attribute
    """
    # Use default logger if not provided
    if logger is None:
        logger = logging.getLogger(__name__)

    # Validate response
    if response is None:
        raise ValueError("Response cannot be None")

    # Try to get payload, prioritizing .text over .content
    try:
        if hasattr(response, 'text'):
            payload = response.text
        elif hasattr(response, 'content'):
            payload = response.content
        else:
            raise TypeError("Response must have 'text' or 'content' attribute")

        # Calculate payload size
        payload_size = len(payload)

        # Log the payload size
        logger.info(f"API Response Payload Size: {payload_size} bytes")

        return payload_size

    except Exception as e:
        logger.error(f"Error logging payload size: {str(e)}")
        raise