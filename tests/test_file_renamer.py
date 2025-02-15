import os
import pytest
import shutil
from src.file_renamer import rename_file

@pytest.fixture
def temp_file(tmp_path):
    """Create a temporary file for testing."""
    test_file = tmp_path / "original_file.txt"
    test_file.write_text("Test content")
    return test_file

def test_rename_file_success(temp_file, tmp_path):
    """Test successful file renaming."""
    original_path = str(temp_file)
    new_path = str(tmp_path / "renamed_file.txt")
    
    result = rename_file(original_path, new_path)
    assert result is True
    assert os.path.exists(new_path)
    assert not os.path.exists(original_path)

def test_rename_file_nonexistent():
    """Test renaming a file that doesn't exist."""
    with pytest.raises(FileNotFoundError):
        rename_file("nonexistent_file.txt", "new_file.txt")

def test_rename_file_invalid_input():
    """Test renaming with invalid input types."""
    with pytest.raises(TypeError):
        rename_file(123, "new_file.txt")
    with pytest.raises(TypeError):
        rename_file("old_file.txt", 456)

def test_rename_file_directory(tmp_path):
    """Test attempting to rename a directory."""
    with pytest.raises(IsADirectoryError):
        rename_file(str(tmp_path), str(tmp_path / "new_dir"))

def test_rename_file_cross_directory(temp_file, tmp_path):
    """Test renaming a file across different directories."""
    original_path = str(temp_file)
    new_dir = tmp_path / "new_directory"
    new_path = str(new_dir / "renamed_file.txt")
    
    result = rename_file(original_path, new_path)
    assert result is True
    assert os.path.exists(new_path)
    assert not os.path.exists(original_path)