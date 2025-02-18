import os
import pytest
import zipfile

from src.zip_encryption import create_password_protected_zip

def test_create_password_protected_zip(tmp_path):
    # Prepare test files
    file1 = tmp_path / "test1.txt"
    file1.write_text("Test content 1")
    file2 = tmp_path / "test2.txt"
    file2.write_text("Test content 2")
    
    # Output zip path
    output_zip = tmp_path / "encrypted.zip"
    
    # Create password-protected zip
    result = create_password_protected_zip(
        [str(file1), str(file2)], 
        str(output_zip), 
        "SecurePass123"
    )
    
    # Verify zip was created
    assert os.path.exists(output_zip)
    
    # Try to open zip with correct password
    with zipfile.ZipFile(output_zip, 'r') as zipf:
        # Verify files in zip
        assert set(zipf.namelist()) == {'test1.txt', 'test2.txt'}

def test_invalid_input_files():
    with pytest.raises(ValueError, match="At least one input file must be provided"):
        create_password_protected_zip([], "output.zip", "password")

def test_short_password():
    with pytest.raises(ValueError, match="Password must be at least 4 characters long"):
        create_password_protected_zip(["dummy.txt"], "output.zip", "123")

def test_nonexistent_file(tmp_path):
    with pytest.raises(FileNotFoundError):
        create_password_protected_zip(
            [str(tmp_path / "nonexistent.txt")], 
            str(tmp_path / "output.zip"), 
            "password"
        )