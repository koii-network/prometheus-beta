import os
import pytest
import shutil

from src.file_mover import move_file

@pytest.fixture
def setup_test_files(tmp_path):
    # Create a source directory
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    
    # Create a destination directory
    dest_dir = tmp_path / "destination"
    dest_dir.mkdir()
    
    # Create a test file
    test_file = source_dir / "test_file.txt"
    test_file.write_text("Test content")
    
    return {
        "source_dir": str(source_dir),
        "dest_dir": str(dest_dir),
        "test_file": str(test_file)
    }

def test_move_file_successful(setup_test_files):
    """Test successful file movement."""
    source_file = setup_test_files["test_file"]
    dest_dir = setup_test_files["dest_dir"]
    
    # Move the file
    new_path = move_file(source_file, dest_dir)
    
    # Verify file is moved
    assert os.path.exists(new_path)
    assert os.path.basename(new_path) == "test_file.txt"
    assert not os.path.exists(source_file)

def test_move_file_nonexistent_source(setup_test_files):
    """Test moving a non-existent file raises FileNotFoundError."""
    dest_dir = setup_test_files["dest_dir"]
    
    with pytest.raises(FileNotFoundError):
        move_file("nonexistent_file.txt", dest_dir)

def test_move_file_invalid_destination(setup_test_files):
    """Test moving to a non-directory path raises NotADirectoryError."""
    source_file = setup_test_files["test_file"]
    
    with pytest.raises(NotADirectoryError):
        move_file(source_file, "not_a_directory/path")

def test_move_file_same_filename_in_destination(setup_test_files):
    """Test moving a file to a destination with an existing file of the same name."""
    source_file = setup_test_files["test_file"]
    dest_dir = setup_test_files["dest_dir"]
    
    # Create a file with the same name in the destination directory
    existing_file_path = os.path.join(dest_dir, "test_file.txt")
    with open(existing_file_path, "w") as f:
        f.write("Existing content")
    
    # Move the file, which should overwrite the existing file
    new_path = move_file(source_file, dest_dir)
    
    assert os.path.exists(new_path)
    assert not os.path.exists(source_file)
    
    # Verify the content has been replaced
    with open(new_path, "r") as f:
        assert f.read() == "Test content"