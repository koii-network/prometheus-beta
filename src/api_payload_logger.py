import logging
import sys
from typing import Any, Optional

def log_api_response_payload_size(response: Any, logger: Optional[logging.Logger] = None) -> int:
    """
    Log the size of an API response payload.

    Args:
        response (Any): The API response object to measure.
        logger (Optional[logging.Logger]): Custom logger. If None, uses root logger.

    Returns:
        int: The size of the payload in bytes.

    Raises:
        TypeError: If the response cannot be measured.
    """
    # Use root logger if no logger is provided
    if logger is None:
        logger = logging.getLogger()

    # Determine payload size based on different response types
    try:
        # For responses with .text or .content attributes (like requests library)
        if hasattr(response, 'text'):
            payload_size = len(response.text.encode('utf-8'))
        elif hasattr(response, 'content'):
            payload_size = len(response.content)
        # For dictionary-like responses
        elif isinstance(response, dict):
            payload_size = len(str(response).encode('utf-8'))
        # For string responses
        elif isinstance(response, str):
            payload_size = len(response.encode('utf-8'))
        # For bytes responses
        elif isinstance(response, bytes):
            payload_size = len(response)
        else:
            raise TypeError(f"Cannot determine payload size for type {type(response)}")

        # Log the payload size
        logger.info(f"API Response Payload Size: {payload_size} bytes")
        
        return payload_size

    except Exception as e:
        logger.error(f"Error measuring payload size: {str(e)}")
        raise