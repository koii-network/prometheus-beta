import os
import pytest
import logging
from src.debug_logger import conditional_debug_log

def test_debug_log_with_explicit_true():
    """Test logging when debug_mode is explicitly set to True"""
    # Use a capture handler to check logging
    log_capture = logging.StreamHandler()
    logging.getLogger().addHandler(log_capture)
    log_capture.setLevel(logging.DEBUG)
    
    # Capture log output
    with pytest.LogCapture() as caplog:
        result = conditional_debug_log("Test explicit debug", debug_mode=True)
        
    assert result == True
    assert "Test explicit debug" in str(caplog.text)

def test_debug_log_with_explicit_false():
    """Test no logging when debug_mode is explicitly set to False"""
    with pytest.LogCapture() as caplog:
        result = conditional_debug_log("Test explicit no debug", debug_mode=False)
        
    assert result == False
    assert "Test explicit no debug" not in str(caplog.text)

def test_debug_log_with_env_variable(monkeypatch):
    """Test logging controlled by DEBUG environment variable"""
    # Set DEBUG environment variable
    monkeypatch.setenv('DEBUG', '1')
    
    with pytest.LogCapture() as caplog:
        result = conditional_debug_log("Test env debug")
        
    assert result == True
    assert "Test env debug" in str(caplog.text)

def test_debug_log_without_env_variable(monkeypatch):
    """Test no logging when DEBUG environment variable is not set"""
    # Unset DEBUG environment variable
    monkeypatch.delenv('DEBUG', raising=False)
    
    with pytest.LogCapture() as caplog:
        result = conditional_debug_log("Test no env debug")
        
    assert result == False
    assert "Test no env debug" not in str(caplog.text)

def test_debug_log_various_env_true_values(monkeypatch):
    """Test various truthy environment variable values"""
    true_values = ['1', 'true', 'TRUE', 'True', 'yes', 'YES']
    
    for val in true_values:
        monkeypatch.setenv('DEBUG', val)
        
        with pytest.LogCapture() as caplog:
            result = conditional_debug_log(f"Test debug with {val}")
            
        assert result == True
        assert f"Test debug with {val}" in str(caplog.text)