import pytest
import sys
from io import StringIO
from src.progress_logger import dynamic_progress_bar


def test_progress_bar_with_list():
    """Test progress bar with a standard list"""
    test_list = list(range(10))
    
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Run progress bar
    processed_items = list(dynamic_progress_bar(test_list))
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check results
    assert processed_items == test_list
    output = captured_output.getvalue()
    assert 'Progress: |' in output
    assert '100%' in output


def test_progress_bar_with_generator():
    """Test progress bar with a generator"""
    def test_generator():
        for i in range(5):
            yield i
    
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Run progress bar
    processed_items = list(dynamic_progress_bar(test_generator()))
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check results
    assert processed_items == list(range(5))
    output = captured_output.getvalue()
    assert 'Progress: 5 items processed' in output


def test_progress_bar_custom_description():
    """Test progress bar with custom description"""
    test_list = list(range(3))
    
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Run progress bar
    processed_items = list(dynamic_progress_bar(test_list, desc='Custom'))
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check results
    assert processed_items == test_list
    output = captured_output.getvalue()
    assert 'Custom: |' in output


def test_progress_bar_invalid_length():
    """Test that progress bar raises ValueError for too short bar length"""
    with pytest.raises(ValueError, match="Progress bar length must be at least 10 characters"):
        list(dynamic_progress_bar(range(10), bar_length=5))


def test_progress_bar_empty_iterable():
    """Test progress bar with empty iterable"""
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Run progress bar
    processed_items = list(dynamic_progress_bar([]))
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check results
    assert processed_items == []
    output = captured_output.getvalue()
    assert '|' in output  # Basic progress bar structure should still be present
    assert '100%' in output