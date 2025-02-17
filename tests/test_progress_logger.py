import sys
import io
import pytest
from src.progress_logger import dynamic_progress_logger

def test_dynamic_progress_logger():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Test with a simple list
    test_list = list(range(10))
    result = list(dynamic_progress_logger(test_list, description='Test'))
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check if the output contains expected progress indicators
    output = captured_output.getvalue()
    assert 'Test: [' in output
    assert ']' in output
    assert '%' in output
    
    # Verify the result is the same as the input list
    assert result == test_list

def test_dynamic_progress_logger_empty_list():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Test with an empty list
    test_list = []
    result = list(dynamic_progress_logger(test_list, description='Empty'))
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Empty list should not produce any output
    output = captured_output.getvalue()
    assert output == ''
    assert result == []

def test_dynamic_progress_logger_custom_bar_length():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Test with a custom bar length
    test_list = list(range(5))
    result = list(dynamic_progress_logger(test_list, description='Custom', bar_length=20))
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check if the output contains expected progress indicators
    output = captured_output.getvalue()
    assert 'Custom: [' in output
    assert len(output.split('[')[1].split(']')[0]) <= 20
    
    # Verify the result is the same as the input list
    assert result == test_list