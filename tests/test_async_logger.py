import asyncio
import logging
import pytest
from src.async_logger import log_async_execution_time

# Configure a test logger
test_logger = logging.getLogger('test_logger')
test_logger.setLevel(logging.INFO)

# Capture log messages
class LogCapture:
    def __init__(self):
        self.messages = []
    
    def info(self, message):
        self.messages.append(('info', message))
    
    def error(self, message):
        self.messages.append(('error', message))

@pytest.mark.asyncio
async def test_log_async_execution_time():
    # Create log capture
    log_capture = LogCapture()
    
    # Define a test async function
    @log_async_execution_time(logger=log_capture)
    async def test_function(delay):
        await asyncio.sleep(delay)
        return "Success"
    
    # Execute the function
    result = await test_function(0.1)
    
    # Assertions
    assert result == "Success"
    assert len(log_capture.messages) == 1
    assert log_capture.messages[0][0] == 'info'
    assert 'test_function' in log_capture.messages[0][1]
    assert 'executed in' in log_capture.messages[0][1]

@pytest.mark.asyncio
async def test_log_async_execution_time_with_exception():
    # Create log capture
    log_capture = LogCapture()
    
    # Define a test async function that raises an exception
    @log_async_execution_time(logger=log_capture)
    async def error_function():
        await asyncio.sleep(0.1)
        raise ValueError("Test error")
    
    # Execute the function and expect an exception
    with pytest.raises(ValueError, match="Test error"):
        await error_function()
    
    # Assertions
    assert len(log_capture.messages) == 1
    assert log_capture.messages[0][0] == 'error'
    assert 'error_function' in log_capture.messages[0][1]
    assert 'failed' in log_capture.messages[0][1]