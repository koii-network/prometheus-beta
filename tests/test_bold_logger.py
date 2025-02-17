import io
import sys
from src.bold_logger import log_bold

def test_log_bold(capsys):
    """Test that the log_bold function prints a message in bold."""
    log_bold("Test message")
    captured = capsys.readouterr()
    
    # Check that the output contains ANSI bold start and end codes
    assert captured.out.startswith("\033[1m")
    assert captured.out.endswith("\033[0m\n")
    assert "Test message" in captured.out

def test_log_bold_empty_string(capsys):
    """Test logging an empty string."""
    log_bold("")
    captured = capsys.readouterr()
    
    # Check that the output has bold codes even for an empty string
    assert captured.out.startswith("\033[1m")
    assert captured.out.endswith("\033[0m\n")
    assert captured.out.strip() == "\033[1m\033[0m"

def test_log_bold_with_special_characters(capsys):
    """Test logging a message with special characters."""
    log_bold("Hello, World! @#$%^&*()")
    captured = capsys.readouterr()
    
    assert captured.out.startswith("\033[1m")
    assert captured.out.endswith("\033[0m\n")
    assert "Hello, World! @#$%^&*()" in captured.out