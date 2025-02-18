import os
import tarfile
import pytest
import shutil
import tempfile

from src.tar_archiver import create_tar_archive

@pytest.fixture
def sample_directory():
    """Create a temporary directory with sample files for testing."""
    temp_dir = tempfile.mkdtemp()
    try:
        # Create some sample files
        os.makedirs(os.path.join(temp_dir, 'subfolder'))
        with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
            f.write('Test content 1')
        with open(os.path.join(temp_dir, 'subfolder', 'file2.txt'), 'w') as f:
            f.write('Test content 2')
        
        yield temp_dir
    finally:
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)

def test_create_tar_archive_default(sample_directory):
    """Test creating a tar archive with default parameters."""
    archive_path = create_tar_archive(sample_directory)
    
    # Verify archive was created
    assert os.path.exists(archive_path)
    assert archive_path.endswith('.tar.gz')
    
    # Verify archive contents
    with tarfile.open(archive_path, 'r:gz') as tar:
        members = tar.getnames()
        assert 'file1.txt' in members
        assert 'subfolder/file2.txt' in members

def test_create_tar_archive_custom_path(sample_directory):
    """Test creating a tar archive with a custom archive path."""
    custom_path = os.path.join(sample_directory, 'custom_archive.tar.gz')
    archive_path = create_tar_archive(sample_directory, archive_path=custom_path)
    
    assert archive_path == custom_path
    assert os.path.exists(archive_path)

def test_create_tar_archive_with_exclusions(sample_directory):
    """Test creating a tar archive with excluded files."""
    archive_path = create_tar_archive(sample_directory, exclude_patterns=['file2'])
    
    with tarfile.open(archive_path, 'r:gz') as tar:
        members = tar.getnames()
        assert 'file1.txt' in members
        assert 'subfolder/file2.txt' not in members

def test_create_tar_archive_nonexistent_directory():
    """Test that an error is raised for a non-existent directory."""
    with pytest.raises(ValueError, match="Source directory does not exist"):
        create_tar_archive('/path/to/nonexistent/directory')