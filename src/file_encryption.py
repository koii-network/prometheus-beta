from cryptography.fernet import Fernet
import os

def encrypt_file(input_file_path, output_file_path=None, key=None):
    """
    Encrypt the contents of a file using Fernet symmetric encryption.
    
    Args:
        input_file_path (str): Path to the input file to be encrypted.
        output_file_path (str, optional): Path to save the encrypted file. 
                                          If not provided, appends '.encrypted' to input file.
        key (bytes, optional): Encryption key. If not provided, a new key is generated.
    
    Returns:
        bytes: The encryption key
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If file cannot be read or written
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    # Generate or use provided key
    if key is None:
        key = Fernet.generate_key()
    
    # Create Fernet cipher
    fernet = Fernet(key)
    
    # Determine output file path
    if output_file_path is None:
        output_file_path = input_file_path + '.encrypted'
    
    try:
        # Read input file
        with open(input_file_path, 'rb') as file:
            file_data = file.read()
        
        # Encrypt data
        encrypted_data = fernet.encrypt(file_data)
        
        # Write encrypted data
        with open(output_file_path, 'wb') as file:
            file.write(encrypted_data)
        
        return key
    
    except PermissionError:
        raise PermissionError(f"Cannot read or write files: {input_file_path}, {output_file_path}")