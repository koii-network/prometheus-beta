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
        with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
            f.write('Test content 1')
        with open(os.path.join(temp_dir, 'file2.txt'), 'w') as f:
            f.write('Test content 2')
        
        # Create a subdirectory
        os.makedirs(os.path.join(temp_dir, 'subdir'))
        with open(os.path.join(temp_dir, 'subdir', 'file3.txt'), 'w') as f:
            f.write('Subdirectory content')
        
        yield temp_dir
    finally:
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)

def test_create_tar_archive_default(sample_directory):
    """Test creating a tar archive with default settings."""
    archive_path = create_tar_archive(sample_directory)
    
    # Verify archive was created
    assert os.path.exists(archive_path)
    assert archive_path.endswith('.tar.gz')
    
    # Verify contents
    with tarfile.open(archive_path, 'r:gz') as tar:
        members = tar.getnames()
        assert 'file1.txt' in members
        assert 'file2.txt' in members
        assert os.path.join('subdir', 'file3.txt') in members

def test_create_tar_archive_bz2_compression(sample_directory):
    """Test creating a tar archive with bz2 compression."""
    archive_path = create_tar_archive(sample_directory, compression='bz2')
    
    # Verify archive was created
    assert os.path.exists(archive_path)
    assert archive_path.endswith('.tar.bz2')
    
    # Verify contents
    with tarfile.open(archive_path, 'r:bz2') as tar:
        members = tar.getnames()
        assert 'file1.txt' in members

def test_create_tar_archive_no_compression(sample_directory):
    """Test creating a tar archive with no compression."""
    archive_path = create_tar_archive(sample_directory, compression=None)
    
    # Verify archive was created
    assert os.path.exists(archive_path)
    assert archive_path.endswith('.tar')
    
    # Verify contents
    with tarfile.open(archive_path, 'r:') as tar:
        members = tar.getnames()
        assert 'file1.txt' in members

def test_create_tar_archive_custom_output(sample_directory):
    """Test creating a tar archive with a custom output path."""
    custom_path = os.path.join(tempfile.gettempdir(), 'custom_archive.tar.gz')
    archive_path = create_tar_archive(sample_directory, output_path=custom_path)
    
    # Verify archive was created at the specified location
    assert os.path.exists(custom_path)
    assert archive_path == custom_path

def test_create_tar_archive_exclusion(sample_directory):
    """Test creating a tar archive with exclusion patterns."""
    archive_path = create_tar_archive(
        sample_directory, 
        exclude_patterns=['file2.txt']
    )
    
    # Verify archive was created
    assert os.path.exists(archive_path)
    
    # Verify contents
    with tarfile.open(archive_path, 'r:gz') as tar:
        members = tar.getnames()
        assert 'file1.txt' in members
        assert 'file2.txt' not in members

def test_create_tar_archive_invalid_source():
    """Test error handling for non-existent or non-directory source."""
    with pytest.raises(ValueError, match="Source directory does not exist"):
        create_tar_archive('/path/to/nonexistent/directory')
    
    with pytest.raises(ValueError, match="Source is not a directory"):
        create_tar_archive(__file__)  # Use this test file as an invalid source

def test_create_tar_archive_invalid_compression(sample_directory):
    """Test error handling for invalid compression type."""
    with pytest.raises(ValueError, match="Unsupported compression type"):
        create_tar_archive(sample_directory, compression='invalid')