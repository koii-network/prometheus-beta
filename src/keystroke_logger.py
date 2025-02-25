import os
import logging
from typing import Optional

class KeystrokeLogger:
    """
    A class to log keystrokes with configurable logging options.
    
    Provides methods to log keystrokes to a file or in-memory buffer,
    with support for different logging levels and log file management.
    """
    
    def __init__(self, log_file: Optional[str] = None, log_level: int = logging.INFO):
        """
        Initialize the KeystrokeLogger.
        
        Args:
            log_file (Optional[str]): Path to the log file. If None, logs to memory.
            log_level (int): Logging level (default: logging.INFO)
        """
        # Create logger
        self.logger = logging.getLogger('keystroke_logger')
        self.logger.setLevel(log_level)
        
        # In-memory buffer for keystrokes
        self._keystroke_buffer = []
        
        # File logging setup
        if log_file:
            # Ensure directory exists
            os.makedirs(os.path.dirname(log_file), exist_ok=True) if os.path.dirname(log_file) else None
            
            # Create file handler
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(log_level)
            
            # Create formatter
            formatter = logging.Formatter('%(asctime)s - %(message)s')
            file_handler.setFormatter(formatter)
            
            # Add file handler to logger
            self.logger.addHandler(file_handler)
    
    def log_keystroke(self, key: str) -> None:
        """
        Log a single keystroke.
        
        Args:
            key (str): The keystroke to log
        
        Raises:
            ValueError: If the input is not a single character
        """
        # Validate input
        if not isinstance(key, str) or len(key) != 1:
            raise ValueError("Keystroke must be a single character")
        
        # Log to file (if configured)
        self.logger.info(f"Keystroke: {key}")
        
        # Store in memory buffer
        self._keystroke_buffer.append(key)
    
    def get_keystroke_buffer(self) -> list:
        """
        Retrieve the in-memory keystroke buffer.
        
        Returns:
            list: List of logged keystrokes
        """
        return self._keystroke_buffer.copy()
    
    def clear_keystroke_buffer(self) -> None:
        """
        Clear the in-memory keystroke buffer.
        """
        self._keystroke_buffer.clear()