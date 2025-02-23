import os
import pytest
import shutil
from src.file_renamer import rename_file

@pytest.fixture
def setup_test_files(tmp_path):
    """Create temporary test files for renaming operations."""
    # Create a test directory
    test_dir = tmp_path / "test_files"
    test_dir.mkdir()
    
    # Create a source file
    source_file = test_dir / "source.txt"
    source_file.write_text("Test content")
    
    return {
        "test_dir": test_dir,
        "source_file": str(source_file)
    }

def test_rename_file_success(setup_test_files):
    """Test successful file renaming."""
    source_file = setup_test_files["source_file"]
    destination_file = os.path.join(os.path.dirname(source_file), "renamed.txt")
    
    rename_file(source_file, destination_file)
    
    assert not os.path.exists(source_file)
    assert os.path.exists(destination_file)

def test_rename_to_different_directory(setup_test_files):
    """Test renaming a file to a different directory."""
    source_file = setup_test_files["source_file"]
    test_dir = setup_test_files["test_dir"]
    
    new_dir = test_dir / "new_directory"
    new_dir.mkdir()
    destination_file = str(new_dir / "renamed.txt")
    
    rename_file(source_file, destination_file)
    
    assert not os.path.exists(source_file)
    assert os.path.exists(destination_file)

def test_rename_nonexistent_file(setup_test_files):
    """Test renaming a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        rename_file("/path/to/nonexistent/file.txt", "/path/to/destination.txt")

def test_rename_to_existing_file(setup_test_files):
    """Test renaming to an existing file raises FileExistsError."""
    source_file = setup_test_files["source_file"]
    test_dir = setup_test_files["test_dir"]
    
    existing_file = test_dir / "existing.txt"
    existing_file.write_text("Another test file")
    
    with pytest.raises(FileExistsError):
        rename_file(source_file, str(existing_file))

def test_rename_directory(setup_test_files):
    """Test renaming a directory raises IsADirectoryError."""
    test_dir = setup_test_files["test_dir"]
    
    with pytest.raises(IsADirectoryError):
        rename_file(str(test_dir), "/path/to/destination")