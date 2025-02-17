import os
import pytest
import tempfile
import shutil
from src.file_copy import copy_file

def test_copy_file_success():
    """Test successful file copy"""
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as dest_dir:
        # Create a source file
        source_file = os.path.join(source_dir, 'source.txt')
        with open(source_file, 'w') as f:
            f.write("Test content")
        
        # Destination file path
        dest_file = os.path.join(dest_dir, 'destination.txt')
        
        # Perform file copy
        result = copy_file(source_file, dest_file)
        
        # Assertions
        assert result is True
        assert os.path.exists(dest_file)
        
        # Verify file content
        with open(dest_file, 'r') as f:
            assert f.read() == "Test content"

def test_copy_file_nonexistent_source():
    """Test copying a non-existent file"""
    with tempfile.TemporaryDirectory() as dest_dir:
        dest_file = os.path.join(dest_dir, 'destination.txt')
        
        with pytest.raises(FileNotFoundError):
            copy_file('/path/to/nonexistent/file.txt', dest_file)

def test_copy_file_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        copy_file(123, 'dest.txt')
    
    with pytest.raises(TypeError):
        copy_file('source.txt', 456)

def test_copy_file_source_is_directory():
    """Test attempting to copy a directory"""
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as dest_dir:
        with pytest.raises(IsADirectoryError):
            copy_file(source_dir, os.path.join(dest_dir, 'file.txt'))

def test_copy_file_destination_directory_creation():
    """Test automatic destination directory creation"""
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as base_dir:
        # Create source file
        source_file = os.path.join(source_dir, 'source.txt')
        with open(source_file, 'w') as f:
            f.write("Test content")
        
        # Destination in a non-existent subdirectory
        dest_file = os.path.join(base_dir, 'new_dir', 'destination.txt')
        
        # Perform file copy
        result = copy_file(source_file, dest_file)
        
        # Assertions
        assert result is True
        assert os.path.exists(dest_file)