import json
import logging

def log_json_object(logger, log_level, json_object, message=None):
    """
    Log a JSON object with proper formatting and optional message.
    
    Args:
        logger (logging.Logger): The logger to use for logging
        log_level (int): Logging level (e.g., logging.INFO, logging.DEBUG)
        json_object (dict): The JSON object to log
        message (str, optional): Optional additional message to prepend to the log
    
    Returns:
        str: The formatted JSON string that was logged
    """
    try:
        # Validate input is a dictionary
        if not isinstance(json_object, dict):
            raise ValueError("Input must be a dictionary")
        
        # Format JSON with indentation
        formatted_json = json.dumps(json_object, indent=2)
        
        # Prepare log message
        log_message = formatted_json if message is None else f"{message}\n{formatted_json}"
        
        # Log the message at the specified level
        if log_level == logging.DEBUG:
            logger.debug(log_message)
        elif log_level == logging.INFO:
            logger.info(log_message)
        elif log_level == logging.WARNING:
            logger.warning(log_message)
        elif log_level == logging.ERROR:
            logger.error(log_message)
        elif log_level == logging.CRITICAL:
            logger.critical(log_message)
        else:
            raise ValueError("Invalid log level")
        
        return formatted_json
    except (TypeError, ValueError) as e:
        raise ValueError(f"Failed to log JSON object: {str(e)}")