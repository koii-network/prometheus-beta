import json
import logging

def log_json(logger, level, json_obj, message=None):
    """
    Log a JSON object with proper formatting and optional additional message.
    
    :param logger: Logging object to use for logging
    :param level: Logging level (e.g., logging.INFO, logging.DEBUG)
    :param json_obj: Dictionary or JSON-serializable object to log
    :param message: Optional additional message to prepend to the JSON log
    """
    try:
        # Validate input is JSON-serializable
        json.dumps(json_obj)
        
        # Format JSON with indentation for readability
        formatted_json = json.dumps(json_obj, indent=2)
        
        # Prepare log message
        log_message = formatted_json if message is None else f"{message}\n{formatted_json}"
        
        # Log the message at the specified level
        logger.log(level, log_message)
    
    except (TypeError, ValueError) as e:
        # Handle non-JSON-serializable objects
        logger.error(f"Unable to log JSON: {str(e)}")
        raise