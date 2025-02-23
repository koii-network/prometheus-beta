from cryptography.fernet import Fernet, InvalidToken
import os

def decrypt_file(encrypted_file_path, output_file_path, encryption_key):
    """
    Decrypt an encrypted file using Fernet symmetric encryption.
    
    Args:
        encrypted_file_path (str): Path to the encrypted file
        output_file_path (str): Path where decrypted file will be saved
        encryption_key (bytes): Symmetric encryption key used for decryption
    
    Raises:
        FileNotFoundError: If encrypted file does not exist
        ValueError: If encryption key is invalid
        InvalidToken: If decryption fails due to incorrect key
        PermissionError: If cannot write to output path
    """
    # Validate inputs
    if not os.path.exists(encrypted_file_path):
        raise FileNotFoundError(f"Encrypted file not found: {encrypted_file_path}")
    
    try:
        fernet = Fernet(encryption_key)
    except Exception as e:
        raise ValueError(f"Invalid encryption key: {e}")
    
    try:
        with open(encrypted_file_path, 'rb') as file:
            encrypted_data = file.read()
        
        decrypted_data = fernet.decrypt(encrypted_data)
        
        with open(output_file_path, 'wb') as file:
            file.write(decrypted_data)
    
    except PermissionError:
        raise PermissionError(f"Cannot write to output path: {output_file_path}")
    except InvalidToken:
        raise ValueError("Decryption failed: Invalid encryption key")
    except Exception as e:
        raise RuntimeError(f"Decryption failed: {e}")
    
    return output_file_path