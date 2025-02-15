import pytest
import logging
import psutil
from io import StringIO
from src.memory_logger import log_memory_usage

def test_log_memory_usage():
    # Create a string buffer to capture log output
    log_capture = StringIO()
    handler = logging.StreamHandler(log_capture)
    logger = logging.getLogger('test_logger')
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    
    # Call the function
    result = log_memory_usage(logger)
    
    # Assertions
    assert isinstance(result, dict), "Should return a dictionary of memory stats"
    assert 'total' in result, "Should have total memory in stats"
    assert 'available' in result, "Should have available memory in stats"
    assert 'used' in result, "Should have used memory in stats"
    assert 'percent' in result, "Should have memory percent in stats"
    
    # Check value types
    assert isinstance(result['total'], float), "Total memory should be a float"
    assert isinstance(result['available'], float), "Available memory should be a float"
    assert isinstance(result['used'], float), "Used memory should be a float"
    assert isinstance(result['percent'], float), "Memory percentage should be a float"
    
    # Check log output
    log_output = log_capture.getvalue()
    assert "Memory Usage Statistics:" in log_output
    assert "Total Memory:" in log_output
    assert "Available Memory:" in log_output
    assert "Used Memory:" in log_output
    assert "Memory Usage Percentage:" in log_output

def test_memory_stats_reasonable_values():
    # Verify the memory stats are within reasonable ranges
    result = log_memory_usage()
    
    # Total memory should be greater than 0
    assert result['total'] > 0, "Total memory should be positive"
    
    # Available memory should be less than or equal to total memory
    assert result['available'] <= result['total'], "Available memory cannot exceed total memory"
    
    # Used memory should be less than or equal to total memory
    assert result['used'] <= result['total'], "Used memory cannot exceed total memory"
    
    # Percentage should be between 0 and 100
    assert 0 <= result['percent'] <= 100, "Memory percentage should be between 0 and 100"