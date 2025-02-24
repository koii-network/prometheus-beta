"""
Tests for the IndentedLogger class.
"""

import pytest
from src.indented_logger import IndentedLogger

def test_default_initialization():
    """Test default logger initialization."""
    logger = IndentedLogger()
    assert logger.get_indent_level() == 0

def test_custom_indent_initialization():
    """Test custom indent character and size initialization."""
    logger = IndentedLogger(indent_char='-', indent_size=2)
    logger.indent(2)
    assert logger.log("test") == "----test"

def test_log_none_message():
    """Test logging None message."""
    logger = IndentedLogger()
    assert logger.log(None) == ''

def test_log_with_indentation():
    """Test logging messages with different indentation levels."""
    logger = IndentedLogger()
    assert logger.log("Hello") == "Hello"
    
    logger.indent()
    assert logger.log("World") == "    World"
    
    logger.indent(2)
    assert logger.log("Nested") == "        Nested"

def test_indent_and_dedent():
    """Test indentation and de-indentation."""
    logger = IndentedLogger()
    logger.indent(3)
    assert logger.get_indent_level() == 3
    
    logger.dedent(2)
    assert logger.get_indent_level() == 1
    
    logger.dedent(5)  # Should not go below 0
    assert logger.get_indent_level() == 0

def test_invalid_initialization_raises_error():
    """Test invalid initialization raises ValueError."""
    with pytest.raises(ValueError):
        IndentedLogger(indent_size=-1)

def test_invalid_indent_raises_error():
    """Test negative indent raises ValueError."""
    logger = IndentedLogger()
    with pytest.raises(ValueError):
        logger.indent(-1)

def test_invalid_dedent_raises_error():
    """Test negative dedent raises ValueError."""
    logger = IndentedLogger()
    with pytest.raises(ValueError):
        logger.dedent(-1)

def test_multiple_indent_dedent():
    """Test multiple indent and dedent operations."""
    logger = IndentedLogger()
    
    logger.indent(3)
    assert logger.log("Deep") == "            Deep"
    
    logger.dedent(2)
    assert logger.log("Less Deep") == "    Less Deep"
    
    logger.dedent(5)
    assert logger.log("Top Level") == "Top Level"