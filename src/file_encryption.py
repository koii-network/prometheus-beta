from cryptography.fernet import Fernet
import os

def encrypt_file(input_file_path, output_file_path=None, key=None):
    """
    Encrypt the contents of a file using Fernet symmetric encryption.
    
    :param input_file_path: Path to the input file to be encrypted
    :param output_file_path: Path to save the encrypted file (optional)
    :param key: Encryption key (optional). If not provided, a new key will be generated.
    :return: Tuple containing the encryption key and the path of the encrypted file
    """
    # Generate or use the provided key
    if key is None:
        key = Fernet.generate_key()
    
    # Create Fernet cipher
    fernet = Fernet(key)
    
    # Read the input file
    try:
        with open(input_file_path, 'rb') as file:
            file_data = file.read()
    except IOError as e:
        raise IOError(f"Error reading input file: {e}")
    
    # Encrypt the file contents
    encrypted_data = fernet.encrypt(file_data)
    
    # Determine output file path
    if output_file_path is None:
        # If no output path provided, append .encrypted to the input file name
        output_file_path = input_file_path + '.encrypted'
    
    # Write encrypted data to output file
    try:
        with open(output_file_path, 'wb') as file:
            file.write(encrypted_data)
    except IOError as e:
        raise IOError(f"Error writing encrypted file: {e}")
    
    return key, output_file_path