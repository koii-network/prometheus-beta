import os
import pytest
import zipfile
import tempfile
import shutil

from src.zip_protector import create_password_protected_zip

def test_create_password_protected_zip():
    # Setup temporary directory and files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files
        file1_path = os.path.join(temp_dir, 'test1.txt')
        file2_path = os.path.join(temp_dir, 'test2.txt')
        
        with open(file1_path, 'w') as f1, open(file2_path, 'w') as f2:
            f1.write('Test content 1')
            f2.write('Test content 2')
        
        # Output zip path
        output_zip_path = os.path.join(temp_dir, 'protected.zip')
        
        # Create password-protected zip
        result_path = create_password_protected_zip(
            [file1_path, file2_path], 
            output_zip_path, 
            'secretpassword'
        )
        
        # Verify zip was created
        assert os.path.exists(result_path)

def test_invalid_inputs():
    # Test empty source files list
    with pytest.raises(ValueError, match="At least one source file must be provided"):
        create_password_protected_zip([], 'output.zip', 'password')
    
    # Test invalid file type for source_files
    with pytest.raises(TypeError, match="source_files must be a list of file paths"):
        create_password_protected_zip('not a list', 'output.zip', 'password')
    
    # Test invalid output path type
    with pytest.raises(TypeError, match="output_zip_path must be a string"):
        create_password_protected_zip(['file.txt'], 123, 'password')
    
    # Test invalid password type
    with pytest.raises(TypeError, match="password must be a string"):
        create_password_protected_zip(['file.txt'], 'output.zip', 123)
    
    # Test short password
    with pytest.raises(ValueError, match="Password must be at least 4 characters long"):
        create_password_protected_zip(['file.txt'], 'output.zip', '123')

def test_nonexistent_files():
    # Test with nonexistent files
    with pytest.raises(ValueError, match="Invalid files"):
        create_password_protected_zip(['/path/to/nonexistent/file.txt'], 'output.zip', 'password')

def test_extract_with_password():
    # Setup temporary directory and files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files
        file_path = os.path.join(temp_dir, 'test.txt')
        
        with open(file_path, 'w') as f:
            f.write('Test content')
        
        # Output zip path
        output_zip_path = os.path.join(temp_dir, 'protected.zip')
        
        # Create password-protected zip
        create_password_protected_zip([file_path], output_zip_path, 'correctpassword')
        
        # Try extracting with correct password
        extract_dir = os.path.join(temp_dir, 'extracted')
        os.makedirs(extract_dir)
        
        try:
            with zipfile.ZipFile(output_zip_path, 'r') as zf:
                # Attempt to extract
                extracted_file = os.path.join(extract_dir, 'test.txt')
                with open(extracted_file, 'wb') as f:
                    f.write(zf.read('test.txt', pwd=b'correctpassword'))
                
                # Verify extracted content
                with open(extracted_file, 'r') as f:
                    assert f.read() == 'Test content'
        except Exception as e:
            pytest.fail(f"Failed to extract zip with correct password: {e}")