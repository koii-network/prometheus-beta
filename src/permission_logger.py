import logging
import sys
from enum import Enum, auto
from typing import Optional, Any

class UserPermissionLevel(Enum):
    """Enum representing different user permission levels."""
    GUEST = 0
    USER = 1
    ADMIN = 2

class PermissionLogger:
    """
    A logging utility that logs messages based on user permission levels.
    
    This class provides a flexible logging mechanism where messages are 
    logged only if the user's permission level meets or exceeds the 
    required permission level.
    """
    
    def __init__(self, log_file: Optional[str] = None):
        """
        Initialize the PermissionLogger.
        
        Args:
            log_file (Optional[str]): Path to the log file. If None, logs to console.
        """
        # Configure logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        # Console handler (using sys.stdout)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # File handler (if log_file is provided)
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
    
    def log(self, 
            message: str, 
            level: str = 'info', 
            min_permission: UserPermissionLevel = UserPermissionLevel.USER,
            user_permission: UserPermissionLevel = UserPermissionLevel.USER
    ) -> bool:
        """
        Log a message based on user permissions.
        
        Args:
            message (str): The message to log
            level (str): Logging level (debug, info, warning, error, critical)
            min_permission (UserPermissionLevel): Minimum permission required to log
            user_permission (UserPermissionLevel): Current user's permission level
        
        Returns:
            bool: True if message was logged, False otherwise
        
        Raises:
            ValueError: If an invalid logging level is provided
        """
        # Validate logging level
        level = level.lower()
        log_methods = {
            'debug': self.logger.debug,
            'info': self.logger.info,
            'warning': self.logger.warning,
            'error': self.logger.error,
            'critical': self.logger.critical
        }
        
        if level not in log_methods:
            raise ValueError(f"Invalid logging level: {level}")
        
        # Check if user has sufficient permissions
        if user_permission.value >= min_permission.value:
            # Log the message using the appropriate method
            log_method = log_methods[level]
            log_method(message)
            return True
        
        return False