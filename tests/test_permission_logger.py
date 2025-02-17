import pytest
import logging
from io import StringIO
import sys

from src.permission_logger import PermissionLogger, UserPermissionLevel

class TestPermissionLogger:
    def test_guest_logger_default_logging(self, caplog):
        """Test that guest can log basic messages"""
        logger = PermissionLogger(UserPermissionLevel.GUEST)
        assert logger.log("Guest message") == True
        assert "Guest message" in caplog.text
    
    def test_guest_logger_restricted_logging(self, caplog):
        """Test that guest cannot log admin messages"""
        logger = PermissionLogger(UserPermissionLevel.GUEST)
        assert logger.debug("Admin debug message") == False
        assert "Admin debug message" not in caplog.text
    
    def test_user_logger_logging(self, caplog):
        """Test that user can log user-level messages"""
        logger = PermissionLogger(UserPermissionLevel.USER)
        assert logger.log("User message") == True
        assert logger.warn("User warning") == True
        assert logger.debug("Admin debug message") == False
    
    def test_admin_logger_full_logging(self, caplog):
        """Test that admin can log all messages"""
        logger = PermissionLogger(UserPermissionLevel.ADMIN)
        assert logger.log("Admin message") == True
        assert logger.warn("Admin warning") == True
        assert logger.debug("Admin debug message") == True
    
    def test_logger_permission_levels(self):
        """Test different permission levels"""
        assert UserPermissionLevel.GUEST.value < UserPermissionLevel.USER.value
        assert UserPermissionLevel.USER.value < UserPermissionLevel.ADMIN.value