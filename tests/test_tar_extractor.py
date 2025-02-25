import os
import pytest
import tarfile
import tempfile
import shutil

from src.tar_extractor import extract_tar_archive

@pytest.fixture
def sample_tar_archive():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    
    # Create a sample tar archive
    archive_path = os.path.join(temp_dir, 'sample.tar')
    with tarfile.open(archive_path, 'w') as tar:
        # Create some sample files
        files = [
            ('file1.txt', b'content of file 1'),
            ('file2.txt', b'content of file 2'),
            ('subdir/file3.txt', b'content of file 3')
        ]
        
        for filename, content in files:
            # Create a temporary file with content
            temp_file_path = os.path.join(temp_dir, filename)
            os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
            with open(temp_file_path, 'wb') as f:
                f.write(content)
            
            # Add file to tar archive
            tar.add(temp_file_path, arcname=filename)
    
    yield archive_path
    
    # Cleanup
    shutil.rmtree(temp_dir)

def test_extract_all_files(sample_tar_archive):
    """Test extracting all files from a tar archive."""
    with tempfile.TemporaryDirectory() as extract_dir:
        extracted_files = extract_tar_archive(sample_tar_archive, extract_path=extract_dir)
        
        assert len(extracted_files) == 3
        assert all(os.path.exists(f) for f in extracted_files)
        assert set(os.path.basename(f) for f in extracted_files) == {'file1.txt', 'file2.txt', 'file3.txt'}

def test_extract_specific_files(sample_tar_archive):
    """Test extracting specific files from a tar archive."""
    with tempfile.TemporaryDirectory() as extract_dir:
        extracted_files = extract_tar_archive(
            sample_tar_archive, 
            extract_path=extract_dir, 
            specific_files=['file1.txt', 'subdir/file3.txt']
        )
        
        assert len(extracted_files) == 2
        assert set(os.path.basename(f) for f in extracted_files) == {'file1.txt', 'file3.txt'}

def test_nonexistent_archive():
    """Test that FileNotFoundError is raised for a nonexistent archive."""
    with pytest.raises(FileNotFoundError):
        extract_tar_archive('/path/to/nonexistent/archive.tar')

def test_extract_to_default_path(sample_tar_archive):
    """Test extracting to the default path (same directory as archive)."""
    with tempfile.TemporaryDirectory() as temp_dir:
        archive_path = os.path.join(temp_dir, 'sample.tar')
        shutil.copy(sample_tar_archive, archive_path)
        
        extracted_files = extract_tar_archive(archive_path)
        
        assert len(extracted_files) == 3
        assert all(os.path.exists(f) for f in extracted_files)

def test_nonexistent_specific_file(sample_tar_archive):
    """Test that ValueError is raised when a specific file is not in the archive."""
    with tempfile.TemporaryDirectory() as extract_dir:
        with pytest.raises(ValueError, match="File nonexistent.txt not found in the archive"):
            extract_tar_archive(
                sample_tar_archive, 
                extract_path=extract_dir, 
                specific_files=['nonexistent.txt']
            )