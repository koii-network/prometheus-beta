import pytest
import sys
from io import StringIO
from src.progress_logger import dynamic_progress_logger

def test_dynamic_progress_logger_with_list():
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Test with a simple list
    test_list = list(range(10))
    result = list(dynamic_progress_logger(test_list, total=10))
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check results
    assert result == test_list
    output = captured_output.getvalue()
    assert 'Progress:' in output
    assert '%' in output

def test_dynamic_progress_logger_with_generator():
    # Create a generator
    def test_generator():
        for i in range(5):
            yield i
    
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Test with generator
    result = list(dynamic_progress_logger(test_generator(), total=5))
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check results
    assert result == list(range(5))
    output = captured_output.getvalue()
    assert 'Progress:' in output
    assert '%' in output

def test_dynamic_progress_logger_invalid_total():
    with pytest.raises(ValueError, match="Total must be a positive number"):
        list(dynamic_progress_logger(range(10), total=0))

def test_dynamic_progress_logger_custom_params():
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Test with custom parameters
    test_list = list(range(5))
    result = list(dynamic_progress_logger(
        test_list, 
        total=5, 
        prefix='Loading:', 
        suffix='Done', 
        decimals=2, 
        length=20
    ))
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check results
    assert result == test_list
    output = captured_output.getvalue()
    assert 'Loading:' in output
    assert 'Done' in output