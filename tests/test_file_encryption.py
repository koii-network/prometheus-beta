import os
import pytest
from cryptography.fernet import Fernet
from src.file_encryption import encrypt_file

def test_encrypt_file_default(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Secret message")
    
    # Encrypt the file
    key = encrypt_file(str(test_file))
    
    # Check encrypted file was created
    encrypted_file = str(test_file) + '.encrypted'
    assert os.path.exists(encrypted_file)
    
    # Verify the file is encrypted
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()
    
    # Try to decrypt
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    
    assert decrypted_data.decode() == "Secret message"

def test_encrypt_file_custom_output(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Another secret message")
    
    # Custom output file
    output_file = tmp_path / "custom_encrypted.bin"
    
    # Encrypt the file
    key = encrypt_file(str(test_file), str(output_file))
    
    # Check encrypted file was created
    assert os.path.exists(str(output_file))
    
    # Verify the file is encrypted
    with open(str(output_file), 'rb') as f:
        encrypted_data = f.read()
    
    # Try to decrypt
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    
    assert decrypted_data.decode() == "Another secret message"

def test_encrypt_file_with_custom_key(tmp_path):
    # Create a test file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Custom key encryption")
    
    # Generate a custom key
    custom_key = Fernet.generate_key()
    
    # Encrypt the file with custom key
    returned_key = encrypt_file(str(test_file), key=custom_key)
    
    # Check encrypted file was created
    encrypted_file = str(test_file) + '.encrypted'
    assert os.path.exists(encrypted_file)
    
    # Verify the returned key matches the input key
    assert returned_key == custom_key
    
    # Verify decryption works
    fernet = Fernet(custom_key)
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    
    assert decrypted_data.decode() == "Custom key encryption"

def test_encrypt_nonexistent_file():
    # Try to encrypt a file that doesn't exist
    with pytest.raises(FileNotFoundError):
        encrypt_file("/path/to/nonexistent/file.txt")

def test_encrypt_empty_file(tmp_path):
    # Create an empty test file
    test_file = tmp_path / "empty_file.txt"
    test_file.write_text("")
    
    # Encrypt the empty file
    key = encrypt_file(str(test_file))
    
    # Check encrypted file was created
    encrypted_file = str(test_file) + '.encrypted'
    assert os.path.exists(encrypted_file)
    
    # Verify the file can be decrypted
    fernet = Fernet(key)
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    
    assert decrypted_data.decode() == ""