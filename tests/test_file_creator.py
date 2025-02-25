import os
import pytest
import tempfile
import shutil

from src.file_creator import create_text_file

def test_create_empty_file():
    """Test creating an empty file"""
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'empty_file.txt')
        created_path = create_text_file(file_path)
        
        assert created_path == file_path
        assert os.path.exists(file_path)
        assert os.path.getsize(file_path) == 0

def test_create_file_with_content():
    """Test creating a file with specific content"""
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'test_file.txt')
        test_content = "Hello, World!"
        created_path = create_text_file(file_path, test_content)
        
        assert created_path == file_path
        with open(file_path, 'r') as file:
            content = file.read()
            assert content == test_content

def test_create_file_in_nested_directory():
    """Test creating a file in a nested directory"""
    with tempfile.TemporaryDirectory() as temp_dir:
        nested_path = os.path.join(temp_dir, 'nested', 'dir', 'test_file.txt')
        created_path = create_text_file(nested_path, "Nested file content")
        
        assert created_path == nested_path
        assert os.path.exists(nested_path)

def test_empty_file_path_raises_error():
    """Test that empty file path raises ValueError"""
    with pytest.raises(ValueError, match="File path cannot be empty"):
        create_text_file('')

def test_none_file_path_raises_error():
    """Test that None file path raises ValueError"""
    with pytest.raises(ValueError, match="File path cannot be empty"):
        create_text_file(None)

def test_file_with_non_string_content():
    """Test creating a file with non-string content"""
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'numeric_file.txt')
        created_path = create_text_file(file_path, 42)
        
        with open(file_path, 'r') as file:
            content = file.read()
            assert content == '42'