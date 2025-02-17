import os
import pytest
import tempfile
import shutil

from src.file_copy import copy_file

def test_successful_file_copy():
    """Test successful file copy."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create source file
        source_path = os.path.join(tmpdir, 'source.txt')
        dest_path = os.path.join(tmpdir, 'destination.txt')
        
        with open(source_path, 'w') as f:
            f.write('Test content')
        
        # Perform file copy
        result = copy_file(source_path, dest_path)
        
        # Assertions
        assert result is True
        assert os.path.exists(dest_path)
        
        # Verify file contents
        with open(dest_path, 'r') as f:
            assert f.read() == 'Test content'

def test_source_file_not_found():
    """Test copying a non-existent file raises FileNotFoundError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        non_existent_source = os.path.join(tmpdir, 'non_existent.txt')
        dest_path = os.path.join(tmpdir, 'destination.txt')
        
        with pytest.raises(FileNotFoundError):
            copy_file(non_existent_source, dest_path)

def test_empty_paths():
    """Test empty paths raise ValueError."""
    with pytest.raises(ValueError):
        copy_file('', '')
    
    with pytest.raises(ValueError):
        copy_file('source.txt', '')
    
    with pytest.raises(ValueError):
        copy_file('', 'destination.txt')

def test_source_is_directory():
    """Test copying a directory raises IsADirectoryError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        with pytest.raises(IsADirectoryError):
            copy_file(tmpdir, os.path.join(tmpdir, 'destination.txt'))

def test_copy_to_existing_path():
    """Test copying to an existing path overwrites the file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create source file
        source_path = os.path.join(tmpdir, 'source.txt')
        dest_path = os.path.join(tmpdir, 'destination.txt')
        
        with open(source_path, 'w') as f:
            f.write('Original content')
        
        with open(dest_path, 'w') as f:
            f.write('Existing content')
        
        # Perform file copy
        result = copy_file(source_path, dest_path)
        
        # Assertions
        assert result is True
        
        # Verify file contents are overwritten
        with open(dest_path, 'r') as f:
            assert f.read() == 'Original content'