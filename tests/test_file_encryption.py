import os
import pytest
from cryptography.fernet import Fernet
from src.file_encryption import encrypt_file

def test_encrypt_file_default():
    # Create a test file
    test_content = b"This is a secret message!"
    input_file_path = "tests/test_input.txt"
    
    with open(input_file_path, 'wb') as f:
        f.write(test_content)
    
    try:
        # Encrypt the file
        key, encrypted_file_path = encrypt_file(input_file_path)
        
        # Verify the encrypted file exists
        assert os.path.exists(encrypted_file_path)
        assert encrypted_file_path.endswith('.encrypted')
        
        # Verify the file is not the same as the original
        with open(encrypted_file_path, 'rb') as f:
            encrypted_content = f.read()
        
        assert encrypted_content != test_content
        
        # Verify decryption works
        fernet = Fernet(key)
        decrypted_content = fernet.decrypt(encrypted_content)
        assert decrypted_content == test_content
    
    finally:
        # Clean up test files
        if os.path.exists(input_file_path):
            os.remove(input_file_path)
        if os.path.exists(encrypted_file_path):
            os.remove(encrypted_file_path)

def test_encrypt_file_with_custom_output():
    # Create a test file
    test_content = b"Another secret message!"
    input_file_path = "tests/test_input.txt"
    output_file_path = "tests/encrypted_output.bin"
    
    with open(input_file_path, 'wb') as f:
        f.write(test_content)
    
    try:
        # Encrypt the file with custom output path
        key, encrypted_file_path = encrypt_file(input_file_path, output_file_path)
        
        # Verify the encrypted file exists at the specified path
        assert encrypted_file_path == output_file_path
        assert os.path.exists(encrypted_file_path)
        
        # Verify decryption works
        fernet = Fernet(key)
        with open(encrypted_file_path, 'rb') as f:
            encrypted_content = f.read()
        
        decrypted_content = fernet.decrypt(encrypted_content)
        assert decrypted_content == test_content
    
    finally:
        # Clean up test files
        if os.path.exists(input_file_path):
            os.remove(input_file_path)
        if os.path.exists(output_file_path):
            os.remove(output_file_path)

def test_encrypt_file_nonexistent():
    # Test encrypting a nonexistent file
    with pytest.raises(IOError):
        encrypt_file("nonexistent_file.txt")

def test_encrypt_file_with_custom_key():
    # Create a test file
    test_content = b"Custom key encryption!"
    input_file_path = "tests/test_input.txt"
    
    # Generate a custom key
    custom_key = Fernet.generate_key()
    
    with open(input_file_path, 'wb') as f:
        f.write(test_content)
    
    try:
        # Encrypt the file with custom key
        returned_key, encrypted_file_path = encrypt_file(input_file_path, key=custom_key)
        
        # Verify the returned key matches the custom key
        assert returned_key == custom_key
        
        # Verify decryption works with the custom key
        fernet = Fernet(custom_key)
        with open(encrypted_file_path, 'rb') as f:
            encrypted_content = f.read()
        
        decrypted_content = fernet.decrypt(encrypted_content)
        assert decrypted_content == test_content
    
    finally:
        # Clean up test files
        if os.path.exists(input_file_path):
            os.remove(input_file_path)
        if os.path.exists(encrypted_file_path):
            os.remove(encrypted_file_path)