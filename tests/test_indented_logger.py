"""
Unit tests for the IndentedLogger class.
"""

import pytest
from src.indented_logger import IndentedLogger

def test_initial_indent_level():
    """Test that the initial indent level is 0."""
    logger = IndentedLogger()
    assert logger.get_current_indent_level() == 0

def test_basic_logging():
    """Test basic logging without indentation."""
    logger = IndentedLogger()
    assert logger.log("Test message") == "Test message"

def test_indent():
    """Test increasing indentation."""
    logger = IndentedLogger()
    logger.indent()
    assert logger.get_current_indent_level() == 1
    assert logger.log("Indented message") == "    Indented message"

def test_multiple_indents():
    """Test multiple indentation levels."""
    logger = IndentedLogger()
    logger.indent()
    logger.indent()
    assert logger.get_current_indent_level() == 2
    assert logger.log("Deeply indented message") == "        Deeply indented message"

def test_dedent():
    """Test decreasing indentation."""
    logger = IndentedLogger()
    logger.indent()
    logger.indent()
    logger.dedent()
    assert logger.get_current_indent_level() == 1
    assert logger.log("Back to one indent") == "    Back to one indent"

def test_reset_indent():
    """Test resetting indentation to 0."""
    logger = IndentedLogger()
    logger.indent()
    logger.indent()
    logger.reset_indent()
    assert logger.get_current_indent_level() == 0
    assert logger.log("Reset message") == "Reset message"

def test_dedent_error():
    """Test that dedenting below 0 raises an error."""
    logger = IndentedLogger()
    with pytest.raises(ValueError, match="Cannot dedent below 0"):
        logger.dedent()

def test_custom_indent():
    """Test custom indent size and character."""
    logger = IndentedLogger(indent_size=2, indent_char='-')
    logger.indent()
    assert logger.log("Custom indent") == "--Custom indent"

def test_invalid_indent_size():
    """Test that negative indent size raises an error."""
    with pytest.raises(ValueError, match="Indent size must be non-negative"):
        IndentedLogger(indent_size=-1)

def test_invalid_indent_char():
    """Test that empty indent char raises an error."""
    with pytest.raises(ValueError, match="Indent character cannot be empty"):
        IndentedLogger(indent_char="")