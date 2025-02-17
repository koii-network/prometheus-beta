import logging
from enum import Enum, auto

class UserPermissionLevel(Enum):
    GUEST = auto()
    USER = auto()
    ADMIN = auto()

def log_message(message, user_permission, log_level='info'):
    """
    Log console messages based on user permissions.
    
    Args:
        message (str): The message to log
        user_permission (UserPermissionLevel): User's permission level
        log_level (str, optional): Logging level. Defaults to 'info'.
    
    Raises:
        ValueError: If an invalid log level is provided
        TypeError: If message is not a string or permission is invalid
    """
    # Validate inputs
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if not isinstance(user_permission, UserPermissionLevel):
        raise TypeError("Invalid user permission level")
    
    # Configure logging
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Normalize log level
    log_level = log_level.lower()
    
    # Map log levels to logging methods
    log_methods = {
        'debug': logging.debug,
        'info': logging.info,
        'warning': logging.warning,
        'error': logging.error,
        'critical': logging.critical
    }
    
    # Validate log level
    if log_level not in log_methods:
        raise ValueError(f"Invalid log level: {log_level}")
    
    # Permission-based logging
    if user_permission == UserPermissionLevel.GUEST:
        # Guests can only log info and warning messages
        if log_level in ['debug', 'error', 'critical']:
            return False
    
    if user_permission == UserPermissionLevel.USER:
        # Users cannot log debug messages
        if log_level == 'debug':
            return False
    
    # Log the message using the appropriate method
    log_methods[log_level](f"[{user_permission.name}] {message}")
    return True