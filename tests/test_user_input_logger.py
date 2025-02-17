import os
import pytest
import logging
from unittest.mock import patch
from src.user_input_logger import log_user_input

def test_log_user_input_success():
    # Test successful input logging
    with patch('builtins.input', return_value='test input'):
        result = log_user_input()
        assert result == 'test input'
        
        # Check if log file was created
        assert os.path.exists('user_input.log')
        
        # Check log file content
        with open('user_input.log', 'r') as log_file:
            log_content = log_file.read()
            assert 'User Input: test input' in log_content

def test_log_user_input_empty():
    # Test logging of empty input
    with patch('builtins.input', return_value=''):
        result = log_user_input()
        assert result == ''
        
        # Check log file content for empty input
        with open('user_input.log', 'r') as log_file:
            log_content = log_file.read()
            assert 'User Input: ' in log_content

def test_log_user_input_special_characters():
    # Test logging of input with special characters
    with patch('builtins.input', return_value='Hello, World! @#$%'):
        result = log_user_input()
        assert result == 'Hello, World! @#$%'
        
        # Check log file content
        with open('user_input.log', 'r') as log_file:
            log_content = log_file.read()
            assert 'User Input: Hello, World! @#$%' in log_content