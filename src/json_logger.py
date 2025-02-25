import json
import logging

def log_json(logger, log_level, json_data, message=None):
    """
    Log a JSON object with proper formatting and optional message.
    
    :param logger: Logging object to use for logging
    :param log_level: Logging level (e.g., logging.INFO, logging.DEBUG)
    :param json_data: Dictionary or JSON-serializable object to log
    :param message: Optional additional context message
    :return: Formatted JSON string
    """
    try:
        # Validate input is JSON-serializable
        json_str = json.dumps(json_data, indent=2)
        
        # Construct log message with optional prefix
        log_message = f"{message + ': ' if message else ''}\n{json_str}"
        
        # Log based on specified log level
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
            raise ValueError(f"Unsupported log level: {log_level}")
        
        return json_str
    except (TypeError, ValueError) as e:
        # Handle JSON serialization or invalid input errors
        logger.error(f"JSON logging error: {str(e)}")
        raise