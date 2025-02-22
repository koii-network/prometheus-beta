import os
import pytest
import sys
import tempfile

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from is_hidden import is_hidden_file

def test_hidden_file_with_dot_prefix():
    """Test that files starting with a dot are recognized as hidden."""
    with tempfile.NamedTemporaryFile(prefix='.') as temp_file:
        assert is_hidden_file(temp_file.name) is True

def test_non_hidden_file():
    """Test that normal files are not considered hidden."""
    with tempfile.NamedTemporaryFile() as temp_file:
        assert is_hidden_file(temp_file.name) is False

def test_invalid_file_path():
    """Test that a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        is_hidden_file('/path/to/nonexistent/file')

def test_invalid_input_type():
    """Test that invalid input types raise TypeError."""
    with pytest.raises(TypeError):
        is_hidden_file(123)
    with pytest.raises(TypeError):
        is_hidden_file(None)