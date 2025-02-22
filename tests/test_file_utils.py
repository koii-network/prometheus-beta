import os
import pytest
from src.file_utils import file_exists

def test_existing_file():
    """Test that file_exists returns True for existing files."""
    existing_files = [
        '.gitignore', 
        'README.md', 
        'requirements.txt'
    ]
    for file in existing_files:
        assert file_exists(file), f"File {file} should exist"

def test_non_existing_file():
    """Test that file_exists returns False for non-existing files."""
    non_existing_files = [
        'non_existent_file.txt',
        'fake_directory/fake_file.py',
        '/tmp/impossible_file.log'
    ]
    for file in non_existing_files:
        assert not file_exists(file), f"File {file} should not exist"

def test_directory_returns_false():
    """Test that directories are not considered files."""
    assert not file_exists('.'), "Current directory should return False"
    assert not file_exists('src'), "Directory should return False"

def test_empty_path():
    """Test behavior with an empty path."""
    with pytest.raises(TypeError):
        file_exists(None)
    with pytest.raises(TypeError):
        file_exists("")