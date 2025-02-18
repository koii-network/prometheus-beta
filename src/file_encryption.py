from cryptography.fernet import Fernet
import os

def encrypt_file(input_file_path, output_file_path=None, key=None):
    """
    Encrypt the contents of a file using Fernet symmetric encryption.
    
    Args:
        input_file_path (str): Path to the input file to be encrypted
        output_file_path (str, optional): Path to save the encrypted file. 
                                          If None, overwrites the input file.
        key (bytes, optional): Encryption key. If None, a new key is generated.
    
    Returns:
        bytes: The encryption key used
    
    Raises:
        FileNotFoundError: If the input file does not exist
        PermissionError: If there are permission issues reading/writing files
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    # Generate or use provided key
    if key is None:
        key = Fernet.generate_key()
    
    # Create Fernet cipher
    fernet = Fernet(key)
    
    # Read input file
    try:
        with open(input_file_path, 'rb') as file:
            file_data = file.read()
    except PermissionError:
        raise PermissionError(f"Permission denied when reading file: {input_file_path}")
    
    # Encrypt file contents
    encrypted_data = fernet.encrypt(file_data)
    
    # Determine output file path
    if output_file_path is None:
        output_file_path = input_file_path
    
    # Write encrypted data
    try:
        with open(output_file_path, 'wb') as file:
            file.write(encrypted_data)
    except PermissionError:
        raise PermissionError(f"Permission denied when writing to file: {output_file_path}")
    
    return key