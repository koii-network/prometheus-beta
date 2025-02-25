import os
import pytest
import shutil
from src.directory_utils import create_directory

def test_create_directory_success(tmp_path):
    """Test successful directory creation."""
    test_dir = os.path.join(tmp_path, 'new_directory')
    result = create_directory(test_dir)
    
    assert os.path.exists(test_dir)
    assert os.path.isdir(test_dir)
    assert result == os.path.abspath(test_dir)

def test_create_directory_existing_raises_error(tmp_path):
    """Test that creating an existing directory raises an error."""
    test_dir = os.path.join(tmp_path, 'existing_directory')
    os.makedirs(test_dir)
    
    with pytest.raises(OSError, match="Directory already exists"):
        create_directory(test_dir)

def test_create_directory_nested(tmp_path):
    """Test creating a nested directory."""
    nested_dir = os.path.join(tmp_path, 'parent', 'child', 'grandchild')
    result = create_directory(nested_dir)
    
    assert os.path.exists(nested_dir)
    assert os.path.isdir(nested_dir)
    assert result == os.path.abspath(nested_dir)

def test_create_directory_relative_path(tmp_path):
    """Test creating a directory with a relative path."""
    # Change current working directory to tmp_path
    original_cwd = os.getcwd()
    os.chdir(tmp_path)
    
    try:
        relative_dir = 'relative_directory'
        result = create_directory(relative_dir)
        
        assert os.path.exists(os.path.join(tmp_path, relative_dir))
        assert result == os.path.abspath(relative_dir)
    finally:
        # Restore original working directory
        os.chdir(original_cwd)