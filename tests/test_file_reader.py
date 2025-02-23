import os
import pytest
import tempfile

from src.file_reader import read_file_line_by_line

def test_read_file_line_by_line_normal_case():
    """Test reading a normal text file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello\nWorld\nPython")
        temp_file.close()
        
        try:
            lines = read_file_line_by_line(temp_file.name)
            assert lines == ["Hello", "World", "Python"]
        finally:
            os.unlink(temp_file.name)

def test_read_file_line_by_line_empty_file():
    """Test reading an empty file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            lines = read_file_line_by_line(temp_file.name)
            assert lines == []
        finally:
            os.unlink(temp_file.name)

def test_read_file_line_by_line_with_newlines():
    """Test reading a file with extra newlines."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Line1\n\nLine2\n\n")
        temp_file.close()
        
        try:
            lines = read_file_line_by_line(temp_file.name)
            assert lines == ["Line1", "", "Line2", ""]
        finally:
            os.unlink(temp_file.name)

def test_read_file_line_by_line_nonexistent_file():
    """Test reading a nonexistent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        read_file_line_by_line("nonexistent_file.txt")

def test_read_file_line_by_line_invalid_input():
    """Test that invalid input types raise TypeError."""
    with pytest.raises(TypeError):
        read_file_line_by_line(123)
    
    with pytest.raises(TypeError):
        read_file_line_by_line(None)