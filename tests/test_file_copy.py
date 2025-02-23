import os
import pytest
import shutil
import tempfile

from src.file_copy import copy_file


@pytest.fixture
def temp_source_file():
    """Create a temporary source file for testing."""
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_source:
        temp_source.write("Test file content")
        temp_source.flush()
        yield temp_source.name
    # Cleanup after test
    if os.path.exists(temp_source.name):
        os.unlink(temp_source.name)


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


def test_successful_file_copy(temp_source_file, temp_dir):
    """Test successful file copy."""
    destination_path = os.path.join(temp_dir, 'copied_file.txt')
    result = copy_file(temp_source_file, destination_path)
    
    assert result == destination_path
    assert os.path.exists(destination_path)
    
    # Verify file content is the same
    with open(temp_source_file, 'r') as source, open(destination_path, 'r') as dest:
        assert source.read() == dest.read()


def test_copy_to_existing_directory(temp_source_file, temp_dir):
    """Test copying file to an existing directory."""
    destination_path = os.path.join(temp_dir, 'test_subdir', 'copied_file.txt')
    os.makedirs(os.path.dirname(destination_path))
    
    result = copy_file(temp_source_file, destination_path)
    
    assert result == destination_path
    assert os.path.exists(destination_path)


def test_same_source_and_destination(temp_source_file):
    """Test that copying to the same path raises a ValueError."""
    with pytest.raises(ValueError, match="Source and destination paths cannot be the same"):
        copy_file(temp_source_file, temp_source_file)


def test_nonexistent_source_file():
    """Test that copying a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        copy_file('/path/to/nonexistent/file.txt', '/destination/file.txt')


def test_source_is_directory(temp_dir):
    """Test that trying to copy a directory raises IsADirectoryError."""
    with pytest.raises(IsADirectoryError):
        copy_file(temp_dir, '/destination/file.txt')


def test_invalid_path_types():
    """Test that non-string path inputs raise TypeError."""
    with pytest.raises(TypeError):
        copy_file(123, '/destination/file.txt')
    
    with pytest.raises(TypeError):
        copy_file('/source/file.txt', None)


def test_copy_preserves_metadata(temp_source_file, temp_dir):
    """Test that file metadata (like timestamps) are preserved."""
    # Get source file metadata
    source_stat = os.stat(temp_source_file)
    
    destination_path = os.path.join(temp_dir, 'copied_file.txt')
    copy_file(temp_source_file, destination_path)
    
    # Get destination file metadata
    dest_stat = os.stat(destination_path)
    
    # Verify important metadata is preserved
    assert source_stat.st_mode == dest_stat.st_mode  # File permissions
    assert abs(source_stat.st_mtime - dest_stat.st_mtime) < 1  # Modification time