import readline
import logging
from typing import Optional, Callable

def log_interactive_prompt(
    prompt: str, 
    logger: Optional[logging.Logger] = None, 
    log_level: int = logging.INFO,
    validator: Optional[Callable[[str], bool]] = None
) -> str:
    """
    Log and handle interactive prompts using readline with optional validation.
    
    Args:
        prompt (str): The prompt message to display to the user
        logger (Optional[logging.Logger]): Logger to use for recording prompts and inputs. 
                                           If None, no logging will occur.
        log_level (int): Logging level to use (default: logging.INFO)
        validator (Optional[Callable[[str], bool]]): Optional function to validate input
    
    Returns:
        str: The user's input after optional validation
    
    Raises:
        ValueError: If input fails validation
    """
    # Log the prompt if logger is provided
    if logger:
        logger.log(log_level, f"Prompt: {prompt}")
    
    # Use readline for interactive input with history support
    try:
        user_input = input(prompt)
        
        # Validate input if validator is provided
        if validator:
            if not validator(user_input):
                raise ValueError("Input failed validation")
        
        # Log the input if logger is provided
        if logger:
            logger.log(log_level, f"User input: {user_input}")
        
        return user_input
    
    except Exception as e:
        # Log any exceptions
        if logger:
            logger.error(f"Error during input: {str(e)}")
        raise