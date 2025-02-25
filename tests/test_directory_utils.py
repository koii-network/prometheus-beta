import os
import pytest
import tempfile
import shutil

from src.directory_utils import create_directory

def test_create_directory_success():
    """Test creating a new directory successfully."""
    with tempfile.TemporaryDirectory() as temp_base:
        test_dir = os.path.join(temp_base, 'new_directory')
        result = create_directory(test_dir)
        assert result == os.path.abspath(test_dir)
        assert os.path.isdir(test_dir)

def test_create_directory_existing_without_exist_ok():
    """Test that creating an existing directory raises an error by default."""
    with tempfile.TemporaryDirectory() as temp_base:
        test_dir = os.path.join(temp_base, 'existing_directory')
        os.mkdir(test_dir)
        
        with pytest.raises(FileExistsError):
            create_directory(test_dir)

def test_create_directory_existing_with_exist_ok():
    """Test creating an existing directory with exist_ok=True."""
    with tempfile.TemporaryDirectory() as temp_base:
        test_dir = os.path.join(temp_base, 'existing_directory')
        os.mkdir(test_dir)
        
        result = create_directory(test_dir, exist_ok=True)
        assert result == os.path.abspath(test_dir)

def test_create_nested_directories():
    """Test creating nested directories."""
    with tempfile.TemporaryDirectory() as temp_base:
        nested_dir = os.path.join(temp_base, 'parent', 'child', 'grandchild')
        result = create_directory(nested_dir)
        assert result == os.path.abspath(nested_dir)
        assert os.path.isdir(nested_dir)

def test_create_directory_invalid_input():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        create_directory(123)
    
    with pytest.raises(ValueError):
        create_directory('')
    
    with pytest.raises(ValueError):
        create_directory('   ')

def test_create_directory_home_expansion():
    """Test home directory path expansion."""
    home_dir = os.path.expanduser('~')
    test_dir = os.path.join('~', 'test_directory')
    result = create_directory(test_dir)
    full_path = os.path.join(home_dir, 'test_directory')
    
    assert result == os.path.abspath(full_path)
    assert os.path.isdir(full_path)
    
    # Clean up the created directory
    shutil.rmtree(full_path)