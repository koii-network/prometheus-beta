import os
import logging
import pytest
from src.keystroke_logger import log_keystrokes

def test_log_keystrokes_single_character(tmp_path):
    # Temporarily change logging directory to a temp path
    original_log_dir = 'logs'
    os.makedirs(tmp_path / 'logs', exist_ok=True)
    os.chdir(tmp_path)
    
    # Test logging a single character
    result = log_keystrokes('a')
    assert result is True
    
    # Check log file is created
    log_file = os.path.join('logs', f'keystrokes_{os.date.today().isoformat()}.log')
    assert os.path.exists(log_file)
    
    # Reset logging directory
    os.chdir(original_log_dir)

def test_log_keystrokes_invalid_input():
    # Test invalid inputs
    with pytest.raises(ValueError):
        log_keystrokes('')  # Empty string
    
    with pytest.raises(ValueError):
        log_keystrokes('ab')  # Multiple characters
    
    with pytest.raises(ValueError):
        log_keystrokes(123)  # Non-string input

def test_log_keystrokes_special_characters():
    # Test logging special characters
    special_chars = ['!', '@', '#', '$', '%']
    for char in special_chars:
        result = log_keystrokes(char)
        assert result is True