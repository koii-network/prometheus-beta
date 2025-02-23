import logging
from enum import Enum, auto
from typing import Optional, Any

class UserPermissionLevel(Enum):
    """Enum representing different user permission levels."""
    GUEST = 0
    USER = 1
    ADMIN = 2

class ConsoleLogger:
    """
    A logger that restricts console message logging based on user permissions.
    """
    def __init__(self, user_permission: UserPermissionLevel = UserPermissionLevel.GUEST):
        """
        Initialize the logger with a user's permission level.
        
        :param user_permission: Permission level of the user, defaults to GUEST
        """
        self.user_permission = user_permission
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def log(self, message: str, min_permission: UserPermissionLevel = UserPermissionLevel.USER) -> Optional[str]:
        """
        Log a message if the user has sufficient permissions.
        
        :param message: Message to log
        :param min_permission: Minimum permission level required to log the message
        :return: Logged message if permissions allow, None otherwise
        """
        if self.user_permission.value >= min_permission.value:
            self.logger.info(message)
            return message
        return None

    def log_error(self, message: str, min_permission: UserPermissionLevel = UserPermissionLevel.ADMIN) -> Optional[str]:
        """
        Log an error message if the user has sufficient permissions.
        
        :param message: Error message to log
        :param min_permission: Minimum permission level required to log the error
        :return: Logged error message if permissions allow, None otherwise
        """
        if self.user_permission.value >= min_permission.value:
            self.logger.error(message)
            return message
        return None

    def log_debug(self, message: str, min_permission: UserPermissionLevel = UserPermissionLevel.ADMIN) -> Optional[str]:
        """
        Log a debug message if the user has sufficient permissions.
        
        :param message: Debug message to log
        :param min_permission: Minimum permission level required to log the debug message
        :return: Logged debug message if permissions allow, None otherwise
        """
        if self.user_permission.value >= min_permission.value:
            self.logger.debug(message)
            return message
        return None