import os
import pytest
import tempfile
from src.remove_empty_lines import remove_empty_lines

def test_remove_empty_lines_basic():
    """Test removing empty lines from a file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Line 1\n\n\nLine 2\n\nLine 3\n")
        temp_file.close()

        remove_empty_lines(temp_file.name)

        with open(temp_file.name, 'r') as f:
            lines = f.readlines()

        assert lines == ["Line 1\n", "Line 2\n", "Line 3\n"]
        os.unlink(temp_file.name)

def test_remove_empty_lines_only_whitespace():
    """Test removing lines with only whitespace."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Line 1\n   \n\t\n Line 2\n")
        temp_file.close()

        remove_empty_lines(temp_file.name)

        with open(temp_file.name, 'r') as f:
            lines = f.readlines()

        assert lines == ["Line 1\n", " Line 2\n"]
        os.unlink(temp_file.name)

def test_remove_empty_lines_empty_file():
    """Test behavior with an empty file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("")
        temp_file.close()

        remove_empty_lines(temp_file.name)

        with open(temp_file.name, 'r') as f:
            lines = f.readlines()

        assert lines == []
        os.unlink(temp_file.name)

def test_remove_empty_lines_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        remove_empty_lines(123)
    with pytest.raises(TypeError):
        remove_empty_lines(None)

def test_remove_empty_lines_file_not_found():
    """Test error handling for non-existent file."""
    with pytest.raises(FileNotFoundError):
        remove_empty_lines("/path/to/non/existent/file.txt")

def test_remove_empty_lines_preserves_existing_content():
    """Test that non-empty lines are preserved."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("  Hello  \n\nWorld\n\n  Python  \n")
        temp_file.close()

        remove_empty_lines(temp_file.name)

        with open(temp_file.name, 'r') as f:
            lines = f.readlines()

        assert lines == ["  Hello  \n", "World\n", "  Python  \n"]
        os.unlink(temp_file.name)