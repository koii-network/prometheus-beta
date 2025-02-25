from cryptography.fernet import Fernet
import os

def generate_key():
    """
    Generate a new encryption key.
    
    Returns:
        bytes: A new Fernet encryption key.
    """
    return Fernet.generate_key()

def encrypt_file(input_path, output_path, key):
    """
    Encrypt the contents of a file.
    
    Args:
        input_path (str): Path to the input file to be encrypted.
        output_path (str): Path where the encrypted file will be saved.
        key (bytes): Encryption key used for encryption.
    
    Raises:
        FileNotFoundError: If the input file does not exist.
        PermissionError: If there are permission issues with reading/writing files.
        ValueError: If the key is invalid or empty.
    """
    # Validate inputs
    if not key:
        raise ValueError("Encryption key cannot be empty")
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    try:
        # Create Fernet cipher using the key
        fernet = Fernet(key)
        
        # Read input file
        with open(input_path, 'rb') as file:
            file_data = file.read()
        
        # Encrypt the file data
        encrypted_data = fernet.encrypt(file_data)
        
        # Write encrypted data to output file
        with open(output_path, 'wb') as file:
            file.write(encrypted_data)
        
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files: {input_path}, {output_path}")
    except Exception as e:
        raise RuntimeError(f"Encryption failed: {str(e)}")