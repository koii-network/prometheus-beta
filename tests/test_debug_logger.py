import os
import sys
import io
import pytest
from src.debug_logger import conditional_debug_log

def test_debug_logging_enabled():
    """Test that debug logging works when debug is enabled"""
    # Capture stderr
    old_stderr = sys.stderr
    captured_output = io.StringIO()
    sys.stderr = captured_output

    try:
        # Set debug environment variable
        os.environ['DEBUG'] = '1'

        # Log a test message
        result = conditional_debug_log("Test debug message")
        
        # Get captured output
        output = captured_output.getvalue()

        # Assertions
        assert result is True
        assert "Test debug message" in output
    finally:
        # Restore stderr
        sys.stderr = old_stderr

def test_debug_logging_disabled():
    """Test that no logging occurs when debug is disabled"""
    # Capture stderr
    old_stderr = sys.stderr
    captured_output = io.StringIO()
    sys.stderr = captured_output

    try:
        # Unset or set to false debug environment variable
        os.environ['DEBUG'] = '0'

        # Log a test message
        result = conditional_debug_log("Test debug message")
        
        # Get captured output
        output = captured_output.getvalue()

        # Assertions
        assert result is False
        assert "Test debug message" not in output
    finally:
        # Restore stderr
        sys.stderr = old_stderr

def test_custom_env_var():
    """Test logging with a custom environment variable"""
    # Capture stderr
    old_stderr = sys.stderr
    captured_output = io.StringIO()
    sys.stderr = captured_output

    try:
        # Set a custom debug environment variable
        os.environ['CUSTOM_DEBUG'] = '1'

        # Log a test message with custom env var
        result = conditional_debug_log("Custom debug message", debug_env_var='CUSTOM_DEBUG')
        
        # Get captured output
        output = captured_output.getvalue()

        # Assertions
        assert result is True
        assert "Custom debug message" in output
    finally:
        # Restore stderr
        sys.stderr = old_stderr

def test_multiple_debug_values():
    """Test multiple debug environment values"""
    # Each tuple is (debug_value, expected_result)
    test_cases = [
        ('1', True),
        ('true', True),
        ('yes', True),
        ('0', False),
        ('false', False),
        ('', False)
    ]

    for debug_value, expected_result in test_cases:
        # Capture stderr
        old_stderr = sys.stderr
        captured_output = io.StringIO()
        sys.stderr = captured_output

        try:
            # Set debug environment variable
            os.environ['DEBUG'] = debug_value

            # Attempt to log
            result = conditional_debug_log(f"Debug test: {debug_value}")
            
            # Get captured output
            output = captured_output.getvalue()

            # Assertions
            assert result is expected_result, f"Failed for debug_value: {debug_value}"
            
            if expected_result:
                assert f"Debug test: {debug_value}" in output
        finally:
            # Restore stderr
            sys.stderr = old_stderr