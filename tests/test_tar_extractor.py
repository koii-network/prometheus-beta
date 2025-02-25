import os
import pytest
import tarfile
import tempfile
import shutil
import io


from src.tar_extractor import extract_tar_archive


@pytest.fixture
def sample_tar_archive():
    """Create a sample tar archive for testing."""
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    
    # Create some sample files
    file1_path = os.path.join(temp_dir, 'file1.txt')
    file2_path = os.path.join(temp_dir, 'file2.txt')
    
    with open(file1_path, 'w') as f:
        f.write('Content of file1')
    
    with open(file2_path, 'w') as f:
        f.write('Content of file2')
    
    # Create tar archive
    archive_path = os.path.join(temp_dir, 'sample.tar')
    with tarfile.open(archive_path, 'w') as tar:
        tar.add(file1_path, arcname='file1.txt')
        tar.add(file2_path, arcname='file2.txt')
    
    yield archive_path
    
    # Cleanup
    shutil.rmtree(temp_dir)


def test_extract_all_files(sample_tar_archive):
    """Test extracting all files from a tar archive."""
    with tempfile.TemporaryDirectory() as extract_dir:
        extracted_files = extract_tar_archive(sample_tar_archive, extract_dir)
        
        assert len(extracted_files) == 2
        assert all(os.path.exists(f) for f in extracted_files)
        assert any('file1.txt' in f for f in extracted_files)
        assert any('file2.txt' in f for f in extracted_files)


def test_extract_specific_file(sample_tar_archive):
    """Test extracting a specific file from a tar archive."""
    with tempfile.TemporaryDirectory() as extract_dir:
        extracted_files = extract_tar_archive(sample_tar_archive, extract_dir, 'file1.txt')
        
        assert len(extracted_files) == 1
        assert 'file1.txt' in extracted_files[0]
        assert os.path.exists(extracted_files[0])


def test_extract_multiple_specific_files(sample_tar_archive):
    """Test extracting multiple specific files from a tar archive."""
    with tempfile.TemporaryDirectory() as extract_dir:
        extracted_files = extract_tar_archive(sample_tar_archive, extract_dir, ['file1.txt', 'file2.txt'])
        
        assert len(extracted_files) == 2
        assert any('file1.txt' in f for f in extracted_files)
        assert any('file2.txt' in f for f in extracted_files)


def test_extract_nonexistent_file(sample_tar_archive):
    """Test extracting a non-existent file from a tar archive."""
    with tempfile.TemporaryDirectory() as extract_dir:
        extracted_files = extract_tar_archive(sample_tar_archive, extract_dir, 'nonexistent.txt')
        
        assert len(extracted_files) == 0


def test_extract_to_default_directory(sample_tar_archive):
    """Test extracting to the default directory (archive's directory)."""
    extracted_files = extract_tar_archive(sample_tar_archive)
    
    assert len(extracted_files) == 2
    assert all(os.path.exists(f) for f in extracted_files)


def test_invalid_archive_path():
    """Test extracting from a non-existent archive."""
    with pytest.raises(FileNotFoundError):
        extract_tar_archive('/path/to/nonexistent/archive.tar')


def test_archive_with_directories(sample_tar_archive):
    """Test extracting an archive with nested directories."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create tar archive with directory
        nested_archive_path = os.path.join(temp_dir, 'nested.tar')
        with tarfile.open(nested_archive_path, 'w') as tar:
            # Create a TarInfo object for a file in a subdirectory
            tarinfo = tarfile.TarInfo('subdir/file3.txt')
            content = b'Content of file3'
            tarinfo.size = len(content)
            
            # Use a BytesIO to simulate a file-like object
            file_obj = io.BytesIO(content)
            tar.addfile(tarinfo, fileobj=file_obj)
        
        # Extract and verify
        with tempfile.TemporaryDirectory() as extract_dir:
            extracted_files = extract_tar_archive(nested_archive_path, extract_dir)
            
            assert len(extracted_files) == 1
            assert 'subdir/file3.txt' in extracted_files[0]
            assert os.path.exists(extracted_files[0])