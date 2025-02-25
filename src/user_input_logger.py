import sys
import logging
from typing import Optional

def log_user_input(log_file: Optional[str] = None, log_level: int = logging.INFO) -> str:
    """
    Capture and log user input from the command line.

    Args:
        log_file (Optional[str], optional): Path to the log file. 
            If None, logs to console. Defaults to None.
        log_level (int, optional): Logging level. Defaults to logging.INFO.

    Returns:
        str: The user input that was logged.

    Raises:
        ValueError: If input is empty or contains only whitespace.
    """
    # Create a logger
    logger = logging.getLogger('user_input_logger')
    logger.setLevel(log_level)

    # Clear any existing handlers to prevent duplicate logs
    logger.handlers.clear()

    # Create handlers
    if log_file:
        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(file_handler)
    else:
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)
        console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(console_handler)

    # Prompt and capture user input
    try:
        user_input = input("Enter your input: ").strip()
        
        # Validate input
        if not user_input:
            raise ValueError("Input cannot be empty.")
        
        # Log the input
        logger.info(f"User input: {user_input}")
        
        return user_input
    
    except (KeyboardInterrupt, EOFError):
        logger.warning("Input was interrupted.")
        raise