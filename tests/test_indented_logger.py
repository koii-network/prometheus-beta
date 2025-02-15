import io
import pytest
from src.indented_logger import IndentedLogger

def test_basic_logging():
    # Capture output to a string buffer
    output = io.StringIO()
    logger = IndentedLogger(file=output)
    
    # Log a message
    logger.log("Test message")
    
    # Check the output
    assert output.getvalue().strip() == "Test message"

def test_indentation():
    # Capture output to a string buffer
    output = io.StringIO()
    logger = IndentedLogger(file=output)
    
    # Increase indent and log
    logger.indent()
    logger.log("Indented message")
    
    # Check the output
    assert output.getvalue().strip() == "  Indented message"

def test_multiple_indentation():
    # Capture output to a string buffer
    output = io.StringIO()
    logger = IndentedLogger(file=output)
    
    # Multiple indents
    logger.indent()
    logger.indent()
    logger.log("Deeply indented message")
    
    # Check the output
    assert output.getvalue().strip() == "    Deeply indented message"

def test_dedent():
    # Capture output to a string buffer
    output = io.StringIO()
    logger = IndentedLogger(file=output)
    
    # Indent and dedent
    logger.indent()
    logger.indent()
    logger.dedent()
    logger.log("Single indent")
    
    # Check the output
    assert output.getvalue().strip() == "  Single indent"

def test_reset_indent():
    # Capture output to a string buffer
    output = io.StringIO()
    logger = IndentedLogger(file=output)
    
    # Indent, reset, and log
    logger.indent()
    logger.indent()
    logger.reset_indent()
    logger.log("Reset message")
    
    # Check the output
    assert output.getvalue().strip() == "Reset message"

def test_prevent_negative_indent():
    # Capture output to a string buffer
    output = io.StringIO()
    logger = IndentedLogger(file=output)
    
    # Try to dedent below zero
    logger.dedent()
    logger.log("No negative indent")
    
    # Check the output
    assert output.getvalue().strip() == "No negative indent"

def test_custom_indent_char():
    # Capture output to a string buffer
    output = io.StringIO()
    logger = IndentedLogger(indent_char='--', file=output)
    
    # Indent with custom character
    logger.indent()
    logger.log("Custom indent")
    
    # Check the output
    assert output.getvalue().strip() == "--Custom indent"