import os
import pytest
import tarfile
import tempfile
import shutil
import sys
import os

# Add the parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.tar_extractor import extract_tar_archive

@pytest.fixture
def sample_tar_archive():
    """Create a sample tar archive for testing."""
    temp_dir = tempfile.mkdtemp()
    archive_dir = os.path.join(temp_dir, 'test_files')
    os.makedirs(archive_dir)
    
    # Create sample files
    test_files = ['file1.txt', 'file2.txt', 'subdir/file3.txt']
    for file_path in test_files:
        full_path = os.path.join(archive_dir, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(f"Content of {file_path}")
    
    # Create tar archive
    archive_path = os.path.join(temp_dir, 'test_archive.tar')
    with tarfile.open(archive_path, 'w') as tar:
        tar.add(archive_dir, arcname='test_files')
    
    yield archive_path
    
    # Cleanup
    shutil.rmtree(temp_dir)

def test_extract_tar_archive_default_path(sample_tar_archive):
    """Test extracting tar archive to default path."""
    archive_dir = os.path.dirname(sample_tar_archive)
    extracted_files = extract_tar_archive(sample_tar_archive)
    
    assert len(extracted_files) > 0
    for file_path in extracted_files:
        assert os.path.exists(file_path)
        assert file_path.startswith(archive_dir)

def test_extract_tar_archive_custom_path(sample_tar_archive):
    """Test extracting tar archive to a custom path."""
    with tempfile.TemporaryDirectory() as custom_extract_path:
        extracted_files = extract_tar_archive(sample_tar_archive, custom_extract_path)
        
        assert len(extracted_files) > 0
        for file_path in extracted_files:
            assert os.path.exists(file_path)
            assert file_path.startswith(custom_extract_path)

def test_extract_nonexistent_archive():
    """Test extracting a non-existent archive raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        extract_tar_archive('/path/to/nonexistent/archive.tar')

def test_extract_invalid_archive_format():
    """Test extracting an invalid archive format raises ValueError."""
    with tempfile.NamedTemporaryFile(suffix='.zip') as invalid_archive:
        with pytest.raises(ValueError):
            extract_tar_archive(invalid_archive.name)

def test_extract_corrupt_archive(sample_tar_archive):
    """Test handling of a potentially corrupt archive."""
    # Simulate a corrupt archive by truncating the file
    with open(sample_tar_archive, 'r+b') as f:
        f.truncate(len(f.read()) // 2)
    
    with pytest.raises(tarfile.TarError):
        extract_tar_archive(sample_tar_archive)