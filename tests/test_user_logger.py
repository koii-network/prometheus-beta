import pytest
from src.user_logger import UserLogger, UserPermission

class TestUserLogger:
    def test_guest_logger_default(self, capsys):
        """Test logging for guest user with default permission."""
        logger = UserLogger(UserPermission.GUEST)
        result = logger.log("Guest message")
        captured = capsys.readouterr()
        assert result == "Guest message"
        assert "Guest message" in captured.out
    
    def test_guest_logger_restricted_message(self, capsys):
        """Test that guest cannot log messages requiring higher permissions."""
        logger = UserLogger(UserPermission.GUEST)
        result = logger.log("Admin message", UserPermission.ADMIN)
        captured = capsys.readouterr()
        assert result is None
        assert "Admin message" not in captured.out
    
    def test_admin_logger_all_messages(self, capsys):
        """Test that admin can log all messages."""
        logger = UserLogger(UserPermission.ADMIN)
        result = logger.log("Guest message")
        result_admin = logger.log("Admin message", UserPermission.ADMIN)
        captured = capsys.readouterr()
        assert result == "Guest message"
        assert result_admin == "Admin message"
        assert "Guest message" in captured.out
        assert "Admin message" in captured.out
    
    def test_user_logger_intermediate_permissions(self, capsys):
        """Test logging for user with intermediate permissions."""
        logger = UserLogger(UserPermission.USER)
        result_guest = logger.log("Guest message")
        result_user = logger.log("User message", UserPermission.USER)
        result_admin = logger.log("Admin message", UserPermission.ADMIN)
        captured = capsys.readouterr()
        assert result_guest == "Guest message"
        assert result_user == "User message"
        assert result_admin is None
        assert "Guest message" in captured.out
        assert "User message" in captured.out
        assert "Admin message" not in captured.out
    
    def test_empty_message_raises_error(self):
        """Test that empty messages raise a ValueError."""
        logger = UserLogger()
        with pytest.raises(ValueError, match="Message cannot be empty"):
            logger.log("")
        
        with pytest.raises(ValueError, match="Message cannot be empty"):
            logger.log(None)  # type: ignore