import pytest
import time
from src.process_logger import ProcessLogger
import logging
from io import StringIO

def test_process_logger_with_known_total_steps():
    # Capture log output
    log_capture = StringIO()
    handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    def example_process(total_steps):
        for i in range(total_steps):
            time.sleep(0.1)  # Simulate work
            yield i

    process_logger = ProcessLogger(logger)
    steps = 5
    result = list(process_logger.log_progress(example_process, total_steps=steps))

    # Check results
    assert len(result) == steps
    
    # Check log output contains progress information
    log_output = log_capture.getvalue()
    assert "Progress:" in log_output
    assert f"{steps}/{steps}" in log_output

def test_process_logger_without_total_steps():
    # Capture log output
    log_capture = StringIO()
    handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    def example_process():
        for i in range(3):
            time.sleep(0.1)  # Simulate work
            yield i

    process_logger = ProcessLogger(logger)
    result = list(process_logger.log_progress(example_process))

    # Check results
    assert len(result) == 3
    
    # Check log output contains progress information
    log_output = log_capture.getvalue()
    assert "Progress:" in log_output
    assert "steps" in log_output

def test_process_logger_non_iterable_function():
    # Capture log output
    log_capture = StringIO()
    handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    def simple_function():
        return "Hello, World!"

    process_logger = ProcessLogger(logger)
    result = process_logger.log_progress(simple_function)

    # Check result
    assert result == "Hello, World!"
    
    # Check log output
    log_output = log_capture.getvalue()
    assert "does not return an iterable" in log_output