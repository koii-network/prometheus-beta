import pytest
from src.indented_logger import log_with_indent

def test_default_indentation(capsys):
    """Test default indentation with print function."""
    result = log_with_indent("Hello, World!")
    captured = capsys.readouterr()
    assert result == "Hello, World!"
    assert captured.out.strip() == "Hello, World!"

def test_custom_indent_level(capsys):
    """Test custom indentation levels."""
    result = log_with_indent("Nested message", indent_level=2)
    captured = capsys.readouterr()
    assert result == "        Nested message"
    assert captured.out.strip() == "        Nested message"

def test_custom_indent_char(capsys):
    """Test custom indentation character."""
    result = log_with_indent("Tabbed message", indent_level=1, indent_char='\t')
    captured = capsys.readouterr()
    assert result == "\tTabbed message"
    assert captured.out.strip() == "\tTabbed message"

def test_custom_log_func():
    """Test custom logging function."""
    log_messages = []
    def custom_log(msg):
        log_messages.append(msg)
    
    result = log_with_indent("Custom log", indent_level=1, log_func=custom_log)
    assert result == "    Custom log"
    assert log_messages == ["    Custom log"]

def test_invalid_indent_level():
    """Test invalid indent level raises ValueError."""
    with pytest.raises(ValueError, match="Indent level must be an integer"):
        log_with_indent("Message", indent_level="not an int")

def test_invalid_indent_char():
    """Test invalid indent character raises ValueError."""
    with pytest.raises(ValueError, match="Indent character must be a single character"):
        log_with_indent("Message", indent_char="  ")