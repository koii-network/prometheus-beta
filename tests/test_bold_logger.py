import io
import sys
from src.bold_logger import log_bold

def test_log_bold(capsys):
    """Test that the log_bold function prints message in bold."""
    log_bold("Test Message")
    captured = capsys.readouterr()
    
    # Check if the message is wrapped with bold ANSI escape codes
    assert captured.out.strip() == "\033[1mTest Message\033[0m"

def test_log_bold_empty_string(capsys):
    """Test logging an empty string."""
    log_bold("")
    captured = capsys.readouterr()
    
    # Check that an empty string still has bold formatting
    assert captured.out.strip() == "\033[1m\033[0m"

def test_log_bold_with_special_characters(capsys):
    """Test logging a message with special characters."""
    log_bold("Hello, World! @#$%^&*()")
    captured = capsys.readouterr()
    
    # Check if special characters are preserved in bold
    assert captured.out.strip() == "\033[1mHello, World! @#$%^&*()\033[0m"