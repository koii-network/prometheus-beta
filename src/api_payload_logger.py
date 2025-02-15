import logging
import sys
from typing import Any, Dict, Optional

def log_api_response_payload_size(response: Any, logger: Optional[logging.Logger] = None) -> int:
    """
    Log the size of an API response payload.

    Args:
        response: The API response object to measure payload size
        logger: Optional custom logger. If not provided, uses default logging to stdout

    Returns:
        int: The size of the payload in bytes

    Raises:
        TypeError: If the response is None or cannot be processed
    """
    if response is None:
        raise TypeError("Response cannot be None")

    try:
        # Try to get payload size based on different response types
        if hasattr(response, 'content'):
            payload_size = len(response.content)
        elif hasattr(response, 'text'):
            payload_size = len(response.text.encode('utf-8'))
        elif isinstance(response, (str, bytes)):
            payload_size = len(response) if isinstance(response, bytes) else len(response.encode('utf-8'))
        elif hasattr(response, 'json'):
            try:
                payload_size = len(str(response.json()).encode('utf-8'))
            except Exception:
                payload_size = 0
        else:
            payload_size = sys.getsizeof(response)

        # Use provided logger or create a default one
        if logger is None:
            logger = logging.getLogger(__name__)
            logger.setLevel(logging.INFO)
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        # Log the payload size
        logger.info(f"API Response Payload Size: {payload_size} bytes")

        return payload_size

    except Exception as e:
        if logger is not None:
            logger.error(f"Error calculating payload size: {e}")
        raise TypeError(f"Unable to process response payload: {e}")