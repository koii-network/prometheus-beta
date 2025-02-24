import pprint
import logging
import json

def log_object(obj, log_level=logging.INFO, logger=None):
    """
    Log an object in a readable, formatted manner.

    Args:
        obj: The object to be logged (can be any JSON-serializable object)
        log_level (int, optional): Logging level. Defaults to logging.INFO.
        logger (logging.Logger, optional): Custom logger. Defaults to None.

    Returns:
        str: A formatted string representation of the object

    Raises:
        TypeError: If the object cannot be serialized or logged
    """
    # If no logger is provided, use the root logger
    if logger is None:
        logger = logging.getLogger()

    try:
        # Use pprint with custom formatting to handle recursive objects
        formatted_obj = pprint.pformat(
            obj, 
            indent=2, 
            width=100, 
            compact=False, 
            depth=10,  # Limit recursion depth
            sort_dicts=True  # Sort dictionary keys for consistent output
        )
        
        # Log the object
        logger.log(log_level, formatted_obj)
        
        return formatted_obj
    except Exception as e:
        # Handle serialization or formatting errors
        try:
            # Fallback to string representation if pprint fails
            str_repr = str(obj)
            logger.log(log_level, str_repr)
            return str_repr
        except Exception as fallback_error:
            # Final error handling
            error_msg = f"Error logging object: {str(fallback_error)}"
            logger.error(error_msg)
            raise TypeError(error_msg) from fallback_error