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
    
    Returns:
        bool: Whether the message was logged
    
    Raises:
        ValueError: If an invalid log level is provided
        TypeError: If message or user_permission is of incorrect type
    """
    # Validate inputs
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if not isinstance(user_permission, UserPermissionLevel):
        raise TypeError("User permission must be a UserPermissionLevel")
    
    # Configure logging
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    # Validate log level
    log_level = log_level.lower()
    log_methods = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }
    
    if log_level not in log_methods:
        raise ValueError(f"Invalid log level: {log_level}")
    
    # Log based on permission levels
    if user_permission == UserPermissionLevel.ADMIN:
        # Admins can log all levels
        log_methods[log_level](f"[ADMIN] {message}")
        return True
    elif user_permission == UserPermissionLevel.USER:
        # Regular users can log info and warning levels
        if log_level in ['info', 'warning']:
            log_methods[log_level](f"[USER] {message}")
            return True
    elif user_permission == UserPermissionLevel.GUEST:
        # Guests can only log info level
        if log_level == 'info':
            log_methods[log_level](f"[GUEST] {message}")
            return True
    
    return False