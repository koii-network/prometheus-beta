import os
import pytest
from cryptography.fernet import Fernet
from src.file_encryption import encrypt_file

def test_encrypt_file(tmp_path):
    # Create a test file
    test_content = b"Secret message to encrypt!"
    input_file = tmp_path / "test_input.txt"
    input_file.write_bytes(test_content)
    
    # Encrypt the file
    encrypted_file = tmp_path / "test_input.txt.encrypted"
    key = encrypt_file(str(input_file))
    
    # Verify encryption
    assert os.path.exists(str(encrypted_file))
    assert input_file.read_bytes() != encrypted_file.read_bytes()
    
    # Decrypt and verify
    fernet = Fernet(key)
    decrypted_content = fernet.decrypt(encrypted_file.read_bytes())
    assert decrypted_content == test_content

def test_encrypt_file_with_custom_output(tmp_path):
    # Create a test file
    test_content = b"Another secret message!"
    input_file = tmp_path / "test_input.txt"
    input_file.write_bytes(test_content)
    
    # Custom output file
    custom_output = tmp_path / "encrypted_custom.bin"
    key = encrypt_file(str(input_file), str(custom_output))
    
    # Verify encryption
    assert os.path.exists(str(custom_output))
    assert input_file.read_bytes() != custom_output.read_bytes()
    
    # Decrypt and verify
    fernet = Fernet(key)
    decrypted_content = fernet.decrypt(custom_output.read_bytes())
    assert decrypted_content == test_content

def test_encrypt_file_with_preset_key(tmp_path):
    # Create a test file
    test_content = b"Secret with preset key!"
    input_file = tmp_path / "test_input.txt"
    input_file.write_bytes(test_content)
    
    # Preset key
    preset_key = Fernet.generate_key()
    
    # Encrypt with preset key
    encrypted_file = tmp_path / "test_input.txt.encrypted"
    returned_key = encrypt_file(str(input_file), key=preset_key)
    
    # Verify key is the same
    assert returned_key == preset_key
    
    # Verify encryption
    assert os.path.exists(str(encrypted_file))
    assert input_file.read_bytes() != encrypted_file.read_bytes()

def test_encrypt_nonexistent_file(tmp_path):
    # Try to encrypt a non-existent file
    with pytest.raises(FileNotFoundError):
        encrypt_file(str(tmp_path / "nonexistent.txt"))