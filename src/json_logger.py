"""
Module for logging JSON objects with proper formatting.

This module provides a utility function to log JSON objects with 
configurable indentation and spacing.
"""

import json
import logging


def log_json(data, log_level=logging.INFO, indent=2, logger=None):
    """
    Log a JSON object with proper formatting.

    Args:
        data (dict): The JSON-serializable object to log
        log_level (int, optional): Logging level. Defaults to logging.INFO
        indent (int, optional): Number of spaces for indentation. Defaults to 2
        logger (logging.Logger, optional): Custom logger. Defaults to root logger

    Returns:
        str: Formatted JSON string that was logged

    Raises:
        TypeError: If data is not JSON serializable
        ValueError: If indent is negative
    """
    # Validate inputs
    if indent < 0:
        raise ValueError("Indent must be a non-negative integer")

    # Use root logger if no logger provided
    if logger is None:
        logger = logging.getLogger()

    try:
        # Serialize JSON with specified indentation
        formatted_json = json.dumps(data, indent=indent)
        
        # Log the formatted JSON
        logger.log(log_level, formatted_json)
        
        return formatted_json
    except TypeError as e:
        # Handle non-JSON serializable objects
        logger.error(f"Unable to serialize JSON: {e}")
        raise