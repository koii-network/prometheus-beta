import os
import pytest
import tempfile
from cryptography.fernet import Fernet

from src.decryption import decrypt_file

@pytest.fixture
def sample_encrypted_file():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a key
        key = Fernet.generate_key()
        key_path = os.path.join(temp_dir, 'test.key')
        with open(key_path, 'wb') as key_file:
            key_file.write(key)
        
        # Create an original file
        original_text = b"This is a secret message!"
        original_file_path = os.path.join(temp_dir, 'original.txt')
        with open(original_file_path, 'wb') as orig_file:
            orig_file.write(original_text)
        
        # Encrypt the file
        cipher_suite = Fernet(key)
        encrypted_text = cipher_suite.encrypt(original_text)
        encrypted_file_path = os.path.join(temp_dir, 'encrypted.txt')
        with open(encrypted_file_path, 'wb') as enc_file:
            enc_file.write(encrypted_text)
        
        return {
            'key_path': key_path,
            'encrypted_file_path': encrypted_file_path,
            'original_text': original_text
        }

def test_decrypt_file_successful(sample_encrypted_file):
    # Decrypt the file
    decrypted_file_path = decrypt_file(
        sample_encrypted_file['encrypted_file_path'], 
        sample_encrypted_file['key_path']
    )
    
    # Verify the decrypted file exists
    assert os.path.exists(decrypted_file_path)
    
    # Check the content
    with open(decrypted_file_path, 'rb') as dec_file:
        decrypted_text = dec_file.read()
    
    assert decrypted_text == sample_encrypted_file['original_text']

def test_decrypt_file_custom_output_path(sample_encrypted_file):
    # Create a custom output path
    custom_output_path = '/tmp/custom_decrypted.txt'
    
    # Decrypt the file to a custom path
    decrypted_file_path = decrypt_file(
        sample_encrypted_file['encrypted_file_path'], 
        sample_encrypted_file['key_path'],
        custom_output_path
    )
    
    # Verify the custom path was used
    assert decrypted_file_path == custom_output_path
    
    # Check the content
    with open(decrypted_file_path, 'rb') as dec_file:
        decrypted_text = dec_file.read()
    
    assert decrypted_text == sample_encrypted_file['original_text']

def test_decrypt_file_nonexistent_encrypted_file():
    with pytest.raises(FileNotFoundError):
        decrypt_file('/path/to/nonexistent/encrypted.txt', '/path/to/key.key')

def test_decrypt_file_nonexistent_key():
    with pytest.raises(FileNotFoundError):
        # Create a temporary encrypted file
        with tempfile.NamedTemporaryFile(delete=False) as temp_enc_file:
            temp_enc_file.write(b'some encrypted data')
            encrypted_file_path = temp_enc_file.name
        
        try:
            decrypt_file(encrypted_file_path, '/path/to/nonexistent/key.key')
        finally:
            # Clean up
            os.unlink(encrypted_file_path)