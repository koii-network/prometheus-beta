import os
import pytest
import tempfile
from src.keystroke_logger import KeystrokeLogger

@pytest.fixture
def logger():
    """Create a fresh logger for each test"""
    # Use a unique log file for each test to avoid conflicts
    log_file = f'test_keystroke_log_{pytest.unique_id}.txt'
    return KeystrokeLogger(log_file)

def setup_module(module):
    """Generate a unique id for log files"""
    pytest.unique_id = os.getpid()

def test_log_single_keystroke(logger):
    """Test logging a single keystroke"""
    logger.log_keystroke('a')
    log_contents = logger.get_log_contents()
    assert len(log_contents) > 0
    assert 'Keystroke: a' in log_contents[-1]

def test_log_multiple_keystrokes(logger):
    """Test logging multiple keystrokes"""
    keystrokes = ['h', 'e', 'l', 'l', 'o']
    for key in keystrokes:
        logger.log_keystroke(key)
    
    log_contents = logger.get_log_contents()
    assert len(log_contents) >= len(keystrokes)

def test_invalid_keystroke_type(logger):
    """Test that logging non-string keystrokes raises a TypeError"""
    with pytest.raises(TypeError):
        logger.log_keystroke(123)
    with pytest.raises(TypeError):
        logger.log_keystroke(None)

def test_log_file_creation(logger):
    """Test that the log file is created"""
    logger.log_keystroke('x')
    assert os.path.exists(os.path.join('logs', logger.log_file.split('/')[-1]))

def test_empty_log():
    """Test retrieving contents of an empty log"""
    # Create a completely new logger with a fresh log file
    log_file = f'empty_test_log_{os.getpid()}.txt'
    logger = KeystrokeLogger(log_file)
    
    log_contents = logger.get_log_contents()
    assert isinstance(log_contents, list)
    assert len(log_contents) == 0