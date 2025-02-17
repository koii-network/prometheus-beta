import sys
import io
import pytest
from src.colored_logger import ColoredLogger

class TestColoredLogger:
    def test_default_logging(self):
        """Test default logging behavior"""
        # Redirect stdout to capture print output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        ColoredLogger.log("Test message")
        
        # Reset redirect
        sys.stdout = sys.__stdout__
        
        # The test passes if no exception is raised

    def test_specific_bg_color(self):
        """Test logging with a specific background color"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        ColoredLogger.log("Colored background", bg_color='blue')
        
        # Reset redirect
        sys.stdout = sys.__stdout__
        
        # The test passes if no exception is raised

    def test_specific_text_color(self):
        """Test logging with a specific text color"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        ColoredLogger.log("Colored text", text_color='red')
        
        # Reset redirect
        sys.stdout = sys.__stdout__
        
        # The test passes if no exception is raised

    def test_invalid_bg_color(self):
        """Test that an invalid background color raises a ValueError"""
        with pytest.raises(ValueError, match="Invalid background color"):
            ColoredLogger.log("Invalid color", bg_color='invalid_color')

    def test_invalid_text_color(self):
        """Test that an invalid text color raises a ValueError"""
        with pytest.raises(ValueError, match="Invalid text color"):
            ColoredLogger.log("Invalid color", text_color='invalid_color')

    def test_custom_file_output(self):
        """Test logging to a custom file stream"""
        custom_output = io.StringIO()
        
        ColoredLogger.log("Custom output", file=custom_output)
        
        # Check content was written to custom stream
        assert "Custom output" in custom_output.getvalue()