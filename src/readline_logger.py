import readline
import logging
from typing import Optional, Callable

def log_interactive_prompt(prompt: str, 
                            log_level: int = logging.INFO, 
                            logger: Optional[logging.Logger] = None, 
                            validator: Optional[Callable[[str], bool]] = None) -> str:
    """
    Log an interactive prompt with optional validation and custom logging.
    
    Args:
        prompt (str): The prompt text to display and log
        log_level (int): Logging level (default: logging.INFO)
        logger (Optional[logging.Logger]): Custom logger to use. If None, creates a default logger
        validator (Optional[Callable[[str], bool]]): Optional function to validate input
    
    Returns:
        str: The user's input after successful validation
    
    Raises:
        ValueError: If input fails validation
    """
    # Create a default logger if not provided
    if logger is None:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        
        # Add console handler if no handlers exist
        if not logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
    
    # Log the prompt
    logger.log(log_level, f"Prompt: {prompt}")
    
    while True:
        try:
            # Use readline for interactive input
            user_input = input(prompt)
            
            # Validate input if validator is provided
            if validator is not None:
                if not validator(user_input):
                    logger.warning(f"Input validation failed: {user_input}")
                    continue
            
            # Log the input
            logger.log(log_level, f"User input received: {user_input}")
            return user_input
        
        except (KeyboardInterrupt, EOFError):
            logger.warning("Input interrupted")
            raise