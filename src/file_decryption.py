import os
from cryptography.fernet import Fernet

def decrypt_file(encrypted_file_path, key_path, output_path=None):
    """
    Decrypt an encrypted file using a Fernet symmetric encryption key.

    Args:
        encrypted_file_path (str): Path to the encrypted file
        key_path (str): Path to the encryption key file
        output_path (str, optional): Path to save the decrypted file. 
                                    If None, uses the original filename with '.decrypted' appended

    Returns:
        str: Path to the decrypted file

    Raises:
        FileNotFoundError: If encrypted file or key file does not exist
        ValueError: If key is invalid or decryption fails
    """
    # Validate input file exists
    if not os.path.exists(encrypted_file_path):
        raise FileNotFoundError(f"Encrypted file not found: {encrypted_file_path}")
    
    # Validate key file exists
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"Key file not found: {key_path}")
    
    # Read the encryption key
    try:
        with open(key_path, 'rb') as key_file:
            key = key_file.read()
    except IOError as e:
        raise ValueError(f"Error reading key file: {e}")
    
    # Create Fernet cipher
    try:
        f = Fernet(key)
    except Exception:
        raise ValueError("Invalid encryption key")
    
    # Determine output path
    if output_path is None:
        output_path = f"{encrypted_file_path}.decrypted"
    
    # Decrypt the file
    try:
        with open(encrypted_file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
        
        decrypted_data = f.decrypt(encrypted_data)
        
        with open(output_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
        
        return output_path
    except Exception as e:
        raise ValueError(f"Decryption failed: {e}")