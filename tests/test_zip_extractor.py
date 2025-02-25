import os
import pytest
import zipfile
import tempfile
from src.zip_extractor import extract_zip_files

def test_extract_zip_files():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test zip file
        zip_path = os.path.join(temp_dir, 'test.zip')
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            # Add some test files to the zip
            zipf.writestr('file1.txt', 'content1')
            zipf.writestr('subfolder/file2.txt', 'content2')
        
        # Extract the zip
        extracted_files = extract_zip_files(zip_path)
        
        # Check extraction results
        assert len(extracted_files) == 2
        assert any('file1.txt' in file for file in extracted_files)
        assert any('subfolder/file2.txt' in file for file in extracted_files)
        
        # Verify file contents
        with open(extracted_files[0], 'r') as f:
            assert f.read() == 'content1'

def test_extract_zip_to_custom_path():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test zip file
        zip_path = os.path.join(temp_dir, 'test.zip')
        custom_extract_path = os.path.join(temp_dir, 'extracted')
        
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.writestr('file1.txt', 'content1')
        
        # Extract to custom path
        extracted_files = extract_zip_files(zip_path, custom_extract_path)
        
        # Check extraction results
        assert len(extracted_files) == 1
        assert extracted_files[0].startswith(custom_extract_path)

def test_nonexistent_zip_file():
    with pytest.raises(FileNotFoundError):
        extract_zip_files('nonexistent.zip')

def test_invalid_zip_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        invalid_zip = os.path.join(temp_dir, 'invalid.zip')
        with open(invalid_zip, 'w') as f:
            f.write('Not a zip file')
        
        with pytest.raises(ValueError):
            extract_zip_files(invalid_zip)