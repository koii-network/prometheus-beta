import pytest
import logging
import time
from src.process_progress_logger import ProcessProgressLogger

class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(message)
    
    def setLevel(self, level):
        pass

def test_progress_logger_basic_flow():
    mock_logger = MockLogger()
    logger = ProcessProgressLogger(logger=mock_logger)
    
    # Start tracking
    logger.start(total_steps=10)
    
    # Update progress
    progress = logger.update(3)
    assert progress == 30.0
    assert "3/10 steps (30.00%)" in mock_logger.logs[-1]
    
    # Complete process
    logger.complete()
    assert "Process completed" in mock_logger.logs[-1]

def test_progress_logger_invalid_inputs():
    mock_logger = MockLogger()
    logger = ProcessProgressLogger(logger=mock_logger)
    
    # Test invalid total steps
    with pytest.raises(ValueError, match="Total steps must be a positive integer"):
        logger.start(total_steps=0)
    
    # Test updating before starting
    with pytest.raises(RuntimeError, match="Progress tracking not started"):
        logger.update()
    
    # Test completing before starting
    with pytest.raises(RuntimeError, match="Progress tracking not started"):
        logger.complete()

def test_progress_logger_step_validation():
    mock_logger = MockLogger()
    logger = ProcessProgressLogger(logger=mock_logger)
    
    logger.start(total_steps=5)
    
    # Normal update
    progress = logger.update(2)
    assert progress == 40.0
    
    # Update that would exceed total steps
    with pytest.raises(ValueError, match="Cannot exceed total steps"):
        logger.update(4)

def test_progress_logger_auto_complete():
    mock_logger = MockLogger()
    logger = ProcessProgressLogger(logger=mock_logger)
    
    logger.start(total_steps=5)
    logger.update(3)
    
    # Calling complete when not fully progressed
    logger.complete()
    
    # Verify logging
    assert "Process completed" in mock_logger.logs[-1]
    assert "Total steps: 5" in mock_logger.logs[-1]

def test_progress_logger_logging_levels():
    # Test custom logging level
    logger = ProcessProgressLogger(log_level=logging.DEBUG)
    assert logger.logger.level == logging.DEBUG