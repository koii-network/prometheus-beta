import os
import pytest
from cryptography.fernet import Fernet
import sys
import tempfile

# Ensure src directory is in Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from file_encryption import generate_key, encrypt_file

def test_generate_key():
    """Test that a valid key is generated."""
    key = generate_key()
    assert key is not None
    assert isinstance(key, bytes)
    
    # Validate that the key is a valid Fernet key
    try:
        Fernet(key)
    except Exception:
        pytest.fail("Generated key is not a valid Fernet key")

def test_encrypt_file():
    """Test file encryption process."""
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create test input file
        input_path = os.path.join(tmpdir, 'input.txt')
        output_path = os.path.join(tmpdir, 'encrypted.bin')
        
        # Write test content
        test_content = b"This is a test file for encryption."
        with open(input_path, 'wb') as f:
            f.write(test_content)
        
        # Generate encryption key
        key = generate_key()
        
        # Encrypt the file
        encrypt_file(input_path, output_path, key)
        
        # Verify file was created
        assert os.path.exists(output_path)
        
        # Verify encrypted content is different
        with open(output_path, 'rb') as f:
            encrypted_data = f.read()
        
        assert encrypted_data != test_content
        assert len(encrypted_data) > len(test_content)

def test_encrypt_file_not_found():
    """Test encryption fails for non-existent input file."""
    key = generate_key()
    with tempfile.TemporaryDirectory() as tmpdir:
        non_existent_input = os.path.join(tmpdir, 'nonexistent.txt')
        output_path = os.path.join(tmpdir, 'encrypted.bin')
        
        with pytest.raises(FileNotFoundError):
            encrypt_file(non_existent_input, output_path, key)

def test_encrypt_file_empty_key():
    """Test encryption fails with empty key."""
    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, 'input.txt')
        output_path = os.path.join(tmpdir, 'encrypted.bin')
        
        # Create a dummy input file
        with open(input_path, 'wb') as f:
            f.write(b"Test content")
        
        # Test empty key raises ValueError
        with pytest.raises(ValueError):
            encrypt_file(input_path, output_path, b'')