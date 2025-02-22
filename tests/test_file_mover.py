import os
import pytest
import shutil

# Import the function to test
from src.file_mover import move_file

@pytest.fixture
def setup_test_files(tmp_path):
    """Create temporary files and directories for testing."""
    # Create source directory
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    
    # Create destination directory
    dest_dir = tmp_path / "destination"
    dest_dir.mkdir()
    
    # Create a test file in source directory
    test_file = source_dir / "test_file.txt"
    test_file.write_text("Test content")
    
    return {
        "source_dir": str(source_dir),
        "dest_dir": str(dest_dir),
        "test_file": str(test_file)
    }

def test_move_file_success(setup_test_files):
    """Test successful file move."""
    source_file = setup_test_files["test_file"]
    dest_dir = setup_test_files["dest_dir"]
    dest_path = os.path.join(dest_dir, "moved_file.txt")
    
    # Move the file
    moved_path = move_file(source_file, dest_path)
    
    # Verify file was moved
    assert os.path.exists(dest_path)
    assert not os.path.exists(source_file)
    assert moved_path == dest_path

def test_move_file_nonexistent_source(setup_test_files):
    """Test moving a non-existent file raises FileNotFoundError."""
    source_file = "/path/to/nonexistent/file.txt"
    dest_dir = setup_test_files["dest_dir"]
    dest_path = os.path.join(dest_dir, "moved_file.txt")
    
    with pytest.raises(FileNotFoundError):
        move_file(source_file, dest_path)

def test_move_file_directory_source(setup_test_files):
    """Test attempting to move a directory raises IsADirectoryError."""
    source_dir = setup_test_files["source_dir"]
    dest_dir = setup_test_files["dest_dir"]
    dest_path = os.path.join(dest_dir, "moved_directory")
    
    with pytest.raises(IsADirectoryError):
        move_file(source_dir, dest_path)

def test_move_file_creates_destination_dir(setup_test_files):
    """Test that destination directory is created if it doesn't exist."""
    source_file = setup_test_files["test_file"]
    dest_dir = setup_test_files["dest_dir"]
    
    # Create a nested destination path that doesn't exist yet
    dest_path = os.path.join(dest_dir, "nested", "subdirectory", "moved_file.txt")
    
    # Move the file
    moved_path = move_file(source_file, dest_path)
    
    # Verify file was moved and destination directories were created
    assert os.path.exists(dest_path)
    assert not os.path.exists(source_file)
    assert moved_path == dest_path