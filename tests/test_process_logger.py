import pytest
import time
from src.process_logger import ProcessLogger

def test_process_logger_initialization():
    """Test basic initialization of ProcessLogger"""
    logger = ProcessLogger(total_steps=10)
    assert logger.total_steps == 10
    assert logger.current_step == 0

def test_process_logger_update():
    """Test updating progress steps"""
    log_messages = []
    def mock_log(message):
        log_messages.append(message)
    
    logger = ProcessLogger(total_steps=5, log_func=mock_log)
    
    # Update with specific step
    logger.update(current_step=3)
    assert logger.current_step == 3
    assert len(log_messages) == 1
    assert "60.00%" in log_messages[0]
    
    # Update incrementally
    logger.update()
    assert logger.current_step == 4
    assert len(log_messages) == 2

def test_process_logger_complete():
    """Test process completion"""
    log_messages = []
    def mock_log(message):
        log_messages.append(message)
    
    logger = ProcessLogger(total_steps=10, log_func=mock_log)
    logger.complete("All done!")
    
    assert len(log_messages) == 1
    assert "Process completed" in log_messages[0]
    assert "All done!" in log_messages[0]

def test_process_logger_custom_message():
    """Test logging with custom messages"""
    log_messages = []
    def mock_log(message):
        log_messages.append(message)
    
    logger = ProcessLogger(total_steps=5, log_func=mock_log)
    logger.update(current_step=2, message="Processing file")
    
    assert len(log_messages) == 1
    assert "40.00%" in log_messages[0]
    assert "Processing file" in log_messages[0]

def test_process_logger_no_total_steps():
    """Test progress logging without specifying total steps"""
    log_messages = []
    def mock_log(message):
        log_messages.append(message)
    
    logger = ProcessLogger(log_func=mock_log)
    logger.update()
    logger.update(message="Halfway there")
    logger.complete("No total steps")
    
    assert len(log_messages) == 3
    assert "Elapsed:" in log_messages[0]
    assert "Halfway there" in log_messages[1]
    assert "Process completed" in log_messages[2]