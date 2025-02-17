import pytest
import time
import io
import sys
from contextlib import contextmanager
from src.progress_logger import dynamic_progress_logger

@contextmanager
def capture_stdout():
    """Capture stdout for testing print operations."""
    old_stdout = sys.stdout
    sys.stdout = captured_output = io.StringIO()
    try:
        yield captured_output
    finally:
        sys.stdout = old_stdout

def test_progress_logger_with_known_total():
    """Test progress logger with a known total."""
    test_list = list(range(10))
    
    with capture_stdout() as output:
        list(dynamic_progress_logger(test_list, total=10))
        stdout_content = output.getvalue()
    
    assert 'Progress: [' in stdout_content
    assert '%' in stdout_content

def test_progress_logger_with_unknown_total():
    """Test progress logger with an unknown total."""
    test_generator = (x for x in range(5))
    
    with capture_stdout() as output:
        list(dynamic_progress_logger(test_generator))
        stdout_content = output.getvalue()
    
    assert 'Progress: [' in stdout_content

def test_progress_logger_custom_description():
    """Test custom description."""
    test_list = list(range(5))
    
    with capture_stdout() as output:
        list(dynamic_progress_logger(test_list, desc='Custom Desc', total=5))
        stdout_content = output.getvalue()
    
    assert 'Custom Desc: [' in stdout_content

def test_progress_logger_preserves_iteration():
    """Ensure the logger preserves original iteration."""
    test_list = list(range(10))
    
    result = list(dynamic_progress_logger(test_list, total=10))
    
    assert result == test_list

def test_progress_logger_update_interval():
    """Test custom update interval."""
    test_list = list(range(100))
    
    start_time = time.time()
    with capture_stdout() as output:
        list(dynamic_progress_logger(test_list, total=100, update_interval=0.5))
        total_time = time.time() - start_time
    
    # Should not update too frequently
    assert total_time >= 0.5