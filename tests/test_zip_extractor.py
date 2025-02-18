import os
import zipfile
import pytest
import tempfile
from src.zip_extractor import extract_zip_files

def create_test_zip(zip_path, files_content):
    """Helper function to create a test zip file"""
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for filename, content in files_content.items():
            zipf.writestr(filename, content)

def test_extract_zip_files_default_path():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test zip file
        zip_path = os.path.join(temp_dir, 'test.zip')
        create_test_zip(zip_path, {
            'file1.txt': 'Content 1',
            'file2.txt': 'Content 2'
        })

        # Extract files
        extracted_files = extract_zip_files(zip_path)

        # Verify extraction
        assert len(extracted_files) == 2
        assert any('file1.txt' in f for f in extracted_files)
        assert any('file2.txt' in f for f in extracted_files)
        assert all(os.path.exists(f) for f in extracted_files)

def test_extract_zip_files_custom_path():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test zip file
        zip_path = os.path.join(temp_dir, 'test.zip')
        extract_dir = os.path.join(temp_dir, 'extracted')
        create_test_zip(zip_path, {
            'file1.txt': 'Content 1',
            'subdir/file2.txt': 'Content 2'
        })

        # Extract files to custom directory
        extracted_files = extract_zip_files(zip_path, extract_dir)

        # Verify extraction
        assert len(extracted_files) == 2
        assert any('file1.txt' in f for f in extracted_files)
        assert any('file2.txt' in f for f in extracted_files)
        assert all(f.startswith(extract_dir) for f in extracted_files)

def test_extract_zip_files_nonexistent_zip():
    with tempfile.TemporaryDirectory() as temp_dir:
        zip_path = os.path.join(temp_dir, 'nonexistent.zip')
        
        # Should raise FileNotFoundError
        with pytest.raises(FileNotFoundError):
            extract_zip_files(zip_path)

def test_extract_zip_files_nested_structure():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test zip file with nested directory structure
        zip_path = os.path.join(temp_dir, 'nested.zip')
        create_test_zip(zip_path, {
            'dir1/subdir/file1.txt': 'Nested Content 1',
            'dir1/subdir/file2.txt': 'Nested Content 2'
        })

        # Extract files
        extracted_files = extract_zip_files(zip_path)

        # Verify extraction
        assert len(extracted_files) == 2
        assert any('file1.txt' in f for f in extracted_files)
        assert any('file2.txt' in f for f in extracted_files)
        assert all(os.path.exists(f) for f in extracted_files)