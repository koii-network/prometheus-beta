import pytest
import asyncio
import logging
from src.async_logger import log_async_execution_time

# Configure a test logger
class TestLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(('info', message))
    
    def error(self, message):
        self.logs.append(('error', message))

@pytest.mark.asyncio
async def test_log_async_execution_time():
    test_logger = TestLogger()
    
    @log_async_execution_time(logger=test_logger)
    async def sample_async_function(delay):
        await asyncio.sleep(delay)
        return "Done"
    
    # Test successful execution
    result = await sample_async_function(0.1)
    assert result == "Done"
    
    # Check logging
    assert len(test_logger.logs) == 1
    log_type, log_message = test_logger.logs[0]
    assert log_type == 'info'
    assert 'sample_async_function' in log_message
    assert 'executed in' in log_message

@pytest.mark.asyncio
async def test_log_async_execution_time_error():
    test_logger = TestLogger()
    
    @log_async_execution_time(logger=test_logger)
    async def failing_async_function():
        await asyncio.sleep(0.1)
        raise ValueError("Test error")
    
    # Test error handling
    with pytest.raises(ValueError):
        await failing_async_function()
    
    # Check error logging
    assert len(test_logger.logs) == 1
    log_type, log_message = test_logger.logs[0]
    assert log_type == 'error'
    assert 'failing_async_function' in log_message
    assert 'failed' in log_message
    assert 'Test error' in log_message