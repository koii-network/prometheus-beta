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
    
    return {
        "source_dir": str(source_dir),
        "dest_dir": str(dest_dir),
        "source_file": str(test_file),
        "dest_file": str(dest_dir / "test_file.txt")
    }

def test_move_file_success(setup_test_files):
    """Test successful file move."""
    source_file = setup_test_files["source_file"]
    dest_file = setup_test_files["dest_file"]
    
    # Move the file
    result = move_file(source_file, dest_file)
    
    # Verify file was moved
    assert result == dest_file
    assert not os.path.exists(source_file)
    assert os.path.exists(dest_file)
    
    # Verify file contents
    with open(dest_file, 'r') as f:
        assert f.read() == "Test content"

def test_move_to_new_directory(setup_test_files):
    """Test moving file to a new directory that doesn't exist."""
    source_file = setup_test_files["source_file"]
    new_dest_dir = os.path.join(setup_test_files["dest_dir"], "new_subdir")
    new_dest_file = os.path.join(new_dest_dir, "test_file.txt")
    
    # Move the file
    result = move_file(source_file, new_dest_file)
    
    # Verify file was moved and directory was created
    assert result == new_dest_file
    assert os.path.exists(new_dest_file)
    assert not os.path.exists(source_file)

def test_file_not_found(setup_test_files):
    """Test moving a non-existent file."""
    non_existent_file = os.path.join(setup_test_files["source_dir"], "non_existent.txt")
    
    with pytest.raises(FileNotFoundError):
        move_file(non_existent_file, setup_test_files["dest_file"])

def test_move_directory(setup_test_files):
    """Test attempting to move a directory instead of a file."""
    with pytest.raises(IsADirectoryError):
        move_file(setup_test_files["source_dir"], setup_test_files["dest_dir"])