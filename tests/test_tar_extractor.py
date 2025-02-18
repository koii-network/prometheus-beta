import os
import pytest
import tarfile
import tempfile
import shutil

from src.tar_extractor import extract_tar_archive

def create_sample_tar(tar_path, files_content):
    """Helper function to create a sample tar archive for testing"""
    with tarfile.open(tar_path, 'w:gz') as tar:
        for filename, content in files_content.items():
            # Create a temporary file with content
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
                temp_file.write(content)
                temp_file.close()
            
            # Add the temporary file to the tar archive
            tar.add(temp_file.name, arcname=filename)
            
            # Remove the temporary file
            os.unlink(temp_file.name)

def test_extract_tar_archive_default_path():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a sample tar file
        tar_path = os.path.join(tmpdir, 'sample.tar.gz')
        files_content = {
            'file1.txt': 'Content of file 1',
            'file2.txt': 'Content of file 2'
        }
        create_sample_tar(tar_path, files_content)
        
        # Extract the tar archive
        extracted_files = extract_tar_archive(tar_path)
        
        # Check if files are extracted in the same directory
        assert len(extracted_files) == 2
        for filename in ['file1.txt', 'file2.txt']:
            assert os.path.exists(os.path.join(tmpdir, filename))

def test_extract_tar_archive_custom_path():
    # Create temporary directories
    with tempfile.TemporaryDirectory() as tmpdir, \
         tempfile.TemporaryDirectory() as extract_dir:
        # Create a sample tar file
        tar_path = os.path.join(tmpdir, 'sample.tar.gz')
        files_content = {
            'file1.txt': 'Content of file 1',
            'file2.txt': 'Content of file 2'
        }
        create_sample_tar(tar_path, files_content)
        
        # Extract the tar archive to a custom directory
        extracted_files = extract_tar_archive(tar_path, extract_dir)
        
        # Check if files are extracted in the custom directory
        assert len(extracted_files) == 2
        for filename in ['file1.txt', 'file2.txt']:
            assert os.path.exists(os.path.join(extract_dir, filename))

def test_extract_tar_archive_nonexistent_file():
    # Test attempting to extract a non-existent tar file
    with pytest.raises(FileNotFoundError):
        extract_tar_archive('/path/to/nonexistent/file.tar.gz')

def test_extract_tar_archive_corrupted_tar():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a corrupted tar file
        corrupted_tar_path = os.path.join(tmpdir, 'corrupted.tar.gz')
        with open(corrupted_tar_path, 'wb') as f:
            f.write(b'Invalid tar content')
        
        # Test extracting a corrupted tar file
        with pytest.raises(tarfile.TarError):
            extract_tar_archive(corrupted_tar_path)