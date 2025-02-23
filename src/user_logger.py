import logging
from enum import Enum, auto

class UserPermissionLevel(Enum):
    GUEST = auto()
    USER = auto()
    ADMIN = auto()

class UserLogger:
    def __init__(self, user_permission_level=UserPermissionLevel.GUEST):
        """
        Initialize a logger with specific user permission level.
        
        Args:
            user_permission_level (UserPermissionLevel): Permission level of the user
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.user_permission_level = user_permission_level

    def log(self, message, min_permission_level=UserPermissionLevel.GUEST):
        """
        Log a message based on user permissions.
        
        Args:
            message (str): Message to log
            min_permission_level (UserPermissionLevel): Minimum permission level required to log
        
        Returns:
            bool: True if message was logged, False otherwise
        """
        if self.user_permission_level.value >= min_permission_level.value:
            self.logger.info(f"[{self.user_permission_level.name}] {message}")
            return True
        return False

    def log_admin(self, message):
        """
        Log a message only for admin users.
        
        Args:
            message (str): Message to log
        
        Returns:
            bool: True if message was logged, False otherwise
        """
        return self.log(message, min_permission_level=UserPermissionLevel.ADMIN)

    def log_user(self, message):
        """
        Log a message for users and admins.
        
        Args:
            message (str): Message to log
        
        Returns:
            bool: True if message was logged, False otherwise
        """
        return self.log(message, min_permission_level=UserPermissionLevel.USER)