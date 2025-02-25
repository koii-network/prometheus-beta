import pytest
import sys
from io import StringIO
from src.log_formatter import log_with_size

def test_log_with_default_size(capsys):
    """Test logging with default medium size"""
    log_with_size("Test message")
    captured = capsys.readouterr()
    assert "Test message" in captured.out

def test_log_with_different_sizes(capsys):
    """Test logging with different sizes"""
    sizes = ['small', 'medium', 'large', 'xlarge']
    for size in sizes:
        log_with_size(f"Message in {size} size", size=size)
        captured = capsys.readouterr()
        assert f"Message in {size} size" in captured.out

def test_invalid_size():
    """Test that invalid size raises ValueError"""
    with pytest.raises(ValueError, match="Invalid size"):
        log_with_size("Test message", size="huge")

def test_log_with_unicode(capsys):
    """Test logging with unicode characters"""
    log_with_size("ããã«ã¡ã¯", size='large')
    captured = capsys.readouterr()
    assert "ããã«ã¡ã¯" in captured.out