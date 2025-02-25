import os
import pytest
import zipfile
from src.password_zip import create_password_protected_zip

def test_create_password_protected_zip(tmp_path):
    # Create test files
    test_file1 = tmp_path / "test1.txt"
    test_file2 = tmp_path / "test2.txt"
    test_file1.write_text("Test content 1")
    test_file2.write_text("Test content 2")

    # Prepare zip filename
    zip_path = str(tmp_path / "test_encrypted.zip")
    
    # Create password-protected zip
    result = create_password_protected_zip(
        [str(test_file1), str(test_file2)], 
        zip_path, 
        "secret_password"
    )
    
    # Verify zip file was created
    assert os.path.exists(result)
    assert result == zip_path

    # Verify zip contents with correct password
    with zipfile.ZipFile(result, 'r') as zipf:
        # Try extracting with correct password
        zipf.extractall(pwd=b"secret_password")
        # Check files are in the zip
        assert set(zipf.namelist()) == {"test1.txt", "test2.txt"}

def test_create_zip_without_extension(tmp_path):
    # Create test file
    test_file = tmp_path / "test.txt"
    test_file.write_text("Test content")

    # Prepare zip filename without .zip extension
    zip_path = str(tmp_path / "test_encrypted")
    
    # Create password-protected zip
    result = create_password_protected_zip(
        [str(test_file)], 
        zip_path, 
        "secret_password"
    )
    
    # Verify .zip extension was added
    assert result.endswith('.zip')
    assert os.path.exists(result)

def test_empty_source_files():
    # Verify error when no source files are provided
    with pytest.raises(ValueError, match="No source files provided"):
        create_password_protected_zip([], "test.zip", "password")

def test_nonexistent_source_file(tmp_path):
    # Verify error for nonexistent file
    nonexistent_file = str(tmp_path / "nonexistent.txt")
    
    with pytest.raises(FileNotFoundError, match=f"Source file not found: {nonexistent_file}"):
        create_password_protected_zip([nonexistent_file], "test.zip", "password")

def test_incorrect_password(tmp_path):
    # Create test file
    test_file = tmp_path / "test.txt"
    test_file.write_text("Test content")

    # Create password-protected zip
    zip_path = str(tmp_path / "test_encrypted.zip")
    result = create_password_protected_zip(
        [str(test_file)], 
        zip_path, 
        "correct_password"
    )
    
    # Try extracting with incorrect password
    with zipfile.ZipFile(result, 'r') as zipf:
        with pytest.raises(RuntimeError):
            zipf.extractall(pwd=b"wrong_password")