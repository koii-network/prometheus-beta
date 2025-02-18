import os
import pytest
import tarfile
import tempfile
import shutil

from src.tar_extractor import extract_tar_archive

def create_test_tar(file_contents):
    """Helper function to create a test tar archive"""
    temp_dir = tempfile.mkdtemp()
    tar_path = os.path.join(temp_dir, 'test.tar')
    
    with tarfile.open(tar_path, 'w') as tar:
        for filename, content in file_contents.items():
            # Create a temporary file with content
            temp_file_path = os.path.join(temp_dir, filename)
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
            
            with open(temp_file_path, 'w') as f:
                f.write(content)
            
            # Add file to tar
            tar.add(temp_file_path, arcname=filename)
    
    return tar_path, temp_dir

def test_extract_tar_archive_default_path():
    """Test extracting tar archive to default path"""
    file_contents = {
        'file1.txt': 'Hello World',
        'file2.txt': 'Test Content'
    }
    
    tar_path, temp_dir = create_test_tar(file_contents)
    
    try:
        # Extract to default path (same as tar file location)
        extracted_files = extract_tar_archive(tar_path)
        
        # Verify extracted files exist and have correct content
        assert len(extracted_files) == 2
        
        for filename in ['file1.txt', 'file2.txt']:
            full_path = os.path.join(os.path.dirname(tar_path), filename)
            assert os.path.exists(full_path)
            
            with open(full_path, 'r') as f:
                expected_content = file_contents[filename]
                assert f.read() == expected_content
    
    finally:
        # Clean up
        shutil.rmtree(os.path.dirname(tar_path))

def test_extract_tar_archive_custom_path():
    """Test extracting tar archive to custom path"""
    file_contents = {
        'file1.txt': 'Custom Path Test',
        'subdir/file2.txt': 'Nested File Test'
    }
    
    tar_path, temp_dir = create_test_tar(file_contents)
    
    try:
        # Create a custom extraction path
        custom_extract_path = os.path.join(temp_dir, 'extract')
        os.makedirs(custom_extract_path)
        
        # Extract to custom path
        extracted_files = extract_tar_archive(tar_path, custom_extract_path)
        
        # Verify extracted files exist and have correct content
        assert len(extracted_files) == 2
        
        for filename in ['file1.txt', 'subdir/file2.txt']:
            full_path = os.path.join(custom_extract_path, filename)
            assert os.path.exists(full_path)
    
    finally:
        # Clean up
        shutil.rmtree(temp_dir)

def test_extract_nonexistent_tar():
    """Test extracting a nonexistent tar file"""
    with pytest.raises(FileNotFoundError):
        extract_tar_archive('/path/to/nonexistent/file.tar')

def test_extract_invalid_tar():
    """Test extracting an invalid tar file"""
    # Create an invalid tar file
    temp_dir = tempfile.mkdtemp()
    invalid_tar_path = os.path.join(temp_dir, 'invalid.tar')
    
    try:
        # Create an invalid tar file
        with open(invalid_tar_path, 'w') as f:
            f.write('This is not a valid tar archive')
        
        with pytest.raises(ValueError):
            extract_tar_archive(invalid_tar_path)
    
    finally:
        # Clean up
        shutil.rmtree(temp_dir)