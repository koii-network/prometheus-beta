import os
import tarfile
import pytest
import tempfile
import shutil

from src.tar_extractor import extract_tar_archive

def create_test_tar(files):
    """Helper function to create a test tar archive"""
    temp_dir = tempfile.mkdtemp()
    tar_path = os.path.join(temp_dir, 'test.tar')
    
    with tarfile.open(tar_path, 'w') as tar:
        for filename, content in files.items():
            temp_file_path = os.path.join(temp_dir, filename)
            os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
            with open(temp_file_path, 'w') as f:
                f.write(content)
            tar.add(temp_file_path, arcname=filename)
    
    return tar_path, temp_dir

def test_extract_tar_archive_default_path():
    test_files = {
        'file1.txt': 'Content of file 1',
        'file2.txt': 'Content of file 2'
    }
    tar_path, temp_dir = create_test_tar(test_files)
    
    try:
        extracted_files = extract_tar_archive(tar_path)
        
        # Check number of extracted files
        assert len(extracted_files) == len(test_files)
        
        # Check extracted files exist
        for filename in test_files.keys():
            assert os.path.exists(os.path.join(os.path.dirname(tar_path), filename))
    
    finally:
        shutil.rmtree(temp_dir)

def test_extract_tar_archive_custom_path():
    test_files = {
        'file1.txt': 'Content of file 1',
        'subdir/file2.txt': 'Content of file 2'
    }
    tar_path, temp_dir = create_test_tar(test_files)
    
    extract_dir = tempfile.mkdtemp()
    
    try:
        extracted_files = extract_tar_archive(tar_path, extract_dir)
        
        # Check number of extracted files
        assert len(extracted_files) == len(test_files)
        
        # Check extracted files exist
        for filename in test_files.keys():
            assert os.path.exists(os.path.join(extract_dir, filename))
    
    finally:
        shutil.rmtree(temp_dir)
        shutil.rmtree(extract_dir)

def test_extract_tar_archive_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        extract_tar_archive('/path/to/nonexistent/archive.tar')

def test_extract_tar_archive_corrupted_tar():
    temp_dir = tempfile.mkdtemp()
    corrupted_tar_path = os.path.join(temp_dir, 'corrupted.tar')
    
    try:
        # Create a deliberately corrupted tar file
        with open(corrupted_tar_path, 'wb') as f:
            f.write(b'Corrupted tar content')
        
        with pytest.raises(tarfile.TarError):
            extract_tar_archive(corrupted_tar_path)
    
    finally:
        shutil.rmtree(temp_dir)