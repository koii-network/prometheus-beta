import os
import pytest
import logging
import readline
from unittest.mock import patch
from src.readline_logger import ReadlinePromptLogger

@pytest.fixture
def readline_logger():
    """Fixture to create a ReadlinePromptLogger instance."""
    test_log_file = 'logs/test_readline_prompts.log'
    return ReadlinePromptLogger(log_file=test_log_file)

def test_initialization(readline_logger):
    """Test logger initialization."""
    assert os.path.exists('logs')
    assert isinstance(readline_logger.logger, logging.Logger)
    assert readline_logger.log_file.endswith('test_readline_prompts.log')

@patch('builtins.input', return_value='test response')
def test_log_prompt(mock_input, readline_logger):
    """Test logging of prompts and responses."""
    # Clear existing log
    open(readline_logger.log_file, 'w').close()
    
    # Log a prompt
    response = readline_logger.log_prompt("Test prompt: ")
    
    # Check response
    assert response == 'test response'
    
    # Check log contents
    with open(readline_logger.log_file, 'r') as log_file:
        log_contents = log_file.read()
        assert "PROMPT: Test prompt: " in log_contents
        assert "RESPONSE: test response" in log_contents

def test_prompt_history(readline_logger):
    """Test retrieving prompt history."""
    # Reset readline history
    for _ in range(readline.get_current_history_length()):
        readline.remove_history_item(0)
    
    # Add some history
    readline.add_history("First input")
    readline.add_history("Second input")
    
    # Get history
    history = readline_logger.get_prompt_history()
    
    # Check history
    assert len(history) >= 2
    assert history[-2] == "First input"
    assert history[-1] == "Second input"

def test_history_limit(readline_logger):
    """Test retrieving limited history."""
    # Reset readline history
    for _ in range(readline.get_current_history_length()):
        readline.remove_history_item(0)
    
    # Add multiple history entries
    for i in range(5):
        readline.add_history(f"Input {i}")
    
    # Get limited history
    limited_history = readline_logger.get_prompt_history(limit=3)
    
    # Check limited history
    assert len(limited_history) == 3
    assert limited_history == ["Input 2", "Input 3", "Input 4"]

def test_clear_log(readline_logger):
    """Test clearing the log file."""
    # Write some content to log
    readline_logger.logger.info("Test log content")
    
    # Clear log
    readline_logger.clear_log()
    
    # Check log file is empty
    with open(readline_logger.log_file, 'r') as log_file:
        assert len(log_file.read().strip()) == 0