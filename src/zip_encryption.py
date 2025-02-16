import zipfile
import os

def create_password_protected_zip(input_files, output_zip_path, password):
    """
    Create a password-protected zip file from given input files.
    
    :param input_files: List of file paths to be added to the zip
    :param output_zip_path: Path for the output zip file
    :param password: Password to encrypt the zip file
    :raises ValueError: If input files are invalid or password is empty
    :raises FileNotFoundError: If any input file does not exist
    """
    # Validate inputs
    if not input_files:
        raise ValueError("No input files provided")
    
    if not password:
        raise ValueError("Password cannot be empty")
    
    # Check if all input files exist
    for file_path in input_files:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
    
    # Create password-protected zip file
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Set encryption method to ZIP file encryption
        zipf.setpassword(password.encode('utf-8'))
        
        # Add files to the zip
        for file_path in input_files:
            # Add each file to the zip while preserving its base name
            zipf.write(file_path, os.path.basename(file_path))
    
    return output_zip_path