import os
import pytest
import tempfile
import shutil

from src.directory_checker import is_directory_exists

def test_existing_directory():
    """Test that an existing directory returns True."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert is_directory_exists(temp_dir) is True

def test_non_existing_directory():
    """Test that a non-existing directory returns False."""
    non_existing_path = "/path/to/definitely/non/existing/directory"
    assert is_directory_exists(non_existing_path) is False

def test_file_path():
    """Test that a file path returns False."""
    with tempfile.NamedTemporaryFile() as temp_file:
        assert is_directory_exists(temp_file.name) is False

def test_invalid_input_type():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Path must be a string"):
        is_directory_exists(123)
    
    with pytest.raises(TypeError, match="Path must be a string"):
        is_directory_exists(None)

def test_relative_path():
    """Test that relative paths are handled correctly."""
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Change current working directory
        original_cwd = os.getcwd()
        os.chdir(temp_dir)
        
        try:
            # Create a subdirectory
            os.mkdir('test_subdir')
            
            # Test relative path
            assert is_directory_exists('test_subdir') is True
            assert is_directory_exists('./test_subdir') is True
        finally:
            # Restore original working directory
            os.chdir(original_cwd)

def test_path_normalization():
    """Test that different path representations are handled correctly."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a subdirectory
        subdir = os.path.join(temp_dir, 'test_dir')
        os.mkdir(subdir)
        
        # Test various path representations
        assert is_directory_exists(subdir) is True
        assert is_directory_exists(subdir + '/') is True
        assert is_directory_exists(os.path.join(subdir, '..', os.path.basename(subdir))) is True