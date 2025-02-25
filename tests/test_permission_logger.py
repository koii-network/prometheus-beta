import pytest
import logging
import io
import sys
from src.permission_logger import PermissionLogger, UserPermissionLevel

class TestPermissionLogger:
    @pytest.fixture
    def captured_output(self):
        """Fixture to capture console output."""
        output = io.StringIO()
        return output
    
    def test_default_logging(self, captured_output):
        """Test default logging behavior for a regular user."""
        # Create logger with captured output
        logger = PermissionLogger(output_stream=captured_output)
        
        # Log info message (default permission level)
        result = logger.log("Test info message")
        assert result is True
        
        # Check console output
        output = captured_output.getvalue().strip()
        assert "Test info message" in output
    
    def test_permission_levels(self, captured_output):
        """Test logging with different permission levels."""
        # Create logger with captured output
        logger = PermissionLogger(output_stream=captured_output)
        
        # Guest tries to log admin message
        result = logger.log(
            "Admin message", 
            min_permission=UserPermissionLevel.ADMIN, 
            user_permission=UserPermissionLevel.GUEST
        )
        assert result is False
        
        # Admin logs message requiring admin permissions
        result = logger.log(
            "Secret admin message", 
            min_permission=UserPermissionLevel.ADMIN, 
            user_permission=UserPermissionLevel.ADMIN
        )
        assert result is True
        
        # Check console output
        output = captured_output.getvalue()
        assert "Secret admin message" in output
    
    def test_log_levels(self, captured_output):
        """Test different logging levels."""
        # Create logger with captured output
        logger = PermissionLogger(output_stream=captured_output)
        
        # Test all log levels
        log_levels = ['debug', 'info', 'warning', 'error', 'critical']
        for level in log_levels:
            result = logger.log(f"Test {level} message", level=level)
            assert result is True
    
    def test_invalid_log_level(self):
        """Test raising ValueError for invalid log level."""
        logger = PermissionLogger()
        
        with pytest.raises(ValueError, match="Invalid logging level"):
            logger.log("Invalid message", level="invalid_level")
    
    def test_file_logging(self, tmp_path):
        """Test logging to a file."""
        log_file = tmp_path / "test.log"
        logger = PermissionLogger(str(log_file))
        
        # Log a message
        logger.log("File log test")
        
        # Read the log file
        with open(log_file, 'r') as f:
            log_content = f.read()
        
        assert "File log test" in log_content