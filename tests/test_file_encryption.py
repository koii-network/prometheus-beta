import os
import pytest
from cryptography.fernet import Fernet
from src.file_encryption import encrypt_file

@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file for testing"""
    sample_content = b"This is a test file for encryption"
    test_file = tmp_path / "test_input.txt"
    test_file.write_bytes(sample_content)
    return str(test_file)

def test_encrypt_file_default(sample_file, tmp_path):
    """Test encryption with default parameters"""
    key = encrypt_file(sample_file)
    
    # Check encrypted file exists
    encrypted_file = sample_file + '.encrypted'
    assert os.path.exists(encrypted_file)
    
    # Verify file is encrypted
    with open(encrypted_file, 'rb') as f:
        encrypted_data = f.read()
    
    # Try decrypting
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # Check decrypted content matches original
    with open(sample_file, 'rb') as f:
        original_data = f.read()
    
    assert decrypted_data == original_data

def test_encrypt_file_custom_output(sample_file, tmp_path):
    """Test encryption with custom output file"""
    custom_output = str(tmp_path / "custom_encrypted.txt")
    key = encrypt_file(sample_file, output_file=custom_output)
    
    # Check custom encrypted file exists
    assert os.path.exists(custom_output)
    
    # Verify file is encrypted
    with open(custom_output, 'rb') as f:
        encrypted_data = f.read()
    
    # Try decrypting
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # Check decrypted content matches original
    with open(sample_file, 'rb') as f:
        original_data = f.read()
    
    assert decrypted_data == original_data

def test_encrypt_file_with_custom_key(sample_file, tmp_path):
    """Test encryption with a custom key"""
    custom_key = Fernet.generate_key()
    custom_output = str(tmp_path / "key_encrypted.txt")
    key = encrypt_file(sample_file, output_file=custom_output, key=custom_key)
    
    # Verify returned key matches custom key
    assert key == custom_key
    
    # Verify encryption works with custom key
    fernet = Fernet(key)
    with open(custom_output, 'rb') as f:
        encrypted_data = f.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    with open(sample_file, 'rb') as f:
        original_data = f.read()
    
    assert decrypted_data == original_data

def test_encrypt_nonexistent_file():
    """Test encryption of a nonexistent file raises FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        encrypt_file("/path/to/nonexistent/file.txt")