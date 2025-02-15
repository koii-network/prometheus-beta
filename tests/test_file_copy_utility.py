import os
import pytest
import tempfile
import shutil
from src.file_copy_utility import copy_file

def test_successful_file_copy():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a source file
        source_path = os.path.join(tmpdir, 'source.txt')
        with open(source_path, 'w') as f:
            f.write('Test content')
        
        # Define destination path
        destination_path = os.path.join(tmpdir, 'destination.txt')
        
        # Copy file
        result = copy_file(source_path, destination_path)
        
        # Assertions
        assert result == destination_path
        assert os.path.exists(destination_path)
        
        # Check file contents
        with open(destination_path, 'r') as f:
            assert f.read() == 'Test content'

def test_copy_to_new_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a source file
        source_path = os.path.join(tmpdir, 'source.txt')
        with open(source_path, 'w') as f:
            f.write('Test content')
        
        # Define destination path in a new directory
        destination_dir = os.path.join(tmpdir, 'new_directory')
        destination_path = os.path.join(destination_dir, 'destination.txt')
        
        # Copy file
        result = copy_file(source_path, destination_path)
        
        # Assertions
        assert result == destination_path
        assert os.path.exists(destination_path)

def test_source_file_not_found():
    with tempfile.TemporaryDirectory() as tmpdir:
        source_path = os.path.join(tmpdir, 'nonexistent.txt')
        destination_path = os.path.join(tmpdir, 'destination.txt')
        
        with pytest.raises(FileNotFoundError):
            copy_file(source_path, destination_path)

def test_source_is_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        source_path = tmpdir  # Use the temp directory itself as source
        destination_path = os.path.join(tmpdir, 'destination.txt')
        
        with pytest.raises(IsADirectoryError):
            copy_file(source_path, destination_path)