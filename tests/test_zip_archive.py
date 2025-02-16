import os
import pytest
import zipfile
from src.zip_archive import create_zip_archive

def test_create_zip_archive_single_file(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Create zip archive
    archive_path = create_zip_archive([str(test_file)], str(tmp_path / "test_archive.zip"))
    
    # Verify archive was created
    assert archive_path is not None
    assert os.path.exists(archive_path)
    
    # Verify contents of the archive
    with zipfile.ZipFile(archive_path, 'r') as zipf:
        assert len(zipf.namelist()) == 1
        assert zipf.namelist()[0] == "test_file.txt"

def test_create_zip_archive_multiple_files(tmp_path):
    # Create test files
    test_file1 = tmp_path / "test_file1.txt"
    test_file1.write_text("Test content 1")
    test_file2 = tmp_path / "test_file2.txt"
    test_file2.write_text("Test content 2")
    
    # Create zip archive
    archive_path = create_zip_archive([str(test_file1), str(test_file2)], str(tmp_path / "multi_file_archive.zip"))
    
    # Verify archive was created
    assert archive_path is not None
    assert os.path.exists(archive_path)
    
    # Verify contents of the archive
    with zipfile.ZipFile(archive_path, 'r') as zipf:
        assert len(zipf.namelist()) == 2
        assert set(zipf.namelist()) == {"test_file1.txt", "test_file2.txt"}

def test_create_zip_archive_no_files():
    # Test creating archive with no files
    result = create_zip_archive([], "empty_archive.zip")
    assert result is None

def test_create_zip_archive_nonexistent_files(tmp_path):
    # Test creating archive with nonexistent files
    with pytest.raises(FileNotFoundError):
        create_zip_archive(["nonexistent_file.txt"], str(tmp_path / "fail_archive.zip"))

def test_create_zip_archive_auto_append_zip_extension(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    
    # Create zip archive without .zip extension
    archive_path = create_zip_archive([str(test_file)], str(tmp_path / "auto_archive"))
    
    # Verify archive was created with .zip extension
    assert archive_path is not None
    assert archive_path.endswith('.zip')
    assert os.path.exists(archive_path)