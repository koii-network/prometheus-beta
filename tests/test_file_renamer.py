import os
import pytest
import shutil
from src.file_renamer import rename_file

@pytest.fixture
def setup_test_files(tmp_path):
    """Create test files for renaming operations."""
    # Create a test directory
    test_dir = tmp_path / "test_files"
    test_dir.mkdir()
    
    # Create sample files
    file1 = test_dir / "original_file.txt"
    file1.write_text("Test content")
    
    return {
        "test_dir": test_dir,
        "original_file": file1
    }

def test_rename_file_success(setup_test_files):
    """Test successful file renaming."""
    original_file = setup_test_files["original_file"]
    new_path = os.path.join(os.path.dirname(original_file), "renamed_file.txt")
    
    result = rename_file(str(original_file), new_path)
    
    assert result == new_path
    assert os.path.exists(new_path)
    assert not os.path.exists(str(original_file))

def test_rename_file_not_found():
    """Test renaming a non-existent file."""
    with pytest.raises(FileNotFoundError):
        rename_file("non_existent_file.txt", "new_file.txt")

def test_rename_file_to_existing_destination(setup_test_files):
    """Test renaming to an existing destination."""
    original_file = setup_test_files["original_file"]
    existing_file = os.path.join(os.path.dirname(original_file), "existing_file.txt")
    
    # Create an existing file
    with open(existing_file, 'w') as f:
        f.write("Existing content")
    
    result = rename_file(str(original_file), existing_file)
    
    assert result == existing_file
    assert os.path.exists(existing_file)
    assert not os.path.exists(str(original_file))

def test_rename_across_directories(setup_test_files):
    """Test renaming a file across different directories."""
    original_file = setup_test_files["original_file"]
    new_dir = os.path.join(os.path.dirname(original_file), "new_directory")
    new_path = os.path.join(new_dir, "moved_file.txt")
    
    result = rename_file(str(original_file), new_path)
    
    assert result == new_path
    assert os.path.exists(new_path)
    assert not os.path.exists(str(original_file))

def test_rename_directory():
    """Test attempting to rename a directory."""
    with pytest.raises(IsADirectoryError):
        rename_file(".", "new_directory")