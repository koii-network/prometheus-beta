import os
import platform
import pytest
from unittest.mock import patch
import sys
import io

from src.console_utils import clear_console_and_log

def test_clear_console_and_log_windows():
    with patch('platform.system', return_value='Windows'):
        with patch('os.system') as mock_os_system:
            with patch('builtins.print') as mock_print:
                clear_console_and_log("Test message")
                mock_os_system.assert_called_once_with('cls')
                mock_print.assert_called_once_with("Test message")

def test_clear_console_and_log_unix():
    with patch('platform.system', return_value='Linux'):
        with patch('os.system') as mock_os_system:
            with patch('builtins.print') as mock_print:
                clear_console_and_log("Test message")
                mock_os_system.assert_called_once_with('clear')
                mock_print.assert_called_once_with("Test message")

def test_clear_console_and_log_output():
    # Capture stdout to verify message logging
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    clear_console_and_log("Hello, World!")
    
    # Reset redirect
    sys.stdout = sys.__stdout__
    
    assert captured_output.getvalue().strip() == "Hello, World!"

def test_clear_console_and_log_empty_message():
    # Test with an empty message
    with patch('os.system'):
        clear_console_and_log("")  # Should not raise any errors