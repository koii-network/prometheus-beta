import os
import pytest
import zipfile
import tempfile
from src.zip_encryption import create_password_protected_zip

def test_create_password_protected_zip():
    # Create temporary files for testing
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create some test files
        test_file1 = os.path.join(tmpdir, 'test1.txt')
        test_file2 = os.path.join(tmpdir, 'test2.txt')
        
        with open(test_file1, 'w') as f:
            f.write('Test content 1')
        
        with open(test_file2, 'w') as f:
            f.write('Test content 2')
        
        # Output zip path
        output_zip = os.path.join(tmpdir, 'encrypted.zip')
        
        # Create password-protected zip
        result = create_password_protected_zip([test_file1, test_file2], output_zip, 'testpassword')
        
        # Verify the zip was created
        assert os.path.exists(output_zip)
        
        # Try to open the zip with correct password
        with zipfile.ZipFile(output_zip, 'r') as zf:
            zf.extractall(path=tmpdir, pwd='testpassword'.encode('utf-8'))
            
            # Verify extracted files
            assert os.path.exists(os.path.join(tmpdir, 'test1.txt'))
            assert os.path.exists(os.path.join(tmpdir, 'test2.txt'))

def test_empty_input_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        output_zip = os.path.join(tmpdir, 'empty.zip')
        
        with pytest.raises(ValueError, match="No input files provided"):
            create_password_protected_zip([], output_zip, 'password')

def test_empty_password():
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = os.path.join(tmpdir, 'test.txt')
        
        with open(test_file, 'w') as f:
            f.write('Test content')
        
        output_zip = os.path.join(tmpdir, 'nopassword.zip')
        
        with pytest.raises(ValueError, match="Password cannot be empty"):
            create_password_protected_zip([test_file], output_zip, '')

def test_nonexistent_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        output_zip = os.path.join(tmpdir, 'nonexistent.zip')
        
        with pytest.raises(FileNotFoundError):
            create_password_protected_zip(['/path/to/nonexistent/file.txt'], output_zip, 'password')