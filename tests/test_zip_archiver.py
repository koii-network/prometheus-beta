import os
import zipfile
import pytest
import shutil
import tempfile

from src.zip_archiver import create_zip_archive


@pytest.fixture
def temp_files():
    """Fixture to create temporary files for testing"""
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    
    # Create some test files
    files = [
        os.path.join(temp_dir, 'test1.txt'),
        os.path.join(temp_dir, 'test2.txt')
    ]
    
    for file_path in files:
        with open(file_path, 'w') as f:
            f.write(f"Content for {os.path.basename(file_path)}")
    
    yield files
    
    # Cleanup temporary directory
    shutil.rmtree(temp_dir)


def test_create_zip_archive_success(temp_files):
    """Test successful zip archive creation"""
    output_path = os.path.join(tempfile.gettempdir(), 'test_archive.zip')
    
    # Call the function
    result = create_zip_archive(temp_files, output_path)
    
    # Verify the result
    assert result is True
    assert os.path.exists(output_path)
    
    # Verify zip contents
    with zipfile.ZipFile(output_path, 'r') as zipf:
        assert set(zipf.namelist()) == set(os.path.basename(f) for f in temp_files)
    
    # Clean up the created zip file
    os.remove(output_path)


def test_create_zip_archive_no_files():
    """Test error handling when no files are provided"""
    with pytest.raises(ValueError, match="No files provided"):
        create_zip_archive([], 'output.zip')


def test_create_zip_archive_missing_file(temp_files):
    """Test error handling when a file is missing"""
    # Add a non-existent file to the list
    files_with_missing = temp_files + ['non_existent_file.txt']
    
    with pytest.raises(FileNotFoundError, match="File not found"):
        create_zip_archive(files_with_missing, 'output.zip')


def test_create_zip_archive_auto_extension(temp_files):
    """Test that .zip extension is added automatically if not provided"""
    output_path = os.path.join(tempfile.gettempdir(), 'test_archive')
    
    # Call the function
    result = create_zip_archive(temp_files, output_path)
    
    # Verify the result
    assert result is True
    assert os.path.exists(output_path + '.zip')
    
    # Clean up the created zip file
    os.remove(output_path + '.zip')


def test_create_zip_archive_nested_directory():
    """Test creating zip archive in a nested directory"""
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    nested_dir = os.path.join(temp_dir, 'nested', 'subdirectory')
    os.makedirs(nested_dir, exist_ok=True)
    
    # Create a test file
    test_file = os.path.join(nested_dir, 'test.txt')
    with open(test_file, 'w') as f:
        f.write("Test content")
    
    output_path = os.path.join(temp_dir, 'nested', 'archive')
    
    # Call the function
    result = create_zip_archive([test_file], output_path)
    
    # Verify the result
    assert result is True
    assert os.path.exists(output_path + '.zip')
    
    # Verify zip contents
    with zipfile.ZipFile(output_path + '.zip', 'r') as zipf:
        assert zipf.namelist() == ['test.txt']
    
    # Clean up
    shutil.rmtree(temp_dir)