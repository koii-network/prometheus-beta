import sys
import io
import pytest
from src.dynamic_progress_logger import log_with_progress_bar

def test_progress_bar_basic_functionality(capsys):
    # Capture stdout
    progress_updater = log_with_progress_bar(total_steps=10)
    
    # Simulate progress
    for i in range(11):
        progress_updater(i)
    
    # Capture the output
    captured = capsys.readouterr()
    output = captured.out
    
    # Verify key components of the output
    assert 'Processing: ' in output
    assert '[' in output and ']' in output
    assert '100.0%' in output
    assert '10/10 steps' in output

def test_progress_bar_edge_cases():
    # Test with zero steps
    progress_updater_zero = log_with_progress_bar(total_steps=0)
    progress_updater_zero(0)  # Should not raise an error
    
    # Test with very large number of steps
    progress_updater_large = log_with_progress_bar(total_steps=1000000)
    progress_updater_large(1000000)  # Should handle large numbers

def test_progress_bar_custom_prefix():
    # Test with custom prefix
    progress_updater = log_with_progress_bar(total_steps=5, message_prefix="Custom Task")
    
    # Simulate progress
    for i in range(6):
        progress_updater(i)

def test_input_validation():
    # Test negative steps
    with pytest.raises(Exception):
        progress_updater = log_with_progress_bar(total_steps=-1)
    
    # Test non-integer steps
    with pytest.raises(Exception):
        progress_updater = log_with_progress_bar(total_steps=1.5)