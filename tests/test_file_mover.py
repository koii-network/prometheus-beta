import os
import pytest
import shutil
from src.file_mover import move_file

@pytest.fixture
def setup_test_files(tmp_path):
    # Create a source directory and a test file
    source_dir = tmp_path / "source"
    dest_dir = tmp_path / "destination"
    source_dir.mkdir()
    dest_dir.mkdir()
    
    test_file = source_dir / "test_file.txt"
    test_file.write_text("Test content")
    
    return str(source_dir), str(dest_dir), str(test_file)

def test_move_file_successfully(setup_test_files):
    source_dir, dest_dir, source_file = setup_test_files
    dest_file = os.path.join(dest_dir, "test_file.txt")
    
    # Move the file
    move_file(source_file, dest_file)
    
    # Verify the file was moved
    assert not os.path.exists(source_file)
    assert os.path.exists(dest_file)

def test_move_file_nonexistent_source():
    with pytest.raises(FileNotFoundError):
        move_file("nonexistent_file.txt", "destination/file.txt")

def test_move_file_source_is_directory(tmp_path):
    source_dir = tmp_path / "source_dir"
    source_dir.mkdir()
    
    with pytest.raises(IsADirectoryError):
        move_file(str(source_dir), "destination/file.txt")

def test_move_file_destination_in_new_directory(setup_test_files):
    source_dir, dest_dir, source_file = setup_test_files
    new_subdest = os.path.join(dest_dir, "subdir", "test_file.txt")
    
    # Move the file to a new subdirectory
    move_file(source_file, new_subdest)
    
    # Verify the file was moved and intermediate directories created
    assert not os.path.exists(source_file)
    assert os.path.exists(new_subdest)