import os
import pytest
from src.text_file_creator import create_text_file

def test_create_empty_text_file(tmp_path):
    """Test creating an empty text file"""
    file_path = tmp_path / "empty_file.txt"
    result = create_text_file(str(file_path))
    assert result is True
    assert os.path.exists(file_path)
    assert os.path.getsize(file_path) == 0

def test_create_text_file_with_content(tmp_path):
    """Test creating a text file with content"""
    file_path = tmp_path / "test_file.txt"
    test_content = "Hello, World!"
    result = create_text_file(str(file_path), test_content)
    assert result is True
    assert os.path.exists(file_path)
    with open(file_path, 'r') as file:
        assert file.read() == test_content

def test_create_text_file_in_nested_directory(tmp_path):
    """Test creating a text file in a nested directory"""
    file_path = tmp_path / "nested" / "test_file.txt"
    result = create_text_file(str(file_path), "Nested file content")
    assert result is True
    assert os.path.exists(file_path)

def test_create_text_file_empty_path_raises_error():
    """Test that empty file path raises ValueError"""
    with pytest.raises(ValueError, match="File path cannot be empty"):
        create_text_file("")

def test_create_text_file_none_path_raises_error():
    """Test that None file path raises ValueError"""
    with pytest.raises(ValueError, match="File path cannot be empty"):
        create_text_file(None)