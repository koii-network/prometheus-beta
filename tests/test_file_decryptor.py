import os
import pytest
from cryptography.fernet import Fernet
from src.file_decryptor import decrypt_file

@pytest.fixture
def sample_key():
    """Generate a random encryption key for testing."""
    return Fernet.generate_key()

@pytest.fixture
def encrypted_file(tmp_path, sample_key):
    """Create a sample encrypted file for testing."""
    input_data = b"Secret test data for encryption"
    input_file = tmp_path / "input.txt"
    encrypted_file = tmp_path / "encrypted.bin"
    
    # Encrypt the file
    fernet = Fernet(sample_key)
    input_file.write_bytes(input_data)
    encrypted_data = fernet.encrypt(input_data)
    encrypted_file.write_bytes(encrypted_data)
    
    return {
        'key': sample_key,
        'file_path': str(encrypted_file)
    }

def test_successful_decryption(encrypted_file, tmp_path):
    """Test successful file decryption."""
    output_file = str(tmp_path / "decrypted.txt")
    result = decrypt_file(
        encrypted_file['file_path'], 
        output_file, 
        encrypted_file['key']
    )
    
    assert result == output_file
    assert os.path.exists(output_file)
    
    decrypted_data = open(output_file, 'rb').read()
    assert decrypted_data == b"Secret test data for encryption"

def test_nonexistent_file(sample_key, tmp_path):
    """Test decryption of non-existent file."""
    output_file = str(tmp_path / "output.txt")
    with pytest.raises(FileNotFoundError):
        decrypt_file("/path/to/nonexistent/file.bin", output_file, sample_key)

def test_invalid_key(encrypted_file, tmp_path):
    """Test decryption with invalid key."""
    invalid_key = Fernet.generate_key()
    output_file = str(tmp_path / "output.txt")
    
    with pytest.raises(ValueError):
        decrypt_file(encrypted_file['file_path'], output_file, invalid_key)

def test_permission_denied(encrypted_file, mocker):
    """Test handling of permission errors."""
    output_file = "/root/impossible/path/output.txt"
    
    with pytest.raises(PermissionError):
        decrypt_file(encrypted_file['file_path'], output_file, encrypted_file['key'])