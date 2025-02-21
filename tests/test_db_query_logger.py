import pytest
import logging
import time
from src.db_query_logger import log_query_time

class MockLogger:
    def __init__(self):
        self.info_logs = []
        self.error_logs = []
    
    def info(self, message):
        self.info_logs.append(message)
    
    def error(self, message):
        self.error_logs.append(message)

def test_log_query_time_success():
    mock_logger = MockLogger()
    
    @log_query_time(logger=mock_logger)
    def mock_database_query():
        time.sleep(0.1)  # Simulate query execution
        return "Data"
    
    result = mock_database_query()
    
    assert result == "Data"
    assert len(mock_logger.info_logs) == 1
    assert "mock_database_query" in mock_logger.info_logs[0]
    assert "0.1" in mock_logger.info_logs[0]

def test_log_query_time_error():
    mock_logger = MockLogger()
    
    @log_query_time(logger=mock_logger)
    def mock_failing_query():
        time.sleep(0.05)  # Simulate partial query execution
        raise ValueError("Database error")
    
    with pytest.raises(ValueError, match="Database error"):
        mock_failing_query()
    
    assert len(mock_logger.error_logs) == 1
    assert "mock_failing_query" in mock_logger.error_logs[0]
    assert "0.05" in mock_logger.error_logs[0]
    assert "Database error" in mock_logger.error_logs[0]