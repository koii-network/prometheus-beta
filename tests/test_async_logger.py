import asyncio
import logging
import pytest
from src.async_logger import log_async_execution_time

class TestLogger:
    def setup_method(self):
        # Capture logs for verification
        self.log_capture = logging.getLogger('test_logger')
        self.log_capture.handlers = []
        self.log_capture.setLevel(logging.INFO)
        self.log_handler = logging.Handler()
        self.log_capture.addHandler(self.log_handler)

    @log_async_execution_time(logger=logging.getLogger('test_logger'))
    async def _test_async_function(self, delay=0.1):
        await asyncio.sleep(delay)
        return "Success"

    @log_async_execution_time(logger=logging.getLogger('test_logger'))
    async def _test_async_function_with_error(self):
        await asyncio.sleep(0.1)
        raise ValueError("Test error")

    @pytest.mark.asyncio
    async def test_log_async_execution_time_success(self, caplog):
        caplog.set_level(logging.INFO)
        
        result = await self._test_async_function()
        assert result == "Success"
        
        log_records = [record for record in caplog.records if record.levelname == 'INFO']
        assert len(log_records) > 0
        assert "executed in" in log_records[0].message
        assert "_test_async_function" in log_records[0].message

    @pytest.mark.asyncio
    async def test_log_async_execution_time_execution_duration(self, caplog):
        caplog.set_level(logging.INFO)
        
        await self._test_async_function(0.2)
        
        log_records = [record for record in caplog.records if record.levelname == 'INFO']
        assert len(log_records) > 0
        
        # Check execution time is approximately 0.2 seconds
        import re
        time_match = re.search(r'executed in (\d+\.\d+) seconds', log_records[0].message)
        assert time_match is not None
        execution_time = float(time_match.group(1))
        assert 0.19 < execution_time < 0.21

    @pytest.mark.asyncio
    async def test_log_async_execution_time_error(self, caplog):
        caplog.set_level(logging.ERROR)
        
        with pytest.raises(ValueError, match="Test error"):
            await self._test_async_function_with_error()
        
        log_records = [record for record in caplog.records if record.levelname == 'ERROR']
        assert len(log_records) > 0
        assert "failed" in log_records[0].message
        assert "_test_async_function_with_error" in log_records[0].message
        assert "Test error" in log_records[0].message