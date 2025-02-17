import os
import pytest
import shutil
from src.file_operations import move_file

@pytest.fixture
def setup_test_files(tmpdir):
    # Create a temporary source directory
    source_dir = tmpdir.mkdir("source")
    # Create a temporary destination directory
    dest_dir = tmpdir.mkdir("destination")
    
    # Create a test file
    test_file_path = os.path.join(source_dir, "test_file.txt")
    with open(test_file_path, 'w') as f:
        f.write("Test content")
    
    return {
        'source_dir': str(source_dir),
        'dest_dir': str(dest_dir),
        'source_file': test_file_path
    }

def test_move_file_successful(setup_test_files):
    source_file = setup_test_files['source_file']
    dest_dir = setup_test_files['dest_dir']
    dest_path = os.path.join(dest_dir, "moved_file.txt")
    
    # Move the file
    moved_file_path = move_file(source_file, dest_path)
    
    # Verify file was moved
    assert os.path.exists(moved_file_path)
    assert not os.path.exists(source_file)
    assert moved_file_path == dest_path

def test_move_file_nonexistent_source(setup_test_files):
    dest_dir = setup_test_files['dest_dir']
    
    # Try to move a non-existent file
    with pytest.raises(FileNotFoundError):
        move_file("non_existent_file.txt", os.path.join(dest_dir, "some_file.txt"))

def test_move_file_to_existing_path(setup_test_files):
    source_file = setup_test_files['source_file']
    dest_dir = setup_test_files['dest_dir']
    
    # Create a destination file
    dest_path = os.path.join(dest_dir, "existing_file.txt")
    with open(dest_path, 'w') as f:
        f.write("Existing content")
    
    # Moving should overwrite the existing file
    moved_file_path = move_file(source_file, dest_path)
    
    assert os.path.exists(moved_file_path)
    assert not os.path.exists(source_file)

def test_move_file_directory_source(setup_test_files):
    source_dir = setup_test_files['source_dir']
    dest_dir = setup_test_files['dest_dir']
    
    # Try to move a directory instead of a file
    with pytest.raises(IsADirectoryError):
        move_file(source_dir, os.path.join(dest_dir, "some_dir"))