import os
import pytest
from cryptography.fernet import Fernet
import tempfile
import shutil

from src.file_decryption import decrypt_file

class TestFileDecryption:
    @pytest.fixture
    def setup_encrypted_file(self):
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()
        
        try:
            # Generate a key
            key = Fernet.generate_key()
            key_path = os.path.join(temp_dir, 'test.key')
            with open(key_path, 'wb') as key_file:
                key_file.write(key)
            
            # Create a test file to encrypt
            original_content = b"This is a secret message!"
            input_file_path = os.path.join(temp_dir, 'input.txt')
            with open(input_file_path, 'wb') as input_file:
                input_file.write(original_content)
            
            # Encrypt the file
            f = Fernet(key)
            encrypted_content = f.encrypt(original_content)
            encrypted_file_path = os.path.join(temp_dir, 'encrypted.txt')
            with open(encrypted_file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_content)
            
            yield {
                'temp_dir': temp_dir,
                'key_path': key_path,
                'input_file_path': input_file_path,
                'encrypted_file_path': encrypted_file_path,
                'original_content': original_content
            }
        finally:
            # Cleanup
            shutil.rmtree(temp_dir)
    
    def test_successful_decryption(self, setup_encrypted_file):
        """Test successful file decryption"""
        decrypted_path = decrypt_file(
            setup_encrypted_file['encrypted_file_path'], 
            setup_encrypted_file['key_path']
        )
        
        # Check decrypted file exists
        assert os.path.exists(decrypted_path)
        
        # Check decrypted content
        with open(decrypted_path, 'rb') as decrypted_file:
            decrypted_content = decrypted_file.read()
        
        assert decrypted_content == setup_encrypted_file['original_content']
    
    def test_custom_output_path(self, setup_encrypted_file):
        """Test decryption with custom output path"""
        custom_output = os.path.join(os.path.dirname(setup_encrypted_file['encrypted_file_path']), 
                                     'custom_decrypted.txt')
        
        decrypted_path = decrypt_file(
            setup_encrypted_file['encrypted_file_path'], 
            setup_encrypted_file['key_path'],
            output_path=custom_output
        )
        
        assert decrypted_path == custom_output
        assert os.path.exists(decrypted_path)
    
    def test_nonexistent_encrypted_file(self, setup_encrypted_file):
        """Test error when encrypted file does not exist"""
        with pytest.raises(FileNotFoundError):
            decrypt_file('/path/to/nonexistent/file', setup_encrypted_file['key_path'])
    
    def test_nonexistent_key_file(self, setup_encrypted_file):
        """Test error when key file does not exist"""
        with pytest.raises(FileNotFoundError):
            decrypt_file(setup_encrypted_file['encrypted_file_path'], '/path/to/nonexistent/key')
    
    def test_invalid_key(self, setup_encrypted_file):
        """Test error with invalid encryption key"""
        # Create an invalid key
        invalid_key_path = os.path.join(os.path.dirname(setup_encrypted_file['key_path']), 'invalid.key')
        with open(invalid_key_path, 'wb') as invalid_key_file:
            invalid_key_file.write(b'invalid_key')
        
        with pytest.raises(ValueError, match="Invalid encryption key"):
            decrypt_file(setup_encrypted_file['encrypted_file_path'], invalid_key_path)