from enum import Enum, auto
from typing import Union, Optional

class UserPermissionLevel(Enum):
    """Enum representing user permission levels for logging."""
    GUEST = 0
    USER = 1
    ADMIN = 2

class ConsoleLogger:
    """
    A logger that controls message logging based on user permission levels.
    
    Provides methods to log messages with different severity and permission requirements.
    """
    def __init__(self, current_user_permission: UserPermissionLevel = UserPermissionLevel.GUEST):
        """
        Initialize the logger with a specific user permission level.
        
        :param current_user_permission: Permission level of the current user
        """
        self.current_user_permission = current_user_permission
    
    def log(self, message: str, required_permission: UserPermissionLevel = UserPermissionLevel.GUEST) -> Union[str, None]:
        """
        Log a message if the user has sufficient permissions.
        
        :param message: The message to log
        :param required_permission: Minimum permission level required to log the message
        :return: The logged message if permission is sufficient, None otherwise
        """
        if self.current_user_permission.value >= required_permission.value:
            print(message)
            return message
        return None
    
    def debug(self, message: str) -> Union[str, None]:
        """
        Log a debug message (requires USER or higher permissions).
        
        :param message: The debug message to log
        :return: The logged message if permission is sufficient, None otherwise
        """
        return self.log(f"DEBUG: {message}", UserPermissionLevel.USER)
    
    def error(self, message: str) -> Union[str, None]:
        """
        Log an error message (requires ADMIN permissions).
        
        :param message: The error message to log
        :return: The logged message if permission is sufficient, None otherwise
        """
        return self.log(f"ERROR: {message}", UserPermissionLevel.ADMIN)