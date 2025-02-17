import pytest
import time
from src.process_logger import log_process_progress

def test_log_process_progress():
    """Test the process logging decorator."""
    # Prepare a test list
    test_items = ['apple', 'banana', 'cherry']
    
    # Use the decorator
    @log_process_progress
    def process_items(items):
        processed = []
        for item in items:
            time.sleep(0.1)  # Simulate processing
            processed.append(item.upper())
        return processed
    
    # Run the decorated function
    result = process_items(test_items)
    
    # Assertions
    assert result == ['APPLE', 'BANANA', 'CHERRY']
    assert len(result) == len(test_items)

def test_log_process_progress_empty_list():
    """Test with an empty list."""
    @log_process_progress
    def process_empty_list(items):
        return []
    
    result = process_empty_list([])
    assert result == []

def test_log_process_progress_custom_total():
    """Test with a custom total parameter."""
    @log_process_progress
    def custom_total_task(total=10):
        for _ in range(total):
            time.sleep(0.1)
        return True
    
    result = custom_total_task(total=5)
    assert result is True