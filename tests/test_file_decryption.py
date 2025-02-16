import os
import pytest
from cryptography.fernet import Fernet
from src.file_decryption import decrypt_file

@pytest.fixture
def sample_key():
    """Generate a Fernet key for testing"""
    return Fernet.generate_key()

@pytest.fixture
def encrypted_file(tmp_path, sample_key):
    """Create a sample encrypted file for testing"""
    # Create sample file
    original_content = b"This is a secret message!"
    input_file_path = tmp_path / "original.txt"
    encrypted_file_path = tmp_path / "encrypted.bin"
    key_file_path = tmp_path / "key.key"
    
    # Write the key
    with open(key_file_path, 'wb') as key_file:
        key_file.write(sample_key)
    
    # Write original file
    with open(input_file_path, 'wb') as f:
        f.write(original_content)
    
    # Encrypt the file
    fernet = Fernet(sample_key)
    with open(input_file_path, 'rb') as f:
        encrypted_data = fernet.encrypt(f.read())
    
    # Write encrypted file
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_data)
    
    return {
        'original_content': original_content,
        'key_path': str(key_file_path),
        'encrypted_path': str(encrypted_file_path)
    }

def test_decrypt_file_success(encrypted_file, tmp_path):
    """Test successful file decryption"""
    output_path = tmp_path / "decrypted.txt"
    decrypted_file_path = decrypt_file(
        encrypted_file['encrypted_path'], 
        encrypted_file['key_path'], 
        str(output_path)
    )
    
    # Check decrypted file exists
    assert os.path.exists(decrypted_file_path)
    
    # Check decrypted content matches original
    with open(decrypted_file_path, 'rb') as f:
        decrypted_content = f.read()
    
    assert decrypted_content == encrypted_file['original_content']

def test_decrypt_file_default_output(encrypted_file):
    """Test decryption with default output path"""
    decrypted_file_path = decrypt_file(
        encrypted_file['encrypted_path'], 
        encrypted_file['key_path']
    )
    
    # Check default output path (original path + .decrypted)
    assert decrypted_file_path == encrypted_file['encrypted_path'] + '.decrypted'
    
    # Check decrypted content
    with open(decrypted_file_path, 'rb') as f:
        decrypted_content = f.read()
    
    assert decrypted_content == encrypted_file['original_content']

def test_decrypt_file_nonexistent_encrypted_file(encrypted_file, tmp_path):
    """Test decryption with non-existent encrypted file"""
    non_existent_path = str(tmp_path / "non_existent.bin")
    
    with pytest.raises(FileNotFoundError):
        decrypt_file(non_existent_path, encrypted_file['key_path'])

def test_decrypt_file_nonexistent_key(encrypted_file, tmp_path):
    """Test decryption with non-existent key file"""
    non_existent_key_path = str(tmp_path / "non_existent_key.key")
    
    with pytest.raises(FileNotFoundError):
        decrypt_file(encrypted_file['encrypted_path'], non_existent_key_path)

def test_decrypt_file_invalid_key(encrypted_file):
    """Test decryption with invalid key"""
    with pytest.raises(ValueError):
        decrypt_file(encrypted_file['encrypted_path'], encrypted_file['key_path'][:-1] + b'x')