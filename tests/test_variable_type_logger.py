import pytest
import logging
import io
import sys
from src.variable_type_logger import log_variable_type

def test_log_variable_type_primitives():
    # Capture logging output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Test various primitive types
    assert log_variable_type(42) == 'int'
    assert 'int' in log_capture.getvalue()
    assert '42' in log_capture.getvalue()
    
    log_capture.truncate(0)
    log_capture.seek(0)
    
    assert log_variable_type("hello") == 'str'
    assert 'str' in log_capture.getvalue()
    assert "'hello'" in log_capture.getvalue()
    
    log_capture.truncate(0)
    log_capture.seek(0)
    
    assert log_variable_type(3.14) == 'float'
    assert 'float' in log_capture.getvalue()
    assert '3.14' in log_capture.getvalue()

def test_log_variable_type_complex():
    # Capture logging output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Test list
    test_list = [1, 2, 3]
    assert log_variable_type(test_list) == 'list'
    assert 'list' in log_capture.getvalue()
    assert str(test_list) in log_capture.getvalue()
    
    log_capture.truncate(0)
    log_capture.seek(0)
    
    # Test dictionary
    test_dict = {'a': 1, 'b': 2}
    assert log_variable_type(test_dict) == 'dict'
    assert 'dict' in log_capture.getvalue()
    assert str(test_dict) in log_capture.getvalue()

def test_log_variable_type_custom_class():
    # Capture logging output
    log_capture = io.StringIO()
    logging.basicConfig(stream=log_capture, level=logging.INFO)
    
    # Test custom class
    class TestClass:
        pass
    
    test_obj = TestClass()
    assert log_variable_type(test_obj) == 'TestClass'
    assert 'TestClass' in log_capture.getvalue()
    assert str(test_obj) in log_capture.getvalue()