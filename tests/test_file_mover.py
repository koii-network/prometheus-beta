import os
import pytest
import shutil
from src.file_mover import move_file

@pytest.fixture
def setup_test_files(tmp_path):
    # Create a test directory and files
    source_dir = tmp_path / "source"
    dest_dir = tmp_path / "destination"
    source_dir.mkdir()
    dest_dir.mkdir()
    
    test_file = source_dir / "test_file.txt"
    test_file.write_text("Test content")
    
    return str(source_dir / "test_file.txt"), str(dest_dir / "moved_file.txt")

def test_move_file_success(setup_test_files):
    source_path, dest_path = setup_test_files
    
    # Perform file move
    result = move_file(source_path, dest_path)
    
    # Check that move was successful
    assert result is True
    assert os.path.exists(dest_path)
    assert not os.path.exists(source_path)

def test_move_file_nonexistent_source():
    with pytest.raises(FileNotFoundError):
        move_file("nonexistent_file.txt", "destination.txt")

def test_move_file_is_directory(tmp_path):
    test_dir = tmp_path / "test_directory"
    test_dir.mkdir()
    
    with pytest.raises(IsADirectoryError):
        move_file(str(test_dir), "destination.txt")

def test_move_file_destination_directory_creation(tmp_path):
    source_file = tmp_path / "source" / "test_file.txt"
    source_file.parent.mkdir()
    source_file.write_text("Test content")
    
    dest_path = str(tmp_path / "new_directory" / "moved_file.txt")
    
    result = move_file(str(source_file), dest_path)
    
    assert result is True
    assert os.path.exists(dest_path)