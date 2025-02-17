from enum import Enum, auto
import logging

class UserPermissionLevel(Enum):
    GUEST = 1
    USER = 2
    ADMIN = 3

class PermissionLogger:
    def __init__(self, user_permission_level=UserPermissionLevel.GUEST):
        """
        Initialize the logger with a specific user permission level.
        
        :param user_permission_level: Permission level of the user
        """
        self.user_permission_level = user_permission_level
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
    
    def log(self, message, min_permission_level=UserPermissionLevel.GUEST):
        """
        Log a message based on user permission level.
        
        :param message: Message to log
        :param min_permission_level: Minimum permission level required to log the message
        :return: True if message was logged, False otherwise
        """
        if self.user_permission_level.value >= min_permission_level.value:
            self.logger.info(message)
            return True
        return False
    
    def debug(self, message):
        """
        Log debug messages for admin users only.
        
        :param message: Debug message to log
        :return: True if message was logged, False otherwise
        """
        return self.log(message, UserPermissionLevel.ADMIN)
    
    def warn(self, message):
        """
        Log warning messages for users and admins.
        
        :param message: Warning message to log
        :return: True if message was logged, False otherwise
        """
        return self.log(message, UserPermissionLevel.USER)