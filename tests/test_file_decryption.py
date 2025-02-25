import os
import pytest
from cryptography.fernet import Fernet
import tempfile

from src.file_decryption import decrypt_file

@pytest.fixture
def setup_encrypted_file():
    """Create a temporary encrypted file and key for testing."""
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Generate a key
        key = Fernet.generate_key()
        key_path = os.path.join(temp_dir, 'test.key')
        with open(key_path, 'wb') as key_file:
            key_file.write(key)

        # Create a sample file to encrypt
        original_content = b"This is a test file for decryption."
        input_file_path = os.path.join(temp_dir, 'input.txt')
        with open(input_file_path, 'wb') as input_file:
            input_file.write(original_content)

        # Encrypt the file
        cipher = Fernet(key)
        encrypted_content = cipher.encrypt(original_content)
        encrypted_file_path = os.path.join(temp_dir, 'encrypted.txt')
        with open(encrypted_file_path, 'wb') as enc_file:
            enc_file.write(encrypted_content)

        yield {
            'key_path': key_path,
            'input_file_path': input_file_path,
            'encrypted_file_path': encrypted_file_path,
            'original_content': original_content
        }

def test_successful_decryption(setup_encrypted_file):
    """Test successful file decryption."""
    # Arrange
    encrypted_file = setup_encrypted_file['encrypted_file_path']
    key_file = setup_encrypted_file['key_path']
    
    # Act
    decrypted_file_path = decrypt_file(encrypted_file, key_file)
    
    # Assert
    assert os.path.exists(decrypted_file_path)
    with open(decrypted_file_path, 'rb') as dec_file:
        decrypted_content = dec_file.read()
    assert decrypted_content == setup_encrypted_file['original_content']

def test_custom_output_path(setup_encrypted_file):
    """Test decryption with a custom output path."""
    # Arrange
    encrypted_file = setup_encrypted_file['encrypted_file_path']
    key_file = setup_encrypted_file['key_path']
    custom_output = 'temp_decrypted.txt'
    
    # Act
    decrypted_file_path = decrypt_file(encrypted_file, key_file, custom_output)
    
    # Assert
    assert decrypted_file_path == custom_output
    assert os.path.exists(custom_output)
    with open(custom_output, 'rb') as dec_file:
        decrypted_content = dec_file.read()
    assert decrypted_content == setup_encrypted_file['original_content']
    
    # Clean up
    os.remove(custom_output)

def test_nonexistent_encrypted_file():
    """Test handling of nonexistent encrypted file."""
    with pytest.raises(FileNotFoundError):
        decrypt_file('nonexistent_file.txt', 'nonexistent_key.key')

def test_nonexistent_key_file(setup_encrypted_file):
    """Test handling of nonexistent key file."""
    encrypted_file = setup_encrypted_file['encrypted_file_path']
    with pytest.raises(FileNotFoundError):
        decrypt_file(encrypted_file, 'nonexistent_key.key')

def test_invalid_key(setup_encrypted_file):
    """Test handling of invalid encryption key."""
    encrypted_file = setup_encrypted_file['encrypted_file_path']
    # Create an invalid key
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as invalid_key_file:
        invalid_key_file.write(b'invalid_key')
    
    with pytest.raises(ValueError):
        decrypt_file(encrypted_file, invalid_key_file.name)
    
    # Clean up
    os.unlink(invalid_key_file.name)