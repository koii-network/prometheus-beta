from enum import Enum
from typing import Optional, Union

class UserPermissionLevel(Enum):
    """Enumeration of user permission levels."""
    GUEST = 0
    USER = 1
    ADMIN = 2

class ConsoleLogger:
    """
    A logger that controls message logging based on user permission levels.
    
    This class provides a method to log messages with different verbosity levels
    depending on the user's permission level.
    """
    
    @staticmethod
    def log_message(
        message: str, 
        user_permission: UserPermissionLevel, 
        min_permission_level: UserPermissionLevel = UserPermissionLevel.USER
    ) -> Optional[str]:
        """
        Log a message based on user permissions.
        
        Args:
            message (str): The message to be logged
            user_permission (UserPermissionLevel): Current user's permission level
            min_permission_level (UserPermissionLevel, optional): 
                Minimum permission level required to log the message. 
                Defaults to UserPermissionLevel.USER.
        
        Returns:
            Optional[str]: The logged message if permission is sufficient, 
                           None otherwise
        
        Raises:
            ValueError: If message is empty or None
            TypeError: If incorrect types are provided
        """
        # Validate inputs
        if message is None or message.strip() == "":
            raise ValueError("Message cannot be empty or None")
        
        if not isinstance(user_permission, UserPermissionLevel):
            raise TypeError("user_permission must be a UserPermissionLevel")
        
        if not isinstance(min_permission_level, UserPermissionLevel):
            raise TypeError("min_permission_level must be a UserPermissionLevel")
        
        # Check if user has sufficient permissions to log the message
        if user_permission.value >= min_permission_level.value:
            # In a real-world scenario, this might use a proper logging framework
            print(f"[{user_permission.name}] {message}")
            return message
        
        # If insufficient permissions, return None
        return None