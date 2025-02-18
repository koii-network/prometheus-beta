import os
from cryptography.fernet import Fernet

def decrypt_file(encrypted_file_path, key_path, decrypted_file_path=None):
    """
    Decrypt an encrypted file using a provided key.
    
    Args:
        encrypted_file_path (str): Path to the encrypted file
        key_path (str): Path to the encryption key file
        decrypted_file_path (str, optional): Path to save the decrypted file. 
                                             If None, uses the original filename with '.decrypted' appended
    
    Returns:
        str: Path to the decrypted file
    
    Raises:
        FileNotFoundError: If encrypted file or key file doesn't exist
        ValueError: If key is invalid or decryption fails
    """
    # Validate input file paths exist
    if not os.path.exists(encrypted_file_path):
        raise FileNotFoundError(f"Encrypted file not found: {encrypted_file_path}")
    
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"Key file not found: {key_path}")
    
    # Read the encryption key
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
    
    # Create Fernet cipher suite
    try:
        cipher_suite = Fernet(key)
    except ValueError:
        raise ValueError("Invalid encryption key")
    
    # Read encrypted file
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    # Decrypt the file
    try:
        decrypted_data = cipher_suite.decrypt(encrypted_data)
    except Exception as e:
        raise ValueError(f"Decryption failed: {str(e)}")
    
    # Determine decrypted file path
    if decrypted_file_path is None:
        decrypted_file_path = encrypted_file_path + '.decrypted'
    
    # Write decrypted data to file
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    
    return decrypted_file_path