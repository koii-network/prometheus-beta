import os
import pytest
from src.file_creator import create_text_file

def test_create_empty_file(tmp_path):
    """Test creating an empty file"""
    file_path = os.path.join(tmp_path, 'test_empty.txt')
    result = create_text_file(file_path)
    assert result is True
    assert os.path.exists(file_path)
    assert os.path.getsize(file_path) == 0

def test_create_file_with_content(tmp_path):
    """Test creating a file with specific content"""
    file_path = os.path.join(tmp_path, 'test_content.txt')
    test_content = "Hello, world!"
    result = create_text_file(file_path, test_content)
    assert result is True
    assert os.path.exists(file_path)
    with open(file_path, 'r') as f:
        assert f.read() == test_content

def test_create_file_in_nested_directory(tmp_path):
    """Test creating a file in a nested directory"""
    file_path = os.path.join(tmp_path, 'nested', 'dir', 'test_nested.txt')
    result = create_text_file(file_path)
    assert result is True
    assert os.path.exists(file_path)

def test_create_file_invalid_path():
    """Test creating a file with empty path raises ValueError"""
    with pytest.raises(ValueError):
        create_text_file('')

def test_create_file_none_path():
    """Test creating a file with None path raises ValueError"""
    with pytest.raises(ValueError):
        create_text_file(None)