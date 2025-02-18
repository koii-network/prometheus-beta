import os
import pytest
import zipfile
import tempfile
from src.zip_encryption import create_password_protected_zip

def test_create_password_protected_zip():
    # Create temporary files and directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files
        file1_path = os.path.join(temp_dir, 'test1.txt')
        file2_path = os.path.join(temp_dir, 'test2.txt')
        
        with open(file1_path, 'w') as f1:
            f1.write('Test content 1')
        
        with open(file2_path, 'w') as f2:
            f2.write('Test content 2')
        
        # Output zip path
        output_zip_path = os.path.join(temp_dir, 'protected.zip')
        
        # Create password-protected zip
        result_path = create_password_protected_zip(
            [file1_path, file2_path], 
            output_zip_path, 
            'secret_password'
        )
        
        # Verify zip was created
        assert os.path.exists(result_path)
        
        # Verify zip can be opened with password
        with zipfile.ZipFile(result_path, 'r') as zf:
            zf.setpassword(b'secret_password')
            assert set(zf.namelist()) == {'test1.txt', 'test2.txt'}

def test_empty_source_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        output_zip_path = os.path.join(temp_dir, 'protected.zip')
        
        with pytest.raises(ValueError, match="At least one source file must be provided"):
            create_password_protected_zip([], output_zip_path, 'secret_password')

def test_empty_password():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test file
        test_file_path = os.path.join(temp_dir, 'test.txt')
        with open(test_file_path, 'w') as f:
            f.write('Test content')
        
        output_zip_path = os.path.join(temp_dir, 'protected.zip')
        
        with pytest.raises(ValueError, match="Password cannot be empty"):
            create_password_protected_zip([test_file_path], output_zip_path, '')

def test_nonexistent_source_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        output_zip_path = os.path.join(temp_dir, 'protected.zip')
        
        with pytest.raises(FileNotFoundError, match="Source file not found"):
            create_password_protected_zip(['/path/to/nonexistent/file.txt'], output_zip_path, 'secret_password')