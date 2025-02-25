import os
import pytest
import shutil
import tempfile

from src.file_copy import copy_file

def test_successful_file_copy():
    """Test successful file copy."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create source file
        source_path = os.path.join(tmpdir, 'source.txt')
        with open(source_path, 'w') as f:
            f.write('Test content')

        # Define destination path
        dest_path = os.path.join(tmpdir, 'destination.txt')

        # Perform copy
        result = copy_file(source_path, dest_path)

        # Assertions
        assert result is True
        assert os.path.exists(dest_path)
        with open(dest_path, 'r') as f:
            assert f.read() == 'Test content'

def test_copy_to_new_directory():
    """Test copying file to a new directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create source file
        source_path = os.path.join(tmpdir, 'source.txt')
        with open(source_path, 'w') as f:
            f.write('Test content')

        # Define destination path in a new subdirectory
        dest_path = os.path.join(tmpdir, 'new_dir', 'destination.txt')

        # Perform copy
        result = copy_file(source_path, dest_path)

        # Assertions
        assert result is True
        assert os.path.exists(dest_path)

def test_source_file_not_exists():
    """Test copying non-existent file raises FileNotFoundError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        non_existent_source = os.path.join(tmpdir, 'non_existent.txt')
        dest_path = os.path.join(tmpdir, 'destination.txt')

        with pytest.raises(FileNotFoundError):
            copy_file(non_existent_source, dest_path)

def test_source_is_directory():
    """Test trying to copy a directory raises IsADirectoryError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        dest_path = os.path.join(tmpdir, 'destination.txt')

        with pytest.raises(IsADirectoryError):
            copy_file(tmpdir, dest_path)

def test_invalid_input_types():
    """Test that non-string inputs raise TypeError."""
    with pytest.raises(TypeError):
        copy_file(123, 'dest')
    
    with pytest.raises(TypeError):
        copy_file('source', 456)

def test_file_preservation():
    """Test that original file is preserved after copy."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create source file
        source_path = os.path.join(tmpdir, 'source.txt')
        with open(source_path, 'w') as f:
            f.write('Original content')

        # Define destination path
        dest_path = os.path.join(tmpdir, 'destination.txt')

        # Perform copy
        copy_file(source_path, dest_path)

        # Check both files exist and have correct content
        assert os.path.exists(source_path)
        assert os.path.exists(dest_path)
        
        with open(source_path, 'r') as f:
            assert f.read() == 'Original content'
        with open(dest_path, 'r') as f:
            assert f.read() == 'Original content'