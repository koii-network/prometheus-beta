import os
import pytest
import tarfile
import tempfile
import shutil

from src.tar_extractor import extract_tar_archive

def create_test_tar(filename, files):
    """Helper function to create a test tar archive"""
    with tarfile.open(filename, 'w:gz') as tar:
        for name, content in files.items():
            with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp:
                temp.write(content)
                temp.close()
                tar.add(temp.name, arcname=name)
                os.unlink(temp.name)
    return filename

def test_extract_tar_archive_default_path():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test tar file
        test_files = {
            'file1.txt': 'Hello world',
            'file2.txt': 'Test content'
        }
        tar_path = os.path.join(tmpdir, 'test_archive.tar.gz')
        create_test_tar(tar_path, test_files)

        # Extract tar file
        extracted_files = extract_tar_archive(tar_path)

        # Verify extraction
        assert len(extracted_files) == 2
        assert all(os.path.exists(f) for f in extracted_files)
        assert all(os.path.basename(f) in test_files for f in extracted_files)

def test_extract_tar_archive_custom_path():
    # Create temporary directories
    with tempfile.TemporaryDirectory() as tmpdir, \
         tempfile.TemporaryDirectory() as extractdir:
        # Create test tar file
        test_files = {
            'data/file1.txt': 'Custom path extraction',
            'data/file2.txt': 'Another test file'
        }
        tar_path = os.path.join(tmpdir, 'custom_archive.tar.gz')
        create_test_tar(tar_path, test_files)

        # Extract tar file to custom path
        extracted_files = extract_tar_archive(tar_path, extractdir)

        # Verify extraction
        assert len(extracted_files) == 2
        assert all(f.startswith(extractdir) for f in extracted_files)
        assert all(os.path.exists(f) for f in extracted_files)

def test_extract_nonexistent_tar():
    with pytest.raises(FileNotFoundError):
        extract_tar_archive('/path/to/nonexistent/archive.tar.gz')

def test_extract_corrupt_tar():
    with tempfile.TemporaryDirectory() as tmpdir:
        corrupt_tar = os.path.join(tmpdir, 'corrupt.tar.gz')
        
        # Create a corrupt tar file by writing invalid data
        with open(corrupt_tar, 'wb') as f:
            f.write(b'This is not a valid tar file')

        with pytest.raises(tarfile.TarError):
            extract_tar_archive(corrupt_tar)