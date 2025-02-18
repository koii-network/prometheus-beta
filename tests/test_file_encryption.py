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
    
    # Verify file was encrypted
    encrypted_content = input_file.read_bytes()
    
    # Attempt to decrypt
    fernet = Fernet(key)
    decrypted_content = fernet.decrypt(encrypted_content)
    
    assert decrypted_content.decode() == "Secret message"

def test_encrypt_file_with_output(tmp_path):
    # Create a test file
    input_file = tmp_path / "test_input.txt"
    output_file = tmp_path / "test_output.txt"
    input_file.write_text("Another secret")
    
    # Encrypt the file with a specific output path
    key = encrypt_file(str(input_file), str(output_file))
    
    # Verify file was encrypted
    encrypted_content = output_file.read_bytes()
    
    # Attempt to decrypt
    fernet = Fernet(key)
    decrypted_content = fernet.decrypt(encrypted_content)
    
    assert decrypted_content.decode() == "Another secret"

def test_encrypt_file_with_provided_key(tmp_path):
    # Create a test file
    input_file = tmp_path / "test_input.txt"
    input_file.write_text("Third secret")
    
    # Create a specific key
    key = Fernet.generate_key()
    
    # Encrypt the file with the provided key
    returned_key = encrypt_file(str(input_file), key=key)
    
    # Verify returned key matches provided key
    assert returned_key == key
    
    # Verify file can be decrypted
    encrypted_content = input_file.read_bytes()
    fernet = Fernet(key)
    decrypted_content = fernet.decrypt(encrypted_content)
    
    assert decrypted_content.decode() == "Third secret"

def test_encrypt_nonexistent_file(tmp_path):
    # Try to encrypt a nonexistent file
    with pytest.raises(FileNotFoundError):
        encrypt_file(str(tmp_path / "nonexistent.txt"))

def test_encrypt_empty_file(tmp_path):
    # Create an empty file
    input_file = tmp_path / "empty.txt"
    input_file.write_text("")
    
    # Encrypt the empty file
    key = encrypt_file(str(input_file))
    
    # Verify file was encrypted
    encrypted_content = input_file.read_bytes()
    
    # Attempt to decrypt
    fernet = Fernet(key)
    decrypted_content = fernet.decrypt(encrypted_content)
    
    assert decrypted_content.decode() == ""