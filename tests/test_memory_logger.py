import logging
import pytest
import sys
import os

# Add the src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from memory_logger import log_memory_usage

# Configure logging to capture log messages
logging.basicConfig(level=logging.INFO)

class TestMemoryLogger:
    def test_memory_logger_basic(self):
        """Test that the memory logger decorator works with a simple function."""
        @log_memory_usage
        def simple_function():
            return [i for i in range(1000)]
        
        # Capture log messages
        with self._capture_logs() as log_records:
            result = simple_function()
        
        # Verify log messages
        assert len(result) == 1000
        assert len(log_records) == 3
        assert "Memory usage before simple_function" in log_records[0]
        assert "Memory usage after simple_function" in log_records[1]
        assert "Memory change during simple_function" in log_records[2]
    
    def test_memory_logger_with_args(self):
        """Test memory logger with a function that takes arguments."""
        @log_memory_usage
        def function_with_args(x, y):
            return [i * x for i in range(y)]
        
        with self._capture_logs() as log_records:
            result = function_with_args(2, 1000)
        
        assert len(result) == 1000
        assert len(log_records) == 3
    
    def test_memory_logger_preserves_function_metadata(self):
        """Ensure the decorator preserves function metadata."""
        @log_memory_usage
        def sample_function(a, b):
            """A sample docstring."""
            return a + b
        
        assert sample_function.__name__ == 'sample_function'
        assert sample_function.__doc__ == 'A sample docstring.'
    
    def _capture_logs(self):
        """Context manager to capture log records."""
        class LogCapture:
            def __init__(self):
                self.records = []
            
            def write(self, record):
                self.records.append(record.getMessage())
        
        class LogCaptureHandler(logging.Handler):
            def __init__(self, capture):
                super().__init__()
                self.capture = capture
            
            def emit(self, record):
                self.capture.write(record)
        
        class LogContext:
            def __init__(self, capture):
                self.capture = capture
                self.handler = LogCaptureHandler(capture)
            
            def __enter__(self):
                logging.getLogger().addHandler(self.handler)
                return self.capture.records
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                logging.getLogger().removeHandler(self.handler)
        
        return LogContext(LogCapture())