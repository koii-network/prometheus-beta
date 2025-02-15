import pytest
import io
import sys
from src.progress_logger import dynamic_progress_bar

def test_progress_bar_iteration():
    """Test that the progress bar works with standard iteration."""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Create a sample list and iterate through it
    test_list = list(range(10))
    processed_items = list(dynamic_progress_bar(test_list, desc='Test'))
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check that all items were processed
    assert processed_items == test_list
    
    # Check output contains expected patterns
    output = captured_output.getvalue()
    assert 'Test: [' in output
    assert ']' in output
    assert '%' in output

def test_progress_bar_custom_length():
    """Test progress bar with custom bar length."""
    test_list = list(range(5))
    
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    processed_items = list(dynamic_progress_bar(test_list, bar_length=20, desc='Custom'))
    
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    assert 'Custom: [' in output
    
    # Verify custom bar length
    assert len(output.split('[')[1].split(']')[0]) <= 20

def test_progress_bar_empty_list():
    """Test progress bar with an empty list."""
    test_list = []
    
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    processed_items = list(dynamic_progress_bar(test_list, desc='Empty'))
    
    sys.stdout = sys.__stdout__
    
    # Ensure no error is raised and list is processed
    assert processed_items == []
    
    # No meaningful output for an empty list