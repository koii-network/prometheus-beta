import os
import pytest
import tarfile
import tempfile
import shutil

from src.tar_extractor import extract_tar_archive

def create_test_tar(filename, files):
    """Helper function to create a test tar archive."""
    with tarfile.open(filename, 'w:gz') as tar:
        for name, content in files.items():
            # Create a temporary file with content
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(content.encode())
                temp_file.close()
                # Add the file to the tar archive
                tar.add(temp_file.name, arcname=name)
                # Remove the temporary file
                os.unlink(temp_file.name)
    return filename

def test_extract_tar_archive_default_path():
    """Test extracting a tar file to its default directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Change current working directory
        original_dir = os.getcwd()
        os.chdir(tmpdir)
        
        # Create test tar file
        test_files = {
            'file1.txt': 'Hello world',
            'file2.txt': 'Test content'
        }
        tar_path = create_test_tar('test.tar.gz', test_files)
        
        # Extract
        extracted_files = extract_tar_archive(tar_path)
        
        # Verify extraction
        assert len(extracted_files) == 2
        assert any('file1.txt' in f for f in extracted_files)
        assert any('file2.txt' in f for f in extracted_files)
        assert all(os.path.exists(f) for f in extracted_files)
        
        # Change back to original directory
        os.chdir(original_dir)

def test_extract_tar_archive_custom_path():
    """Test extracting a tar file to a custom directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        custom_extract_path = os.path.join(tmpdir, 'extracted')
        
        # Create test tar file
        test_files = {
            'file1.txt': 'Hello world',
            'file2.txt': 'Test content'
        }
        tar_path = create_test_tar(os.path.join(tmpdir, 'test.tar.gz'), test_files)
        
        # Extract
        extracted_files = extract_tar_archive(tar_path, custom_extract_path)
        
        # Verify extraction
        assert len(extracted_files) == 2
        assert any('file1.txt' in f for f in extracted_files)
        assert any('file2.txt' in f for f in extracted_files)
        assert all(os.path.exists(f) for f in extracted_files)
        assert all(f.startswith(custom_extract_path) for f in extracted_files)

def test_extract_invalid_extension():
    """Test that an invalid file extension raises a ValueError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        invalid_tar_path = os.path.join(tmpdir, 'test.zip')
        
        with open(invalid_tar_path, 'w') as f:
            f.write('test')
        
        with pytest.raises(ValueError, match="Invalid tar file extension"):
            extract_tar_archive(invalid_tar_path)

def test_extract_nonexistent_file():
    """Test that a nonexistent file raises a FileNotFoundError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        nonexistent_path = os.path.join(tmpdir, 'nonexistent.tar.gz')
        
        with pytest.raises(FileNotFoundError, match="Tar file not found"):
            extract_tar_archive(nonexistent_path)

def test_extract_corrupt_tar():
    """Test handling of a corrupt tar file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        corrupt_tar_path = os.path.join(tmpdir, 'corrupt.tar.gz')
        
        # Create a corrupt tar file
        with open(corrupt_tar_path, 'wb') as f:
            f.write(b'This is not a valid tar file')
        
        with pytest.raises(ValueError, match="Error extracting tar file"):
            extract_tar_archive(corrupt_tar_path)