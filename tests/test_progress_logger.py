import pytest
import time
import sys
from io import StringIO
from src.progress_logger import ProgressLogger

def test_progress_logger_initialization():
    """Test initialization of ProgressLogger"""
    logger = ProgressLogger(total_steps=10)
    assert logger.total_steps == 10
    assert logger.prefix == 'Progress'
    assert logger.suffix == 'Complete'

def test_progress_logger_without_total_steps():
    """Test behavior when no total steps are provided"""
    logger = ProgressLogger()
    assert logger.total_steps is None

def test_progress_bar_output(capsys):
    """Test progress bar output"""
    # Capture stdout
    logger = ProgressLogger(total_steps=5)
    
    # Simulate progress
    for i in range(6):
        logger.print_progress_bar(i)
    
    # Capture the output
    captured = capsys.readouterr()
    output = captured.out
    
    # Check if output contains expected elements
    assert 'Progress |' in output
    assert '%' in output
    assert 'Complete' in output

def test_track_progress():
    """Test tracking progress of a simple process"""
    def dummy_process(iterations):
        time.sleep(0.1)  # Simulate some work
        return iterations * 2
    
    logger = ProgressLogger(total_steps=3)
    result = logger.track_progress(dummy_process, 3)
    
    assert result == 6

def test_progress_bar_additional_info(capsys):
    """Test progress bar with additional information"""
    logger = ProgressLogger(total_steps=5)
    
    # Simulate progress with additional info
    for i in range(6):
        logger.print_progress_bar(i, additional_info="Processing...")
    
    # Capture the output
    captured = capsys.readouterr()
    output = captured.out
    
    # Check if output contains additional info
    assert 'Processing...' in output

def test_edge_cases():
    """Test edge cases for progress logging"""
    # Test with zero total steps
    logger = ProgressLogger(total_steps=0)
    logger.print_progress_bar(0)  # Should not raise an error
    
    # Test with None total steps
    logger_no_steps = ProgressLogger()
    result = logger_no_steps.track_progress(lambda x: x, 5)
    assert result == 5