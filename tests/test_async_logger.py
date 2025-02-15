import asyncio
import logging
import pytest
from src.async_logger import log_async_execution_time

# Mock logger for testing
class MockLogger:
    def __init__(self):
        self.info_logs = []
        self.error_logs = []
    
    def info(self, message):
        self.info_logs.append(message)
    
    def error(self, message):
        self.error_logs.append(message)

@log_async_execution_time()
async def sample_async_function(delay):
    """Sample async function that simulates work with a delay."""
    await asyncio.sleep(delay)
    return f"Completed after {delay} seconds"

@log_async_execution_time()
async def failing_async_function():
    """Sample async function that raises an exception."""
    raise ValueError("Intentional error")

@pytest.mark.asyncio
async def test_log_async_execution_time_success():
    """Test logging of successful async function execution."""
    mock_logger = MockLogger()
    
    with log_async_execution_time(mock_logger):
        result = await sample_async_function(0.1)
    
    assert result == "Completed after 0.1 seconds"
    assert len(mock_logger.info_logs) == 1
    
    log_message = mock_logger.info_logs[0]
    assert "sample_async_function" in log_message
    assert "execution time" in log_message
    assert float(log_message.split(":")[1].split()[0]) >= 0.1

@pytest.mark.asyncio
async def test_log_async_execution_time_failure():
    """Test logging of async function execution failure."""
    mock_logger = MockLogger()
    
    with pytest.raises(ValueError):
        with log_async_execution_time(mock_logger):
            await failing_async_function()
    
    assert len(mock_logger.error_logs) == 1
    
    error_message = mock_logger.error_logs[0]
    assert "failing_async_function" in error_message
    assert "failed" in error_message
    assert "Intentional error" in error_message

@pytest.mark.asyncio
async def test_log_async_execution_time_default_logger():
    """Test that default logging works when no custom logger is provided."""
    # Capture logs from root logger
    with log_async_execution_time():
        result = await sample_async_function(0.05)
    
    assert result == "Completed after 0.05 seconds"