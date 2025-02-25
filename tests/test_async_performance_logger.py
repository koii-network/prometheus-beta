import asyncio
import logging
import pytest
from src.async_performance_logger import log_async_execution_time

# Create a custom logger for testing
test_logger = logging.getLogger('test_async_logger')
test_logger.setLevel(logging.INFO)

class LogCapture:
    def __init__(self):
        self.records = []
    
    def info(self, msg):
        self.records.append(msg)
    
    def error(self, msg):
        self.records.append(msg)

async def test_log_async_execution_time_success():
    log_capture = LogCapture()
    
    @log_async_execution_time(logger_obj=log_capture)
    async def test_async_func():
        await asyncio.sleep(0.1)  # Simulate work
        return "Success"
    
    result = await test_async_func()
    
    assert result == "Success"
    assert len(log_capture.records) == 1
    assert "test_async_func" in log_capture.records[0]
    assert "0.1" in log_capture.records[0]

async def test_log_async_execution_time_zero_duration():
    log_capture = LogCapture()
    
    @log_async_execution_time(logger_obj=log_capture)
    async def instant_func():
        return "Instant"
    
    result = await instant_func()
    
    assert result == "Instant"
    assert len(log_capture.records) == 1
    assert "0.0" in log_capture.records[0]

async def test_log_async_execution_time_exception():
    log_capture = LogCapture()
    
    @log_async_execution_time(logger_obj=log_capture)
    async def error_func():
        await asyncio.sleep(0.05)
        raise ValueError("Test Error")
    
    with pytest.raises(ValueError, match="Test Error"):
        await error_func()
    
    assert len(log_capture.records) == 1
    assert "failed" in log_capture.records[0]
    assert "0.0" in log_capture.records[0]