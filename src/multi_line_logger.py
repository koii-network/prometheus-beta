import logging

def log_multiline(message, level=logging.INFO, separator='=', separator_length=40):
    """
    Log a multi-line message with optional separation lines.
    
    Args:
        message (str): The message to log
        level (int, optional): Logging level. Defaults to logging.INFO.
        separator (str, optional): Character used for separation lines. Defaults to '='.
        separator_length (int, optional): Length of separation lines. Defaults to 40.
    """
    # Create logger if not already configured
    logger = logging.getLogger(__name__)
    
    # Create separation line
    sep_line = separator * separator_length
    
    # Prepare the log message with separation lines
    log_lines = [
        sep_line,
        message,
        sep_line
    ]
    
    # Join the lines and log based on the specified level
    full_log_message = '\n'.join(log_lines)
    
    if level == logging.DEBUG:
        logger.debug(full_log_message)
    elif level == logging.INFO:
        logger.info(full_log_message)
    elif level == logging.WARNING:
        logger.warning(full_log_message)
    elif level == logging.ERROR:
        logger.error(full_log_message)
    elif level == logging.CRITICAL:
        logger.critical(full_log_message)
    else:
        # Default to INFO if an invalid level is provided
        logger.info(full_log_message)