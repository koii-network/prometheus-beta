import logging
import time
import pytest
from src.process_progress_logger import ProcessProgressLogger

def test_process_progress_logger_with_function():
    """Test tracking progress of a simple function."""
    def example_process(x, y):
        time.sleep(0.1)  # Simulate work
        return x + y
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    progress_logger = ProcessProgressLogger(logger=logger)
    
    result = progress_logger.track_progress(example_process, 3, 4, total_steps=1)
    assert result == 7

def test_process_progress_logger_with_generator():
    """Test tracking progress of a generator function."""
    def generator_process(n):
        for i in range(n):
            time.sleep(0.1)  # Simulate work
            yield i
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    progress_logger = ProcessProgressLogger(logger=logger)
    
    results = list(progress_logger.track_progress(generator_process, 3, total_steps=3))
    assert results == [0, 1, 2]

def test_process_progress_logger_error_handling():
    """Test error handling in progress tracking."""
    def failing_process():
        raise ValueError("Test error")
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    progress_logger = ProcessProgressLogger(logger=logger)
    
    with pytest.raises(ValueError, match="Test error"):
        progress_logger.track_progress(failing_process)

def test_process_progress_logger_invalid_total_steps():
    """Test invalid total_steps parameter."""
    def example_process():
        pass
    
    logger = logging.getLogger(__name__)
    progress_logger = ProcessProgressLogger(logger=logger)
    
    with pytest.raises(ValueError, match="total_steps must be a positive integer"):
        progress_logger.track_progress(example_process, total_steps=0)
    
    with pytest.raises(ValueError, match="total_steps must be a positive integer"):
        progress_logger.track_progress(example_process, total_steps=-1)

def test_process_progress_logger_optional_total_steps():
    """Test progress tracking without specifying total steps."""
    def example_process(n):
        for _ in range(n):
            time.sleep(0.1)
    
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    
    progress_logger = ProcessProgressLogger(logger=logger)
    
    progress_logger.track_progress(example_process, 3)  # Ensure no error