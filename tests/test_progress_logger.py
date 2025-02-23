import pytest
import io
import sys
from src.progress_logger import ProgressBar, log_with_progress

def test_progress_bar_initialization():
    """Test basic initialization of ProgressBar"""
    total = 100
    pb = ProgressBar(total)
    assert pb.total == total
    assert pb.current == 0

def test_progress_bar_update():
    """Test updating progress bar manually"""
    total = 10
    pb = ProgressBar(total)
    
    # Update to halfway
    pb.update(5)
    assert pb.current == 5

def test_progress_bar_increment():
    """Test automatic incrementation"""
    total = 5
    pb = ProgressBar(total)
    
    for _ in range(total):
        pb.update()
    
    assert pb.current == total

def test_progress_bar_iteration():
    """Test iteration protocol"""
    total = 5
    pb = ProgressBar(total)
    
    count = 0
    for _ in pb:
        count += 1
    
    assert count == total

def test_progress_bar_invalid_updates():
    """Test error handling for invalid updates"""
    total = 10
    pb = ProgressBar(total)
    
    # Test negative value
    with pytest.raises(ValueError, match="Current iteration cannot be negative"):
        pb.update(-1)
    
    # Test exceeding total
    with pytest.raises(ValueError, match=f"Current iteration cannot exceed total ({total})"):
        pb.update(total + 1)

def test_log_with_progress():
    """Test the log_with_progress wrapper"""
    test_list = list(range(10))
    
    for item in log_with_progress(test_list):
        pass  # Just iterate through

def test_progress_bar_output(capsys):
    """Test the output formatting of progress bar"""
    total = 5
    pb = ProgressBar(total)
    
    pb.update(3)
    captured = capsys.readouterr()
    assert '|███' in captured.out
    assert '60.0%' in captured.out