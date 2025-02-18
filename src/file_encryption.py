import os
from cryptography.fernet import Fernet

def encrypt_file(input_file, output_file=None, key=None):
    """
    Encrypt the contents of a file using Fernet symmetric encryption.
    
    :param input_file: Path to the input file to be encrypted
    :param output_file: Path to save the encrypted file (optional, defaults to input_file + '.encrypted')
    :param key: Encryption key (optional, will generate a new key if not provided)
    :return: The encryption key used
    :raises FileNotFoundError: If input file does not exist
    :raises PermissionError: If there are permission issues with files
    """
    # Validate input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} not found")
    
    # Generate or use provided key
    if key is None:
        key = Fernet.generate_key()
    
    # Create Fernet cipher
    fernet = Fernet(key)
    
    # Determine output file path
    if output_file is None:
        output_file = input_file + '.encrypted'
    
    try:
        # Read input file
        with open(input_file, 'rb') as file:
            file_data = file.read()
        
        # Encrypt file contents
        encrypted_data = fernet.encrypt(file_data)
        
        # Write encrypted data to output file
        with open(output_file, 'wb') as file:
            file.write(encrypted_data)
        
        return key
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing {input_file} or {output_file}")