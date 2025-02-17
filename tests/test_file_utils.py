import os
import pytest
from src.file_utils import file_exists

def test_file_exists_true():
    """Test that an existing file returns True."""
    # Use an existing file in the repository as a test case
    existing_file = 'README.md'
    assert file_exists(existing_file) is True

def test_file_exists_false():
    """Test that a non-existent file returns False."""
    non_existent_file = 'non_existent_file.txt'
    assert file_exists(non_existent_file) is False

def test_file_exists_absolute_path():
    """Test file existence with an absolute path."""
    abs_path = os.path.abspath('README.md')
    assert file_exists(abs_path) is True

def test_file_exists_empty_string():
    """Test file existence with an empty string."""
    assert file_exists('') is False

def test_file_exists_none():
    """Test file existence with None input."""
    with pytest.raises(TypeError):
        file_exists(None)