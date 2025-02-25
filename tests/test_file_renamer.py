import os
import pytest
import shutil
import tempfile

from src.file_renamer import rename_file

@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

def test_rename_file_success(temp_dir):
    """Test successful file renaming."""
    # Create source file
    source_path = os.path.join(temp_dir, 'source.txt')
    dest_path = os.path.join(temp_dir, 'destination.txt')
    
    with open(source_path, 'w') as f:
        f.write('Test content')
    
    # Rename file
    result = rename_file(source_path, dest_path)
    
    # Verify
    assert result == dest_path
    assert os.path.exists(dest_path)
    assert not os.path.exists(source_path)

def test_rename_file_to_different_directory(temp_dir):
    """Test renaming file to a different directory."""
    # Create source file
    source_path = os.path.join(temp_dir, 'source.txt')
    dest_dir = os.path.join(temp_dir, 'subdirectory')
    dest_path = os.path.join(dest_dir, 'destination.txt')
    
    with open(source_path, 'w') as f:
        f.write('Test content')
    
    # Rename file
    result = rename_file(source_path, dest_path)
    
    # Verify
    assert result == dest_path
    assert os.path.exists(dest_path)
    assert not os.path.exists(source_path)

def test_rename_file_nonexistent_source(temp_dir):
    """Test renaming a non-existent file raises FileNotFoundError."""
    source_path = os.path.join(temp_dir, 'nonexistent.txt')
    dest_path = os.path.join(temp_dir, 'destination.txt')
    
    with pytest.raises(FileNotFoundError):
        rename_file(source_path, dest_path)

def test_rename_file_destination_exists(temp_dir):
    """Test renaming to an existing file raises FileExistsError."""
    source_path = os.path.join(temp_dir, 'source.txt')
    dest_path = os.path.join(temp_dir, 'destination.txt')
    
    # Create both source and destination files
    with open(source_path, 'w') as f:
        f.write('Source content')
    with open(dest_path, 'w') as f:
        f.write('Destination content')
    
    # Attempt to rename
    with pytest.raises(FileExistsError):
        rename_file(source_path, dest_path)

def test_rename_file_invalid_input_types():
    """Test that non-string inputs raise TypeError."""
    with pytest.raises(TypeError):
        rename_file(123, 'dest.txt')
    
    with pytest.raises(TypeError):
        rename_file('source.txt', 456)

def test_rename_directory_fails(temp_dir):
    """Test that trying to rename a directory raises IsADirectoryError."""
    # Create a directory
    source_dir = os.path.join(temp_dir, 'source_dir')
    os.makedirs(source_dir)
    dest_path = os.path.join(temp_dir, 'destination.txt')
    
    with pytest.raises(IsADirectoryError):
        rename_file(source_dir, dest_path)