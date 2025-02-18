import os
import pytest
from cryptography.fernet import Fernet
import sys
import tempfile

# Add the src directory to the Python path
sys.path.append('src')

from file_decryption import decrypt_file

@pytest.fixture
def setup_encrypted_file():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a key
        key = Fernet.generate_key()
        key_path = os.path.join(tmpdir, 'encryption.key')
        with open(key_path, 'wb') as key_file:
            key_file.write(key)
        
        # Create an original file
        original_content = b"This is a secret message!"
        original_file_path = os.path.join(tmpdir, 'original.txt')
        with open(original_file_path, 'wb') as orig_file:
            orig_file.write(original_content)
        
        # Encrypt the file
        fernet = Fernet(key)
        encrypted_content = fernet.encrypt(original_content)
        encrypted_file_path = os.path.join(tmpdir, 'encrypted.txt')
        with open(encrypted_file_path, 'wb') as enc_file:
            enc_file.write(encrypted_content)
        
        return {
            'key_path': key_path,
            'encrypted_file_path': encrypted_file_path,
            'original_content': original_content
        }

def test_decrypt_file_success(setup_encrypted_file):
    # Decrypt the file
    decrypted_file_path = decrypt_file(
        setup_encrypted_file['encrypted_file_path'], 
        setup_encrypted_file['key_path']
    )
    
    # Verify the decrypted file exists
    assert os.path.exists(decrypted_file_path)
    
    # Check the content of the decrypted file
    with open(decrypted_file_path, 'rb') as dec_file:
        decrypted_content = dec_file.read()
    
    assert decrypted_content == setup_encrypted_file['original_content']

def test_decrypt_file_custom_output(setup_encrypted_file):
    # Specify a custom output path
    custom_output_path = 'decrypted_custom.txt'
    decrypted_file_path = decrypt_file(
        setup_encrypted_file['encrypted_file_path'], 
        setup_encrypted_file['key_path'],
        custom_output_path
    )
    
    # Verify the decrypted file exists at the custom path
    assert decrypted_file_path == custom_output_path
    assert os.path.exists(decrypted_file_path)

def test_decrypt_file_nonexistent_encrypted_file():
    with pytest.raises(FileNotFoundError):
        decrypt_file('nonexistent_encrypted.txt', 'nonexistent_key.key')

def test_decrypt_file_nonexistent_key(setup_encrypted_file):
    with pytest.raises(FileNotFoundError):
        decrypt_file(
            setup_encrypted_file['encrypted_file_path'], 
            'nonexistent_key.key'
        )

def test_decrypt_file_invalid_key(setup_encrypted_file):
    # Create an invalid key
    invalid_key_path = setup_encrypted_file['key_path'] + '.invalid'
    with open(invalid_key_path, 'wb') as invalid_key_file:
        invalid_key_file.write(b'invalid_key')
    
    with pytest.raises(ValueError):
        decrypt_file(
            setup_encrypted_file['encrypted_file_path'], 
            invalid_key_path
        )