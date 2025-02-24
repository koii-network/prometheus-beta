import pytest
import logging
import io
import sys
from src.variable_type_logger import log_variable_type

def test_log_variable_type_int():
    """Test logging type for integer"""
    # Redirect logging output to capture
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Call function and check type
    result_type = log_variable_type(42)
    log_output = log_capture.getvalue().strip()
    
    assert result_type == int
    assert "Variable type is: <class 'int'>" in log_output

def test_log_variable_type_string():
    """Test logging type for string"""
    # Redirect logging output to capture
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Call function and check type
    result_type = log_variable_type("hello")
    log_output = log_capture.getvalue().strip()
    
    assert result_type == str
    assert "Variable type is: <class 'str'>" in log_output

def test_log_variable_type_list():
    """Test logging type for list"""
    # Redirect logging output to capture
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Call function and check type
    test_list = [1, 2, 3]
    result_type = log_variable_type(test_list)
    log_output = log_capture.getvalue().strip()
    
    assert result_type == list
    assert "Variable type is: <class 'list'>" in log_output

def test_log_variable_type_none():
    """Test logging type for None"""
    # Redirect logging output to capture
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Call function and check type
    result_type = log_variable_type(None)
    log_output = log_capture.getvalue().strip()
    
    assert result_type == type(None)
    assert "Variable type is: <class 'NoneType'>" in log_output

def test_log_variable_type_custom_class():
    """Test logging type for custom class"""
    class TestClass:
        pass
    
    # Redirect logging output to capture
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Call function and check type
    test_instance = TestClass()
    result_type = log_variable_type(test_instance)
    log_output = log_capture.getvalue().strip()
    
    assert result_type == TestClass
    assert "Variable type is: <class" in log_output