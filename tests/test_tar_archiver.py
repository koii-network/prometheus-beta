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
    """Test creating a tar.gz archive with default settings."""
    archive_path = create_tar_archive(sample_directory)
    
    # Verify archive was created
    assert os.path.exists(archive_path)
    assert archive_path.endswith('.tar.gz')
    
    # Verify contents
    with tarfile.open(archive_path, 'r:gz') as tar:
        members = tar.getnames()
        base_dir = os.path.basename(sample_directory)
        assert base_dir in members
        assert f"{base_dir}/file1.txt" in members
        assert f"{base_dir}/file2.txt" in members
        assert f"{base_dir}/subdir/file3.txt" in members


def test_create_tar_archive_custom_output(sample_directory):
    """Test creating a tar archive with a custom output path."""
    custom_output = os.path.join(tempfile.gettempdir(), 'custom_archive.tar.bz2')
    archive_path = create_tar_archive(sample_directory, 
                                      output_path=custom_output, 
                                      compression='bz2')
    
    # Verify archive was created at specified path
    assert os.path.exists(custom_output)
    assert archive_path == custom_output
    
    # Verify contents
    with tarfile.open(custom_output, 'r:bz2') as tar:
        members = tar.getnames()
        base_dir = os.path.basename(sample_directory)
        assert base_dir in members


def test_create_tar_archive_uncompressed(sample_directory):
    """Test creating an uncompressed tar archive."""
    archive_path = create_tar_archive(sample_directory, compression=None)
    
    # Verify archive was created
    assert os.path.exists(archive_path)
    assert archive_path.endswith('.tar')
    
    # Verify contents
    with tarfile.open(archive_path, 'r:') as tar:
        members = tar.getnames()
        base_dir = os.path.basename(sample_directory)
        assert base_dir in members


def test_create_tar_archive_invalid_directory():
    """Test error handling for non-existent or non-directory path."""
    with pytest.raises(ValueError, match="Source directory does not exist"):
        create_tar_archive('/path/to/nonexistent/directory')
    
    with pytest.raises(ValueError, match="Source path is not a directory"):
        # Create a temporary file instead of a directory
        with tempfile.NamedTemporaryFile() as temp_file:
            create_tar_archive(temp_file.name)


def test_create_tar_archive_invalid_compression(sample_directory):
    """Test error handling for invalid compression type."""
    with pytest.raises(ValueError, match="Invalid compression type"):
        create_tar_archive(sample_directory, compression='invalid')