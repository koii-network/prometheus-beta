import os
import pytest
import shutil
from src.file_mover import move_file

@pytest.fixture
def temp_dir(tmp_path):
    """Create a temporary directory for testing."""
    return tmp_path

@pytest.fixture
def sample_file(temp_dir):
    """Create a sample file for testing."""
    file_path = temp_dir / "sample.txt"
    file_path.write_text("Test content")
    return str(file_path)

def test_move_file_to_existing_directory(sample_file, temp_dir):
    """Test moving a file to an existing directory."""
    destination_dir = temp_dir / "destination"
    destination_dir.mkdir()
    
    # Move the file
    moved_path = move_file(sample_file, str(destination_dir))
    
    # Check that file is moved and exists in the new location
    assert os.path.exists(moved_path)
    assert os.path.basename(moved_path) == "sample.txt"
    assert not os.path.exists(sample_file)

def test_move_file_to_new_location(sample_file, temp_dir):
    """Test moving a file to a new location including filename."""
    destination_path = str(temp_dir / "new_location" / "renamed.txt")
    
    # Move the file
    moved_path = move_file(sample_file, destination_path)
    
    # Check that file is moved and exists in the new location
    assert os.path.exists(moved_path)
    assert os.path.basename(moved_path) == "renamed.txt"
    assert not os.path.exists(sample_file)

def test_move_nonexistent_file(temp_dir):
    """Test moving a nonexistent file raises FileNotFoundError."""
    nonexistent_file = str(temp_dir / "nonexistent.txt")
    
    with pytest.raises(FileNotFoundError):
        move_file(nonexistent_file, str(temp_dir))

def test_move_to_invalid_path(sample_file):
    """Test moving a file with invalid destination path."""
    with pytest.raises(ValueError):
        move_file(sample_file, "")

def test_move_directory_instead_of_file(temp_dir):
    """Test attempting to move a directory instead of a file."""
    with pytest.raises(IsADirectoryError):
        move_file(str(temp_dir), str(temp_dir / "destination"))