import time
import logging
import pytest
from src.execution_timer import log_execution_time, example_function

class TestExecutionTimer:
    def test_log_execution_time_default(self, capfd):
        """
        Test default logging (console print) with example function
        """
        result = example_function(3, 4)
        assert result == 7
        
        # Check console output
        captured = capfd.readouterr()
        assert "Function 'example_function' took" in captured.out
        assert "seconds to execute" in captured.out

    def test_log_execution_time_with_custom_logger(self, caplog):
        """
        Test logging with a custom logger
        """
        # Create a test logger
        logger = logging.getLogger('test_logger')
        logger.setLevel(logging.INFO)

        # Create a decorated function with custom logger
        @log_execution_time(logger=logger)
        def test_func():
            time.sleep(0.1)
            return 42

        # Call the function
        result = test_func()
        assert result == 42

        # Check logger record
        assert len(caplog.records) == 1
        log_record = caplog.records[0]
        assert "Function 'test_func' took" in log_record.message
        assert "seconds to execute" in log_record.message

    def test_log_execution_time_timing_accuracy(self):
        """
        Test that the execution time is reasonably accurate
        """
        @log_execution_time()
        def delayed_func():
            time.sleep(0.5)
            return True

        start_time = time.time()
        result = delayed_func()
        end_time = time.time()

        assert result is True
        # Check if the total time is close to the expected sleep time
        assert 0.4 < (end_time - start_time) < 0.6