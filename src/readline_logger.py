import readline
import logging
from typing import Optional, Callable

class ReadlineLogger:
    """
    A utility class to log interactive prompts using readline module.
    
    This class provides methods to hook into readline's input mechanism 
    and log user interactions with interactive prompts.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize the ReadlineLogger.
        
        Args:
            logger (Optional[logging.Logger]): A logger instance. 
                If not provided, a default logger will be created.
        """
        self.logger = logger or logging.getLogger(__name__)
        self._original_hook: Optional[Callable] = None
    
    def start_logging(self) -> None:
        """
        Start logging readline inputs by hooking into the input mechanism.
        """
        # Store the original hook to restore later
        self._original_hook = readline.get_pre_input_hook()
        
        def log_input_hook() -> None:
            """
            Internal hook to log readline inputs.
            """
            self.logger.info("Interactive prompt initiated")
        
        # Set the new pre-input hook
        readline.set_pre_input_hook(log_input_hook)
    
    def stop_logging(self) -> None:
        """
        Stop logging and restore the original readline hook.
        """
        if self._original_hook is not None:
            readline.set_pre_input_hook(self._original_hook)
            self._original_hook = None
        else:
            self.logger.warning("No active logging hook to stop")
    
    def log_input(self, prompt: str, log_message: Optional[str] = None) -> str:
        """
        Log and capture user input for a given prompt.
        
        Args:
            prompt (str): The prompt to display to the user
            log_message (Optional[str]): Custom log message. If None, uses default.
        
        Returns:
            str: The user's input
        """
        if log_message is None:
            log_message = f"Prompted with: {prompt}"
        
        self.logger.info(log_message)
        return input(prompt)