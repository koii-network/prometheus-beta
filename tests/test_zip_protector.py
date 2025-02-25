import os
import zipfile
import pytest
import tempfile
import shutil

from src.zip_protector import create_password_protected_zip

def test_create_zip_from_single_file():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write("Test content")
        temp_file_path = temp_file.name
    
    # Create temp output directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Create password-protected zip
        zip_path = create_password_protected_zip(
            temp_file_path, 
            os.path.join(temp_dir, 'test_single.zip'), 
            'strongpassword'
        )
        
        # Verify zip was created
        assert os.path.exists(zip_path)
        
        # Try to open zip with correct password
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(pwd=b'strongpassword')
    finally:
        # Clean up
        os.unlink(temp_file_path)
        shutil.rmtree(temp_dir)

def test_create_zip_from_directory():
    # Create a temporary directory with files
    temp_dir = tempfile.mkdtemp()
    try:
        # Create some files in the temp directory
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        
        with open(file1_path, 'w') as f1:
            f1.write("Content 1")
        
        with open(file2_path, 'w') as f2:
            f2.write("Content 2")
        
        # Create output zip
        output_dir = tempfile.mkdtemp()
        zip_path = create_password_protected_zip(
            temp_dir, 
            os.path.join(output_dir, 'test_dir.zip'), 
            'dirpassword'
        )
        
        # Verify zip was created
        assert os.path.exists(zip_path)
        
        # Extract and verify
        extract_dir = tempfile.mkdtemp()
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(path=extract_dir, pwd=b'dirpassword')
        
        # Check extracted files
        assert os.path.exists(os.path.join(extract_dir, 'file1.txt'))
        assert os.path.exists(os.path.join(extract_dir, 'file2.txt'))
    finally:
        # Clean up
        shutil.rmtree(temp_dir)
        shutil.rmtree(output_dir)
        shutil.rmtree(extract_dir)

def test_invalid_inputs():
    # Test invalid source path
    with pytest.raises(ValueError, match="does not exist"):
        create_password_protected_zip('/nonexistent/path', 'output.zip', 'password')
    
    # Test invalid input types
    with pytest.raises(TypeError):
        create_password_protected_zip(123, 'output.zip', 'password')
    
    # Test short password
    with pytest.raises(ValueError, match="Password must be at least 4 characters long"):
        create_password_protected_zip(__file__, 'output.zip', '123')

def test_zip_path_handling():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write("Test content")
        temp_file_path = temp_file.name
    
    # Create temp output directory
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Create zip without .zip extension
        zip_path = create_password_protected_zip(
            temp_file_path, 
            os.path.join(temp_dir, 'test_auto_extension'), 
            'strongpassword'
        )
        
        # Verify .zip was auto-added
        assert zip_path.lower().endswith('.zip')
    finally:
        # Clean up
        os.unlink(temp_file_path)
        shutil.rmtree(temp_dir)