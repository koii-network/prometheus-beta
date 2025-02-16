import os
from cryptography.fernet import Fernet

def encrypt_file(input_file, output_file=None, key=None):
    """
    Encrypt the contents of a file using Fernet symmetric encryption.
    
    Args:
        input_file (str): Path to the input file to be encrypted
        output_file (str, optional): Path to save the encrypted file. 
                                     If not provided, will use input_file + '.encrypted'
        key (bytes, optional): Encryption key. If not provided, a new key will be generated.
    
    Returns:
        bytes: The encryption key
    
    Raises:
        FileNotFoundError: If the input file does not exist
        PermissionError: If there are permission issues reading/writing files
    """
    # Validate input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist")
    
    # Generate or use provided key
    if key is None:
        key = Fernet.generate_key()
    
    # Create Fernet encryption instance
    fernet = Fernet(key)
    
    # Read file contents
    try:
        with open(input_file, 'rb') as file:
            file_data = file.read()
    except PermissionError:
        raise PermissionError(f"Permission denied when reading {input_file}")
    
    # Encrypt file contents
    encrypted_data = fernet.encrypt(file_data)
    
    # Determine output file path
    if output_file is None:
        output_file = input_file + '.encrypted'
    
    # Write encrypted data
    try:
        with open(output_file, 'wb') as file:
            file.write(encrypted_data)
    except PermissionError:
        raise PermissionError(f"Permission denied when writing to {output_file}")
    
    return key