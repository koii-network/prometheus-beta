import os
import zipfile
import pytest
from src.zip_archive import create_zip_archive

def test_create_zip_archive_single_file(tmp_path):
    # Prepare a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    os.chdir(tmp_path)
    
    # Create zip archive
    archive_name = create_zip_archive([str(test_file)], "single_file_archive.zip")
    
    # Verify archive
    assert os.path.exists(archive_name)
    with zipfile.ZipFile(archive_name, 'r') as zf:
        assert len(zf.namelist()) == 1
        assert zf.namelist()[0] == test_file.name

def test_create_zip_archive_multiple_files(tmp_path):
    # Prepare test files
    test_files = [
        tmp_path / "test_file1.txt",
        tmp_path / "test_file2.txt"
    ]
    for file in test_files:
        file.write_text("Test content")
    os.chdir(tmp_path)
    
    # Create zip archive
    archive_name = create_zip_archive([str(f) for f in test_files], "multi_file_archive.zip")
    
    # Verify archive
    assert os.path.exists(archive_name)
    with zipfile.ZipFile(archive_name, 'r') as zf:
        assert len(zf.namelist()) == 2
        assert sorted(zf.namelist()) == sorted([f.name for f in test_files])

def test_create_zip_archive_no_files():
    # Test raising ValueError when no files are provided
    with pytest.raises(ValueError, match="At least one file must be specified for archiving"):
        create_zip_archive([], "empty_archive.zip")

def test_create_zip_archive_nonexistent_file(tmp_path):
    # Test raising FileNotFoundError when a file doesn't exist
    os.chdir(tmp_path)
    non_existent_file = str(tmp_path / "nonexistent.txt")
    
    with pytest.raises(FileNotFoundError, match=f"File not found: {non_existent_file}"):
        create_zip_archive([non_existent_file], "archive.zip")

def test_zip_archive_naming(tmp_path):
    # Prepare a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    os.chdir(tmp_path)
    
    # Test archive naming with and without .zip extension
    archive_name1 = create_zip_archive([str(test_file)], "archive1")
    archive_name2 = create_zip_archive([str(test_file)], "archive2.zip")
    
    assert archive_name1.endswith('.zip')
    assert archive_name2.endswith('.zip')
    assert os.path.exists(archive_name1)
    assert os.path.exists(archive_name2)