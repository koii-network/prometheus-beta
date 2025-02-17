import pytest
import sys
from io import StringIO
from src.indented_logger import IndentedLogger

def test_basic_logging():
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    logger = IndentedLogger()
    result = logger.log("Hello, World!")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result == "Hello, World!"
    assert captured_output.getvalue().strip() == "Hello, World!"

def test_indentation():
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    logger = IndentedLogger()
    logger.indent(1)
    result = logger.log("Indented message")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result == "  Indented message"
    assert captured_output.getvalue().strip() == "  Indented message"

def test_multiple_indentations():
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    logger = IndentedLogger()
    logger.indent(2)
    result = logger.log("Deeply indented")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result == "    Deeply indented"
    assert captured_output.getvalue().strip() == "    Deeply indented"

def test_dedent():
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    logger = IndentedLogger()
    logger.indent(3)
    logger.dedent(1)
    result = logger.log("Semi-indented")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result == "    Semi-indented"
    assert captured_output.getvalue().strip() == "    Semi-indented"

def test_reset_indent():
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    logger = IndentedLogger()
    logger.indent(5)
    logger.reset_indent()
    result = logger.log("Back to base")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result == "Back to base"
    assert captured_output.getvalue().strip() == "Back to base"

def test_custom_indent_step():
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    logger = IndentedLogger(indent_step=4)
    logger.indent(1)
    result = logger.log("Wider indentation")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result == "    Wider indentation"
    assert captured_output.getvalue().strip() == "    Wider indentation"

def test_non_string_input():
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    logger = IndentedLogger()
    result = logger.log(42)
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result == "42"
    assert captured_output.getvalue().strip() == "42"