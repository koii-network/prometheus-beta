import os
import pytest
import shutil
from src.file_mover import move_file

@pytest.fixture
def setup_test_files(tmp_path):
    # Create a source directory with a test file
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    test_file = source_dir / "test_file.txt"
    test_file.write_text("Test content")
    
    # Create a destination directory
    dest_dir = tmp_path / "destination"
    dest_dir.mkdir()
    
    return str(source_dir), str(dest_dir), str(test_file)

def test_move_file_success(setup_test_files):
    source_dir, dest_dir, source_file = setup_test_files
    source_path = os.path.join(source_dir, "test_file.txt")
    dest_path = dest_dir
    
    moved_file_path = move_file(source_path, dest_path)
    
    assert os.path.exists(moved_file_path)
    assert os.path.basename(moved_file_path) == "test_file.txt"
    assert not os.path.exists(source_path)

def test_move_file_nonexistent_source(tmp_path):
    with pytest.raises(FileNotFoundError):
        move_file("nonexistent_file.txt", str(tmp_path))

def test_move_file_empty_paths():
    with pytest.raises(ValueError):
        move_file("", "")

def test_move_file_directory_as_source(tmp_path):
    source_dir = tmp_path / "source_dir"
    source_dir.mkdir()
    
    with pytest.raises(IsADirectoryError):
        move_file(str(source_dir), str(tmp_path))

def test_move_file_same_file_name_in_destination(setup_test_files):
    source_dir, dest_dir, source_file = setup_test_files
    source_path = os.path.join(source_dir, "test_file.txt")
    
    # Move the file first time
    first_move = move_file(source_path, dest_dir)
    
    # Recreate the source file
    source_file = open(source_path, 'w')
    source_file.write("New content")
    source_file.close()
    
    # Move again, should replace the existing file
    second_move = move_file(source_path, dest_dir)
    
    assert os.path.exists(second_move)
    assert not os.path.exists(source_path)