import pytest
import sys
from io import StringIO
from src.indented_logger import IndentedLogger

def capture_log(func):
    """Decorator to capture logger's stdout."""
    def wrapper(*args, **kwargs):
        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            result = func(*args, **kwargs)
            return result, captured_output.getvalue().strip()
        finally:
            sys.stdout = sys.__stdout__
    return wrapper

def test_basic_logging():
    logger = IndentedLogger()
    result, output = capture_log(logger.log)("Hello, World!")
    assert result == "Hello, World!"
    assert output == "Hello, World!"

def test_indentation():
    logger = IndentedLogger()
    logger.indent(1)
    result, output = capture_log(logger.log)("Indented message")
    assert result == "  Indented message"
    assert output == "  Indented message"

def test_multiple_indentations():
    logger = IndentedLogger()
    logger.indent(2)
    result, output = capture_log(logger.log)("Deeply indented")
    assert result == "    Deeply indented"
    assert output == "    Deeply indented"

def test_dedent():
    logger = IndentedLogger()
    logger.indent(3)
    logger.dedent(1)
    result, output = capture_log(logger.log)("Semi-indented")
    assert result == "    Semi-indented"
    assert output == "    Semi-indented"

def test_reset_indent():
    logger = IndentedLogger()
    logger.indent(5)
    logger.reset_indent()
    result, output = capture_log(logger.log)("Back to base")
    assert result == "Back to base"
    assert output == "Back to base"

def test_custom_indent_step():
    logger = IndentedLogger(indent_step=4)
    logger.indent(1)
    result, output = capture_log(logger.log)("Wider indentation")
    assert result == "    Wider indentation"
    assert output == "    Wider indentation"

def test_non_string_input():
    logger = IndentedLogger()
    result, output = capture_log(logger.log)(42)
    assert result == "42"
    assert output == "42"