import json
import logging

def log_json(logger, level, json_obj, message=None):
    """
    Log a JSON object with proper formatting and optional additional message.
    
    :param logger: The logging object to use
    :param level: Logging level (e.g., logging.INFO, logging.DEBUG)
    :param json_obj: The JSON object to log
    :param message: Optional additional message to prepend to the JSON log
    """
    # Validate inputs
    if not hasattr(logger, 'log'):
        raise TypeError("Invalid logger object")
    
    if not isinstance(json_obj, (dict, list)):
        raise TypeError("json_obj must be a dictionary or list")
    
    # Prepare the log message
    try:
        # Use indent=2 for nice, readable JSON formatting
        formatted_json = json.dumps(json_obj, indent=2)
        
        # Combine message with JSON if message is provided
        log_message = f"{message + '\n' if message else ''}{formatted_json}"
        
        # Log the message at the specified level
        logger.log(level, log_message)
    except TypeError as e:
        raise TypeError(f"Unable to serialize JSON: {e}")