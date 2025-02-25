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
    # Configure logging
    logging.basicConfig(
        filename=log_file, 
        level=log_level, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Prompt and capture user input
    try:
        user_input = input("Enter your input: ").strip()
        
        # Validate input
        if not user_input:
            raise ValueError("Input cannot be empty.")
        
        # Log the input
        logging.info(f"User input: {user_input}")
        
        return user_input
    
    except (KeyboardInterrupt, EOFError):
        logging.warning("Input was interrupted.")
        raise