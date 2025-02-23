import os
import pytest
from src.file_size import get_file_size

def test_get_file_size_existing_file(tmp_path):
    """Test getting size of an existing file."""
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Hello, world!")
    assert get_file_size(str(test_file)) == 13

def test_get_file_size_empty_file(tmp_path):
    """Test getting size of an empty file."""
    test_file = tmp_path / "empty_file.txt"
    test_file.touch()
    assert get_file_size(str(test_file)) == 0

def test_get_file_size_nonexistent_file():
    """Test that FileNotFoundError is raised for non-existent file."""
    with pytest.raises(FileNotFoundError):
        get_file_size("nonexistent_file.txt")

def test_get_file_size_directory(tmp_path):
    """Test that IsADirectoryError is raised when path is a directory."""
    with pytest.raises(IsADirectoryError):
        get_file_size(str(tmp_path))

def test_get_file_size_with_spaces(tmp_path):
    """Test file size with filename containing spaces."""
    test_file = tmp_path / "file with spaces.txt"
    test_file.write_text("Test content")
    assert get_file_size(str(test_file)) == 12

def test_get_file_size_unicode_filename(tmp_path):
    """Test file size with unicode filename."""
    test_file = tmp_path / "テスト.txt"
    test_file.write_text("こんにちは")
    assert get_file_size(str(test_file)) == 15  # Length in bytes