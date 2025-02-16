import os
import pytest
from src.file_utils import file_exists

def test_file_exists_true():
    """Test that existing files return True."""
    # Use an existing file in the repository
    assert file_exists('README.md') == True
    assert file_exists('.gitignore') == True
    assert file_exists('requirements.txt') == True

def test_file_exists_false():
    """Test that non-existent files return False."""
    assert file_exists('non_existent_file.txt') == False
    assert file_exists('') == False

def test_file_exists_directory():
    """Test that directories return False."""
    assert file_exists('.') == False
    assert file_exists('src') == False

def test_file_exists_invalid_input():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        file_exists(None)
    with pytest.raises(TypeError):
        file_exists(123)