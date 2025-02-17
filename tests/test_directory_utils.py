import os
import pytest
import shutil
from src.directory_utils import delete_directory

@pytest.fixture
def temp_directory():
    """Create a temporary directory for testing."""
    test_dir = 'test_delete_dir'
    os.makedirs(test_dir, exist_ok=True)
    # Create some files and subdirectories
    with open(os.path.join(test_dir, 'file1.txt'), 'w') as f:
        f.write('test content')
    os.makedirs(os.path.join(test_dir, 'subdir'), exist_ok=True)
    with open(os.path.join(test_dir, 'subdir', 'file2.txt'), 'w') as f:
        f.write('another test content')
    
    yield test_dir
    
    # Cleanup in case the test fails and directory wasn't deleted
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)

def test_delete_directory_success(temp_directory):
    """Test successful deletion of a directory."""
    assert os.path.exists(temp_directory)
    delete_directory(temp_directory)
    assert not os.path.exists(temp_directory)

def test_delete_directory_not_found():
    """Test deleting a non-existent directory raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        delete_directory('non_existent_directory')

def test_delete_directory_not_a_directory(tmp_path):
    """Test attempting to delete a file instead of a directory raises ValueError."""
    file_path = tmp_path / 'test_file.txt'
    file_path.write_text('test')
    
    with pytest.raises(ValueError):
        delete_directory(str(file_path))

# Note: Testing PermissionError is tricky and system-dependent, 
# so we'll omit that for cross-platform compatibility