import os
import pytest
import shutil
from src.file_copy_utility import copy_file

@pytest.fixture
def temp_files(tmp_path):
    """Create temporary files for testing."""
    # Create source file
    source_file = tmp_path / "source_file.txt"
    source_file.write_text("Test content")
    
    # Create destination directory
    dest_dir = tmp_path / "destination"
    dest_dir.mkdir()
    
    return {
        "source_path": str(source_file),
        "dest_dir": str(dest_dir),
        "dest_path": str(dest_dir / "copied_file.txt")
    }

def test_successful_file_copy(temp_files):
    """Test successful file copy."""
    result = copy_file(temp_files["source_path"], temp_files["dest_path"])
    
    assert result == temp_files["dest_path"]
    assert os.path.exists(temp_files["dest_path"])
    
    with open(temp_files["source_path"], 'r') as source, \
         open(temp_files["dest_path"], 'r') as dest:
        assert source.read() == dest.read()

def test_source_file_not_found(temp_files):
    """Test when source file does not exist."""
    non_existent_source = os.path.join(temp_files["dest_dir"], "non_existent.txt")
    
    with pytest.raises(FileNotFoundError):
        copy_file(non_existent_source, temp_files["dest_path"])

def test_source_is_directory(temp_files):
    """Test when source path is a directory."""
    with pytest.raises(IsADirectoryError):
        copy_file(temp_files["dest_dir"], temp_files["dest_path"])

def test_destination_directory_creation(temp_files):
    """Test that destination directory is created if it doesn't exist."""
    new_dest_dir = os.path.join(temp_files["dest_dir"], "new_subdir")
    new_dest_path = os.path.join(new_dest_dir, "new_file.txt")
    
    result = copy_file(temp_files["source_path"], new_dest_path)
    
    assert os.path.exists(new_dest_path)
    assert result == new_dest_path