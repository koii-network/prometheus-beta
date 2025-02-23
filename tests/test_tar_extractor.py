import os
import pytest
import tarfile
import tempfile
import shutil

from src.tar_extractor import extract_tar_archive

def create_test_tar(dir_path, filename, files):
    """Helper function to create a test tar archive"""
    tar_path = os.path.join(dir_path, filename)
    mode = 'w:gz' if filename.endswith(('.tar.gz', '.tgz')) else 'w'
    with tarfile.open(tar_path, mode) as tar:
        for file_content in files:
            # Create a temporary file with content
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
                temp_file.write(file_content)
                temp_file.close()
                tar.add(temp_file.name, arcname=os.path.basename(temp_file.name))
                os.unlink(temp_file.name)
    return tar_path

def test_extract_tar_archive_default_path():
    """Test extracting tar to default path"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test tar with sample files
        tar_path = create_test_tar(temp_dir, 'test.tar.gz', ['content1', 'content2'])
        
        # Extract tar
        extracted_files = extract_tar_archive(tar_path)
        
        # Verify extraction
        assert len(extracted_files) == 2
        for file_path in extracted_files:
            assert os.path.exists(file_path)
            assert os.path.dirname(file_path) == temp_dir

def test_extract_tar_archive_custom_path():
    """Test extracting tar to a custom path"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create custom extraction directory
        extract_dir = os.path.join(temp_dir, 'extracted')
        tar_path = create_test_tar(temp_dir, 'test.tar.gz', ['content1', 'content2'])
        
        # Extract tar to custom path
        extracted_files = extract_tar_archive(tar_path, extract_path=extract_dir)
        
        # Verify extraction
        assert len(extracted_files) == 2
        for file_path in extracted_files:
            assert os.path.exists(file_path)
            assert os.path.dirname(file_path) == extract_dir

def test_extract_tar_archive_nonexistent_file():
    """Test attempting to extract a non-existent tar file"""
    with tempfile.TemporaryDirectory() as temp_dir:
        non_existent_tar = os.path.join(temp_dir, 'nonexistent.tar.gz')
        
        with pytest.raises(FileNotFoundError):
            extract_tar_archive(non_existent_tar)

def test_extract_tar_archive_different_formats():
    """Test extracting different tar formats (tar, tar.gz, tgz)"""
    tar_formats = [
        ('test.tar', 'w'),
        ('test.tar.gz', 'w:gz'),
        ('test.tgz', 'w:gz')
    ]
    
    with tempfile.TemporaryDirectory() as temp_dir:
        for filename, mode in tar_formats:
            tar_path = create_test_tar(temp_dir, filename, ['content1'])
            
            # Extract tar
            extracted_files = extract_tar_archive(tar_path)
            
            # Verify extraction
            assert len(extracted_files) == 1