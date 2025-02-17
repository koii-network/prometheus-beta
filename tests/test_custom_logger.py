import pytest
import colorama
from src.custom_logger import log_with_style

def test_log_with_style_default():
    """Test default logging without style"""
    result = log_with_style("Test message")
    assert "Test message" in result
    assert colorama.Fore.WHITE in result

def test_log_with_style_success():
    """Test success style logging"""
    result = log_with_style("Success message", style='success')
    assert "Success message" in result
    assert "[SUCCESS]" in result
    assert colorama.Fore.GREEN in result

def test_log_with_style_warning():
    """Test warning style logging"""
    result = log_with_style("Warning message", style='warning')
    assert "Warning message" in result
    assert "[WARNING]" in result
    assert colorama.Fore.YELLOW in result

def test_log_with_style_error():
    """Test error style logging"""
    result = log_with_style("Error message", style='error')
    assert "Error message" in result
    assert "[ERROR]" in result
    assert colorama.Fore.RED in result

def test_log_with_style_info():
    """Test info style logging"""
    result = log_with_style("Info message", style='info')
    assert "Info message" in result
    assert "[INFO]" in result
    assert colorama.Fore.BLUE in result

def test_log_with_custom_prefix():
    """Test logging with a custom prefix"""
    result = log_with_style("Custom prefix message", prefix="CUSTOM")
    assert "Custom prefix message" in result
    assert "[CUSTOM]" in result

def test_invalid_style():
    """Test that an invalid style defaults to white"""
    result = log_with_style("Invalid style", style='invalid')
    assert "Invalid style" in result
    assert colorama.Fore.WHITE in result