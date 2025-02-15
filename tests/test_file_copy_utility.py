import os
import pytest
import shutil
from src.file_copy_utility import copy_file

@pytest.fixture
def temp_test_dir(tmp_path):
    """Create a temporary directory for test files."""
    return tmp_path

def test_successful_file_copy(temp_test_dir):
    # Create a source file
    source_file = temp_test_dir / 'source.txt'
    source_file.write_text('Test content')
    
    # Define destination
    dest_file = temp_test_dir / 'destination.txt'
    
    # Perform copy
    result = copy_file(str(source_file), str(dest_file))
    
    # Assertions
    assert os.path.exists(dest_file)
    assert result == str(dest_file)
    assert dest_file.read_text() == 'Test content'

def test_copy_to_nonexistent_directory(temp_test_dir):
    # Create a source file
    source_file = temp_test_dir / 'source.txt'
    source_file.write_text('Test content')
    
    # Define destination in a new subdirectory
    dest_dir = temp_test_dir / 'new_subdir'
    dest_file = dest_dir / 'destination.txt'
    
    # Perform copy
    result = copy_file(str(source_file), str(dest_file))
    
    # Assertions
    assert os.path.exists(dest_file)
    assert result == str(dest_file)

def test_source_file_not_found(temp_test_dir):
    non_existent_source = temp_test_dir / 'non_existent.txt'
    dest_file = temp_test_dir / 'destination.txt'
    
    with pytest.raises(FileNotFoundError):
        copy_file(str(non_existent_source), str(dest_file))

def test_source_is_directory(temp_test_dir):
    source_dir = temp_test_dir / 'source_dir'
    source_dir.mkdir()
    dest_file = temp_test_dir / 'destination.txt'
    
    with pytest.raises(IsADirectoryError):
        copy_file(str(source_dir), str(dest_file))

def test_same_source_and_destination(temp_test_dir):
    source_file = temp_test_dir / 'source.txt'
    source_file.write_text('Test content')
    
    with pytest.raises(ValueError):
        copy_file(str(source_file), str(source_file))