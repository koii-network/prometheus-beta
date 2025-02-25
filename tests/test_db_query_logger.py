import pytest
import logging
import time
from unittest.mock import Mock, patch
from src.db_query_logger import log_query_time

class TestQueryLogger:
    def test_log_query_time_decorator(self, caplog):
        """
        Test that the decorator logs query execution time correctly.
        """
        caplog.set_level(logging.INFO)
        
        @log_query_time
        def mock_query():
            time.sleep(0.1)  # Simulate a slow query
            return "Result"
        
        result = mock_query()
        
        # Check correct result
        assert result == "Result"
        
        # Check logging output
        assert len(caplog.records) == 1
        log_record = caplog.records[0]
        assert log_record.levelno == logging.INFO
        assert "mock_query" in log_record.message
        assert "ms" in log_record.message
    
    def test_log_query_time_with_exception(self):
        """
        Test that exceptions are logged and re-raised.
        """
        with patch('logging.error') as mock_log_error:
            @log_query_time
            def query_with_error():
                raise ValueError("Test Error")
            
            with pytest.raises(ValueError, match="Test Error"):
                query_with_error()
            
            # Verify error was logged
            mock_log_error.assert_called_once()
            log_message = mock_log_error.call_args[0][0]
            assert "Error in query" in log_message
    
    def test_decorator_preserves_function_metadata(self):
        """
        Test that function metadata is preserved after decoration.
        """
        def original_query(param1, param2):
            """Docstring for original query."""
            return f"{param1}-{param2}"
        
        decorated_query = log_query_time(original_query)
        
        # Check preserved metadata
        assert decorated_query.__name__ == original_query.__name__
        assert decorated_query.__doc__ == original_query.__doc__
    
    def test_performance_logging_accuracy(self):
        """
        Test that execution time is logged with reasonable accuracy.
        """
        @log_query_time
        def slow_query():
            time.sleep(0.05)  # 50ms sleep
        
        with patch('logging.info') as mock_log_info:
            slow_query()
            
            # Verify logging call
            mock_log_info.assert_called_once()
            log_message = mock_log_info.call_args[0][0]
            
            # Extract logged time
            import re
            time_match = re.search(r'(\d+\.\d+) ms', log_message)
            assert time_match is not None
            
            logged_time = float(time_match.group(1))
            
            # Check logged time is close to actual sleep time (with some tolerance)
            assert 45 <= logged_time <= 55, f"Logged time {logged_time} ms is not within expected range"