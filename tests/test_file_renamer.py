import os
import pytest
import shutil
from src.file_renamer import rename_file

@pytest.fixture
def setup_test_files(tmpdir):
    """Fixture to create test files."""
    # Create a test directory
    test_dir = tmpdir.mkdir("test_rename")
    
    # Create a source file
    source_file = test_dir.join("source.txt")
    source_file.write("Test content")
    
    return {
        'test_dir': str(test_dir),
        'source_path': str(source_file),
    }

def test_rename_file_success(setup_test_files):
    """Test successful file renaming."""
    source_path = setup_test_files['source_path']
    destination_path = os.path.join(os.path.dirname(source_path), "destination.txt")
    
    # Rename the file
    result = rename_file(source_path, destination_path)
    
    # Check the file was renamed
    assert result == destination_path
    assert os.path.exists(destination_path)
    assert not os.path.exists(source_path)

def test_rename_file_nonexistent_source(setup_test_files):
    """Test renaming a non-existent file raises FileNotFoundError."""
    non_existent_path = os.path.join(setup_test_files['test_dir'], "non_existent.txt")
    destination_path = os.path.join(setup_test_files['test_dir'], "destination.txt")
    
    with pytest.raises(FileNotFoundError):
        rename_file(non_existent_path, destination_path)

def test_rename_file_destination_exists(setup_test_files):
    """Test renaming to an existing file raises FileExistsError."""
    source_path = setup_test_files['source_path']
    destination_path = os.path.join(os.path.dirname(source_path), "existing.txt")
    
    # Create destination file
    with open(destination_path, 'w') as f:
        f.write("Existing content")
    
    with pytest.raises(FileExistsError):
        rename_file(source_path, destination_path)

def test_rename_file_to_different_directory(setup_test_files):
    """Test renaming a file to a different directory."""
    source_path = setup_test_files['source_path']
    new_dir = os.path.join(setup_test_files['test_dir'], "new_directory")
    destination_path = os.path.join(new_dir, "destination.txt")
    
    # Rename the file
    result = rename_file(source_path, destination_path)
    
    # Check the file was renamed and moved
    assert result == destination_path
    assert os.path.exists(destination_path)
    assert not os.path.exists(source_path)

def test_rename_directory_fails(setup_test_files):
    """Test that attempting to rename a directory fails."""
    test_dir = setup_test_files['test_dir']
    destination_path = os.path.join(os.path.dirname(test_dir), "new_directory")
    
    with pytest.raises(IsADirectoryError):
        rename_file(test_dir, destination_path)