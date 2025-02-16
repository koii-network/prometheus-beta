import os
import zipfile
import pytest
import tempfile
import shutil

from src.zip_extractor import extract_zip_archive

def test_extract_zip_archive():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test zip file
        zip_path = os.path.join(temp_dir, 'test_archive.zip')
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            # Add some test files to the zip
            zipf.writestr('file1.txt', 'Test content 1')
            zipf.writestr('file2.txt', 'Test content 2')
            zipf.writestr('subfolder/file3.txt', 'Test content 3')
        
        # Extract the zip
        extracted_files = extract_zip_archive(zip_path)
        
        # Check extraction
        assert len(extracted_files) == 3
        assert any('file1.txt' in f for f in extracted_files)
        assert any('file2.txt' in f for f in extracted_files)
        assert any('subfolder/file3.txt' in f for f in extracted_files)
        
        # Verify files exist
        for file_path in extracted_files:
            assert os.path.exists(file_path)

def test_extract_zip_to_custom_path():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test zip file
        zip_path = os.path.join(temp_dir, 'test_archive.zip')
        custom_extract_path = os.path.join(temp_dir, 'extracted')
        
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.writestr('file1.txt', 'Test content 1')
        
        # Extract to custom path
        extracted_files = extract_zip_archive(zip_path, extract_path=custom_extract_path)
        
        # Check custom path extraction
        assert len(extracted_files) == 1
        assert extracted_files[0].startswith(custom_extract_path)

def test_nonexistent_zip_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        non_existent_zip = os.path.join(temp_dir, 'non_existent.zip')
        
        # Should raise FileNotFoundError
        with pytest.raises(FileNotFoundError):
            extract_zip_archive(non_existent_zip)

def test_empty_zip_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        empty_zip_path = os.path.join(temp_dir, 'empty.zip')
        
        # Create an empty zip file
        with zipfile.ZipFile(empty_zip_path, 'w'):
            pass
        
        # Extract empty zip
        extracted_files = extract_zip_archive(empty_zip_path)
        
        # Should return an empty list
        assert len(extracted_files) == 0