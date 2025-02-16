import os
import pytest
from cryptography.fernet import Fernet
import sys
import tempfile

# Add the src directory to the Python path
sys.path.append('src')

from file_encryption import encrypt_file

def test_encrypt_file_default():
    # Create a temporary input file
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_input:
        temp_input.write(b"Test encryption content")
        input_path = temp_input.name
    
    try:
        # Encrypt the file
        key = encrypt_file(input_path)
        
        # Check that encrypted file was created
        encrypted_path = input_path + '.encrypted'
        assert os.path.exists(encrypted_path)
        
        # Try to decrypt and verify content
        fernet = Fernet(key)
        with open(encrypted_path, 'rb') as file:
            decrypted_data = fernet.decrypt(file.read())
        
        assert decrypted_data == b"Test encryption content"
    
    finally:
        # Clean up temporary files
        if os.path.exists(input_path):
            os.unlink(input_path)
        if os.path.exists(input_path + '.encrypted'):
            os.unlink(input_path + '.encrypted')

def test_encrypt_file_custom_output():
    # Create a temporary input file
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_input:
        temp_input.write(b"Custom output test")
        input_path = temp_input.name
    
    # Create a custom output path
    output_path = input_path + '.custom.encrypted'
    
    try:
        # Encrypt the file with custom output path
        key = encrypt_file(input_path, output_path)
        
        # Check that encrypted file was created at the custom path
        assert os.path.exists(output_path)
        
        # Try to decrypt and verify content
        fernet = Fernet(key)
        with open(output_path, 'rb') as file:
            decrypted_data = fernet.decrypt(file.read())
        
        assert decrypted_data == b"Custom output test"
    
    finally:
        # Clean up temporary files
        if os.path.exists(input_path):
            os.unlink(input_path)
        if os.path.exists(output_path):
            os.unlink(output_path)

def test_encrypt_file_with_custom_key():
    # Create a temporary input file
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_input:
        temp_input.write(b"Custom key test")
        input_path = temp_input.name
    
    # Generate a custom key
    custom_key = Fernet.generate_key()
    
    try:
        # Encrypt the file with custom key
        returned_key = encrypt_file(input_path, key=custom_key)
        
        # Check that the returned key matches the custom key
        assert returned_key == custom_key
        
        # Check encrypted file exists
        encrypted_path = input_path + '.encrypted'
        assert os.path.exists(encrypted_path)
        
        # Try to decrypt and verify content
        fernet = Fernet(custom_key)
        with open(encrypted_path, 'rb') as file:
            decrypted_data = fernet.decrypt(file.read())
        
        assert decrypted_data == b"Custom key test"
    
    finally:
        # Clean up temporary files
        if os.path.exists(input_path):
            os.unlink(input_path)
        if os.path.exists(input_path + '.encrypted'):
            os.unlink(input_path + '.encrypted')

def test_encrypt_file_nonexistent_input():
    # Test that FileNotFoundError is raised for non-existent input file
    with pytest.raises(FileNotFoundError):
        encrypt_file('/path/to/nonexistent/file.txt')