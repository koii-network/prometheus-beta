import pytest
import logging
import io
import sys
from unittest.mock import patch
from src.readline_logger import log_interactive_prompt

def test_log_interactive_prompt_basic():
    # Simulate user input
    with patch('builtins.input', return_value='test input'):
        # Capture logging
        log_capture = io.StringIO()
        handler = logging.StreamHandler(log_capture)
        logger = logging.getLogger()
        logger.addHandler(handler)
        
        result = log_interactive_prompt("Test prompt: ")
        
        assert result == 'test input'
        log_output = log_capture.getvalue()
        assert "Prompt: Test prompt: " in log_output
        assert "User input received: test input" in log_output

def test_log_interactive_prompt_with_validator():
    # Validator that only accepts 'valid' input
    def validator(x):
        return x == 'valid'
    
    # Simulate multiple inputs with a final valid input
    inputs = iter(['invalid', 'also invalid', 'valid'])
    with patch('builtins.input', side_effect=inputs):
        log_capture = io.StringIO()
        handler = logging.StreamHandler(log_capture)
        logger = logging.getLogger()
        logger.addHandler(handler)
        
        result = log_interactive_prompt("Validation prompt: ", validator=validator)
        
        assert result == 'valid'
        log_output = log_capture.getvalue()
        assert "Input validation failed: invalid" in log_output
        assert "Input validation failed: also invalid" in log_output

def test_log_interactive_prompt_custom_logger():
    # Create a custom logger
    custom_logger = logging.getLogger('custom')
    custom_logger.setLevel(logging.DEBUG)
    
    # Capture custom logger output
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    custom_logger.addHandler(handler)
    
    # Simulate user input
    with patch('builtins.input', return_value='custom input'):
        result = log_interactive_prompt("Custom logger prompt: ", 
                                         log_level=logging.DEBUG, 
                                         logger=custom_logger)
        
        assert result == 'custom input'
        log_output = log_capture.getvalue()
        assert "Prompt: Custom logger prompt: " in log_output
        assert "User input received: custom input" in log_output

def test_log_interactive_prompt_keyboard_interrupt():
    # Simulate keyboard interrupt
    with patch('builtins.input', side_effect=KeyboardInterrupt):
        with pytest.raises(KeyboardInterrupt):
            log_interactive_prompt("Interrupt prompt: ")