import pytest
import sys
from io import StringIO
from src.progress_logger import dynamic_progress_log

def test_basic_functionality():
    # Test with a simple list
    items = [1, 2, 3, 4, 5]
    result = dynamic_progress_log(items)
    assert result == items

def test_description():
    # Test with a custom description
    items = range(10)
    result = dynamic_progress_log(items, description="Test Progress")
    assert list(result) == list(items)

def test_logging_interval():
    # Capture stderr to verify logging
    old_stderr = sys.stderr
    sys.stderr = captured_output = StringIO()
    
    items = list(range(10))
    result = dynamic_progress_log(items, log_every=3)
    
    sys.stderr = old_stderr
    logged_output = captured_output.getvalue()
    
    assert result == items
    assert logged_output.count("Processed") == 3  # Should log at 3, 6, 9

def test_custom_total():
    # Test with custom total
    items = range(5)
    result = dynamic_progress_log(items, total=10)
    assert list(result) == list(items)

def test_invalid_inputs():
    # Test error handling
    with pytest.raises(TypeError):
        dynamic_progress_log(42)  # Not an iterable
    
    with pytest.raises(ValueError):
        dynamic_progress_log(range(10), log_every=0)  # Invalid log_every

def test_empty_iterable():
    # Test with empty iterable
    items = []
    result = dynamic_progress_log(items)
    assert result == []