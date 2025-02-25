import os
import pytest
import zipfile
import tempfile
import shutil

from src.zip_extractor import extract_zip_files


def create_test_zip(file_contents=None):
    """
    Create a temporary zip file for testing.
    
    Args:
        file_contents (dict, optional): Dictionary of filenames to contents.
    
    Returns:
        str: Path to the created zip file
    """
    # Create a temporary directory and zip file
    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, 'test_archive.zip')
    
    # Default file contents if not provided
    if file_contents is None:
        file_contents = {
            'file1.txt': 'Hello, World!',
            'file2.txt': 'Test content',
            'nested/file3.txt': 'Nested file content'
        }
    
    # Create zip file
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for filename, content in file_contents.items():
            # Ensure nested directories are created
            full_path = os.path.join(temp_dir, filename)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            
            # Write file content
            with open(full_path, 'w') as f:
                f.write(content)
            
            # Add to zip
            zipf.write(full_path, arcname=filename)
    
    return zip_path


def test_extract_zip_files_default_path():
    """
    Test extracting zip files to default (same) directory.
    """
    # Create a test zip file
    zip_path = create_test_zip()
    
    try:
        # Extract files
        extracted_files = extract_zip_files(zip_path)
        
        # Verify extraction
        assert len(extracted_files) == 3
        
        # Check if files exist
        for file_path in extracted_files:
            assert os.path.exists(file_path)
            assert os.path.getsize(file_path) > 0
    finally:
        # Clean up
        shutil.rmtree(os.path.dirname(zip_path))


def test_extract_zip_files_custom_path():
    """
    Test extracting zip files to a custom directory.
    """
    # Create a temporary extraction directory
    extract_dir = tempfile.mkdtemp()
    
    try:
        # Create a test zip file
        zip_path = create_test_zip()
        
        # Extract files to custom directory
        extracted_files = extract_zip_files(zip_path, extract_dir)
        
        # Verify extraction
        assert len(extracted_files) == 3
        
        # Check if files exist in the custom directory
        for file_path in extracted_files:
            assert os.path.exists(file_path)
            assert file_path.startswith(extract_dir)
    finally:
        # Clean up
        shutil.rmtree(os.path.dirname(zip_path))
        shutil.rmtree(extract_dir)


def test_extract_nonexistent_zip():
    """
    Test extracting a non-existent zip file.
    """
    with pytest.raises(FileNotFoundError):
        extract_zip_files('/path/to/nonexistent/file.zip')


def test_extract_invalid_zip():
    """
    Test attempting to extract an invalid zip file.
    """
    # Create a temporary file that's not a zip
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'This is not a zip file')
        temp_file_path = temp_file.name
    
    try:
        with pytest.raises(ValueError):
            extract_zip_files(temp_file_path)
    finally:
        # Clean up
        os.unlink(temp_file_path)