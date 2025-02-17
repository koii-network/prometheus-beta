import os
import pytest
from src.file_existence import file_exists

def test_existing_file():
    """Test that an existing file returns True."""
    assert file_exists('README.md') == True
    assert file_exists('./README.md') == True
    assert file_exists('.//README.md') == True

def test_non_existing_file():
    """Test that a non-existing file returns False."""
    assert file_exists('non_existent_file.txt') == False

def test_directory():
    """Test that directories return False."""
    assert file_exists('.') == False
    assert file_exists('src') == False

def test_path_variations():
    """Test various path formats."""
    assert file_exists('requirements.txt') == True
    assert file_exists('./requirements.txt') == True
    assert file_exists('.//requirements.txt') == True

def test_absolute_path():
    """Test absolute path handling."""
    current_dir = os.path.abspath('.')
    full_readme_path = os.path.join(current_dir, 'README.md')
    assert file_exists(full_readme_path) == True