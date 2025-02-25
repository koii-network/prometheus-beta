import logging

def log_multiline(message, logger=None, level=logging.INFO, separator='=', separator_length=40):
    """
    Log a multi-line message with optional separation lines.

    Args:
        message (str): The message to log
        logger (logging.Logger, optional): Custom logger. If None, uses root logger.
        level (int, optional): Logging level. Defaults to logging.INFO.
        separator (str, optional): Character used for separation lines. Defaults to '='.
        separator_length (int, optional): Length of separation lines. Defaults to 40.

    Returns:
        None
    """
    # Use root logger if no logger is provided
    if logger is None:
        logger = logging.getLogger()

    # Create separation line
    sep_line = separator * separator_length

    # Log with separation lines
    logger.log(level, sep_line)
    logger.log(level, message)
    logger.log(level, sep_line)