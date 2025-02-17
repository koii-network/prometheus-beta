import io
import sys
from src.indented_logger import IndentedLogger

def test_initial_logging():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    logger = IndentedLogger()
    result = logger.log("Hello, world!")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result == "Hello, world!"
    assert captured_output.getvalue().strip() == "Hello, world!"

def test_indentation():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    logger = IndentedLogger()
    logger.indent()
    result = logger.log("Indented message")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result == "  Indented message"
    assert captured_output.getvalue().strip() == "  Indented message"

def test_multiple_indents():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    logger = IndentedLogger()
    logger.indent()
    logger.indent()
    result = logger.log("Deeply indented")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result == "    Deeply indented"
    assert captured_output.getvalue().strip() == "    Deeply indented"

def test_dedent():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    logger = IndentedLogger()
    logger.indent()
    logger.indent()
    logger.dedent()
    result = logger.log("Back to one indent")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result == "  Back to one indent"
    assert captured_output.getvalue().strip() == "  Back to one indent"

def test_prevent_negative_indent():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    logger = IndentedLogger()
    logger.dedent()  # Should not go below 0
    result = logger.log("No negative indent")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result == "No negative indent"
    assert captured_output.getvalue().strip() == "No negative indent"

def test_reset_indent():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    logger = IndentedLogger()
    logger.indent()
    logger.indent()
    logger.reset_indent()
    result = logger.log("Reset to zero")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result == "Reset to zero"
    assert captured_output.getvalue().strip() == "Reset to zero"

def test_custom_indent_step():
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    logger = IndentedLogger(indent_step=4)
    logger.indent()
    result = logger.log("Four-space indent")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    assert result == "    Four-space indent"
    assert captured_output.getvalue().strip() == "    Four-space indent"