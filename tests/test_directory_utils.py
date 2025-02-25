import os
import pytest
import shutil
import tempfile

from src.directory_utils import create_directory

def test_create_directory():
    """Test creating a new directory."""
    with tempfile.TemporaryDirectory() as temp_base:
        test_dir_path = os.path.join(temp_base, 'new_test_directory')
        
        # Test directory creation
        created_path = create_directory(test_dir_path)
        
        assert os.path.exists(created_path)
        assert os.path.isdir(created_path)
        assert created_path == os.path.abspath(test_dir_path)

def test_create_existing_directory():
    """Test that creating an existing directory raises FileExistsError."""
    with tempfile.TemporaryDirectory() as temp_base:
        existing_dir = os.path.join(temp_base, 'existing_directory')
        os.makedirs(existing_dir)
        
        with pytest.raises(FileExistsError):
            create_directory(existing_dir)

def test_create_directory_with_subdirs():
    """Test creating a directory with multiple nested subdirectories."""
    with tempfile.TemporaryDirectory() as temp_base:
        nested_dir_path = os.path.join(temp_base, 'parent', 'child', 'grandchild')
        
        created_path = create_directory(nested_dir_path)
        
        assert os.path.exists(created_path)
        assert os.path.isdir(created_path)
        assert created_path == os.path.abspath(nested_dir_path)

def test_create_directory_with_relative_path():
    """Test creating a directory with a relative path."""
    with tempfile.TemporaryDirectory() as temp_base:
        original_cwd = os.getcwd()
        os.chdir(temp_base)
        
        try:
            relative_dir_path = 'relative_test_directory'
            created_path = create_directory(relative_dir_path)
            
            assert os.path.exists(created_path)
            assert os.path.isdir(created_path)
            assert created_path == os.path.abspath(relative_dir_path)
        finally:
            os.chdir(original_cwd)