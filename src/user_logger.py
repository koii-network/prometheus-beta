from enum import Enum
from typing import Optional, Union

class UserPermission(Enum):
    """Enum representing different user permission levels."""
    GUEST = 1
    USER = 2
    ADMIN = 3

class UserLogger:
    """
    A logger class that manages console message logging based on user permissions.
    
    Supports different logging levels corresponding to user permission levels.
    Messages are only logged if the user's permission meets the minimum required level.
    """
    
    def __init__(self, user_permission: UserPermission = UserPermission.GUEST):
        """
        Initialize the UserLogger with a specific user permission level.
        
        :param user_permission: Permission level of the user, defaults to GUEST
        """
        self.user_permission = user_permission
    
    def log(self, message: str, min_permission: UserPermission = UserPermission.GUEST) -> Optional[str]:
        """
        Log a message if the user's permission level meets the minimum required level.
        
        :param message: The message to log
        :param min_permission: Minimum permission level required to log the message
        :return: The logged message if permission is sufficient, otherwise None
        :raises ValueError: If message is empty or None
        """
        # Validate input
        if not message:
            raise ValueError("Message cannot be empty")
        
        # Check if user has sufficient permissions
        if self.user_permission.value >= min_permission.value:
            print(message)
            return message
        
        return None