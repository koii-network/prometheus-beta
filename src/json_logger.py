import json
import logging

def log_json(logger, log_level, message, json_obj, indent=2):
    """
    Log a JSON object with proper formatting and spacing.
    
    Args:
        logger (logging.Logger): The logger to use for logging
        log_level (int): Logging level (e.g., logging.INFO, logging.DEBUG)
        message (str): A descriptive message to accompany the JSON
        json_obj (dict): The JSON object to log
        indent (int, optional): Number of spaces for JSON indentation. Defaults to 2.
    
    Raises:
        TypeError: If json_obj is not a dictionary
        ValueError: If indent is less than 0
    """
    # Validate inputs
    if not isinstance(json_obj, dict):
        raise TypeError("json_obj must be a dictionary")
    
    if indent < 0:
        raise ValueError("indent must be a non-negative integer")
    
    # Convert JSON to a formatted string
    formatted_json = json.dumps(json_obj, indent=indent)
    
    # Log the message with the formatted JSON
    logger.log(log_level, f"{message}\n{formatted_json}")