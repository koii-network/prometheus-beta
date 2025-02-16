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
    
    # Create sample files
    os.makedirs(os.path.join(temp_dir, 'subdirectory'), exist_ok=True)
    
    with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
        f.write('Hello, world!')
    
    with open(os.path.join(temp_dir, 'subdirectory', 'file2.txt'), 'w') as f:
        f.write('Another file')
    
    yield temp_dir
    
    # Clean up
    shutil.rmtree(temp_dir)

def test_create_tar_archive_basic(sample_directory):
    """Test basic tar archive creation."""
    archive_path = create_tar_archive(sample_directory)
    
    # Verify archive was created
    assert os.path.exists(archive_path)
    
    # Verify archive contents
    with tarfile.open(archive_path, 'r:gz') as tar:
        members = tar.getmembers()
        assert len(members) == 2
        
        # Check file names in archive
        file_names = [m.name for m in members]
        assert 'file1.txt' in file_names
        assert 'subdirectory/file2.txt' in file_names

def test_create_tar_archive_custom_path(sample_directory):
    """Test tar archive creation with custom archive path."""
    custom_path = os.path.join(tempfile.gettempdir(), 'custom_archive.tar.gz')
    archive_path = create_tar_archive(sample_directory, archive_path=custom_path)
    
    assert archive_path == custom_path
    assert os.path.exists(archive_path)

def test_create_tar_archive_exclude_patterns(sample_directory):
    """Test tar archive creation with exclusion patterns."""
    archive_path = create_tar_archive(
        sample_directory, 
        exclude_patterns=['subdirectory']
    )
    
    # Verify archive was created
    assert os.path.exists(archive_path)
    
    # Verify archive contents
    with tarfile.open(archive_path, 'r:gz') as tar:
        members = tar.getmembers()
        assert len(members) == 1
        assert members[0].name == 'file1.txt'

def test_create_tar_archive_nonexistent_directory():
    """Test creating archive from a non-existent directory."""
    with pytest.raises(ValueError, match="Source directory does not exist"):
        create_tar_archive("/path/to/nonexistent/directory")