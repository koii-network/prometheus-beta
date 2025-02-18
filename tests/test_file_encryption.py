import os
import pytest
from cryptography.fernet import Fernet
from src.file_encryption import encrypt_file

def test_encrypt_file_default(tmp_path):
    # Create a test file
    input_file = tmp_path / "test_input.txt"
    input_file.write_text("Secret message")
    
    # Encrypt the file
    key = encrypt_file(str(input_file))
    
    # Verify file is encrypted
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    
    # Try to decrypt
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    
    assert decrypted_data.decode() == "Secret message"

def test_encrypt_file_custom_output(tmp_path):
    # Create a test file
    input_file = tmp_path / "test_input.txt"
    input_file.write_text("Another secret")
    output_file = tmp_path / "test_encrypted.txt"
    
    # Encrypt the file with custom output path
    key = encrypt_file(str(input_file), str(output_file))
    
    # Verify file is encrypted
    with open(output_file, 'rb') as f:
        encrypted_data = f.read()
    
    # Try to decrypt
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    
    assert decrypted_data.decode() == "Another secret"

def test_encrypt_file_with_custom_key(tmp_path):
    # Create a test file
    input_file = tmp_path / "test_input.txt"
    input_file.write_text("Custom key encryption")
    
    # Generate a custom key
    custom_key = Fernet.generate_key()
    
    # Encrypt the file with custom key
    returned_key = encrypt_file(str(input_file), key=custom_key)
    
    # Verify key is returned correctly
    assert returned_key == custom_key
    
    # Verify file is encrypted
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    
    # Try to decrypt
    fernet = Fernet(returned_key)
    decrypted_data = fernet.decrypt(encrypted_data)
    
    assert decrypted_data.decode() == "Custom key encryption"

def test_encrypt_nonexistent_file(tmp_path):
    # Try to encrypt a nonexistent file
    with pytest.raises(FileNotFoundError):
        encrypt_file(str(tmp_path / "nonexistent.txt"))