import os
import pytest
import shutil
import tempfile

from src.directory_utils import create_directory

def test_create_directory():
    """Test creating a new directory."""
    # Use a temporary directory to avoid cluttering the file system
    with tempfile.TemporaryDirectory() as temp_base:
        test_dir = os.path.join(temp_base, 'new_directory')
        
        # Test successful directory creation
        result = create_directory(test_dir)
        assert result is True
        assert os.path.exists(test_dir)
        assert os.path.isdir(test_dir)

def test_create_existing_directory():
    """Test that creating an existing directory raises FileExistsError."""
    with tempfile.TemporaryDirectory() as temp_base:
        test_dir = os.path.join(temp_base, 'existing_directory')
        
        # Create the directory first
        os.mkdir(test_dir)
        
        # Try to create the same directory again
        with pytest.raises(FileExistsError, match=f"Directory '{test_dir}' already exists."):
            create_directory(test_dir)

def test_create_nested_directories():
    """Test creating nested directories."""
    with tempfile.TemporaryDirectory() as temp_base:
        nested_dir = os.path.join(temp_base, 'parent', 'child', 'grandchild')
        
        # Create nested directories
        result = create_directory(nested_dir)
        assert result is True
        assert os.path.exists(nested_dir)
        assert os.path.isdir(nested_dir)

def test_create_directory_permission_error(mocker):
    """Test handling of permission-related errors."""
    # Mock os.makedirs to simulate a PermissionError
    with mocker.patch('os.makedirs', side_effect=PermissionError("Permission denied")):
        with pytest.raises(PermissionError):
            create_directory('/root/forbidden_dir')  # A directory that would require root permissions