import pytest
from src.console_logger import ConsoleLogger, UserPermissionLevel

class TestConsoleLogger:
    def test_log_message_admin_full_access(self, capsys):
        """Test that admin can log messages at all levels"""
        message = "Admin message"
        result = ConsoleLogger.log_message(
            message, 
            user_permission=UserPermissionLevel.ADMIN
        )
        captured = capsys.readouterr()
        assert result == message
        assert "[ADMIN]" in captured.out
        assert message in captured.out

    def test_log_message_user_default_level(self, capsys):
        """Test that a regular user can log messages at default level"""
        message = "User message"
        result = ConsoleLogger.log_message(
            message, 
            user_permission=UserPermissionLevel.USER
        )
        captured = capsys.readouterr()
        assert result == message
        assert "[USER]" in captured.out
        assert message in captured.out

    def test_log_message_guest_insufficient_permission(self, capsys):
        """Test that a guest cannot log messages above their permission level"""
        message = "Guest message"
        result = ConsoleLogger.log_message(
            message, 
            user_permission=UserPermissionLevel.GUEST,
            min_permission_level=UserPermissionLevel.USER
        )
        captured = capsys.readouterr()
        assert result is None
        assert captured.out == ""

    def test_log_message_empty_message_raises_error(self):
        """Test that empty messages raise a ValueError"""
        with pytest.raises(ValueError, match="Message cannot be empty or None"):
            ConsoleLogger.log_message(
                "", 
                user_permission=UserPermissionLevel.USER
            )

    def test_log_message_none_message_raises_error(self):
        """Test that None messages raise a ValueError"""
        with pytest.raises(ValueError, match="Message cannot be empty or None"):
            ConsoleLogger.log_message(
                None, 
                user_permission=UserPermissionLevel.USER
            )

    def test_log_message_invalid_permission_type(self):
        """Test that invalid permission types raise a TypeError"""
        with pytest.raises(TypeError, match="user_permission must be a UserPermissionLevel"):
            ConsoleLogger.log_message(
                "Test message", 
                user_permission="not a permission"
            )

    def test_log_message_custom_min_permission(self, capsys):
        """Test logging with a custom minimum permission level"""
        message = "Admin-only message"
        result = ConsoleLogger.log_message(
            message, 
            user_permission=UserPermissionLevel.ADMIN,
            min_permission_level=UserPermissionLevel.ADMIN
        )
        captured = capsys.readouterr()
        assert result == message
        assert "[ADMIN]" in captured.out
        assert message in captured.out