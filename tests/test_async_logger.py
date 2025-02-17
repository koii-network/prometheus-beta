import asyncio
import logging
import pytest
import time
from src.async_logger import log_async_execution_time

# Configure a test logger
test_logger = logging.getLogger('test_async_logger')
test_logger.setLevel(logging.INFO)

class LogCapture:
    def __init__(self):
        self.logs = []
    
    def info(self, msg):
        self.logs.append(('INFO', msg))
    
    def error(self, msg):
        self.logs.append(('ERROR', msg))

@pytest.mark.asyncio
async def test_log_async_execution_time_success():
    # Capture logs
    log_capture = LogCapture()
    
    # Create a sample async function with logging
    @log_async_execution_time(logger=log_capture)
    async def sample_async_function():
        await asyncio.sleep(0.1)  # Simulate some async work
        return "Success"
    
    # Call the function
    result = await sample_async_function()
    
    # Assertions
    assert result == "Success"
    assert len(log_capture.logs) == 1
    assert log_capture.logs[0][0] == 'INFO'
    assert 'sample_async_function' in log_capture.logs[0][1]
    assert 'executed in' in log_capture.logs[0][1]

@pytest.mark.asyncio
async def test_log_async_execution_time_exception():
    # Capture logs
    log_capture = LogCapture()
    
    # Create a sample async function that raises an exception
    @log_async_execution_time(logger=log_capture)
    async def error_async_function():
        await asyncio.sleep(0.1)
        raise ValueError("Test error")
    
    # Call the function and expect an exception
    with pytest.raises(ValueError, match="Test error"):
        await error_async_function()
    
    # Assertions
    assert len(log_capture.logs) == 1
    assert log_capture.logs[0][0] == 'ERROR'
    assert 'error_async_function' in log_capture.logs[0][1]
    assert 'failed' in log_capture.logs[0][1]

@pytest.mark.asyncio
async def test_log_async_execution_time_performance():
    @log_async_execution_time()
    async def slow_function():
        await asyncio.sleep(0.2)
        return "Slow result"
    
    start_time = time.perf_counter()
    result = await slow_function()
    end_time = time.perf_counter()
    
    # Verify result and ensure execution took roughly 0.2 seconds
    assert result == "Slow result"
    execution_time = end_time - start_time
    assert 0.19 < execution_time < 0.25  # Allow some variance