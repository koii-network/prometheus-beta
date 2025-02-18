import os
import zipfile

def create_password_protected_zip(input_files, output_zip_path, password):
    """
    Create a password-protected zip file from given input files.

    Args:
        input_files (list): List of file paths to be added to the zip
        output_zip_path (str): Path where the encrypted zip will be saved
        password (str): Password to protect the zip file

    Raises:
        ValueError: If input files are invalid or password is too short
        IOError: If there are issues creating or writing to the zip file
    """
    # Validate inputs
    if not input_files:
        raise ValueError("At least one input file must be provided")
    
    if not password or len(password) < 4:
        raise ValueError("Password must be at least 4 characters long")

    # Ensure all input files exist
    for file_path in input_files:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Input file not found: {file_path}")

    try:
        # Create encrypted zip file
        with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add files to the zip
            for file_path in input_files:
                # Use basename to avoid full path in the zip
                arcname = os.path.basename(file_path)
                zipf.write(file_path, arcname=arcname)
            
            # Set password protection
            zipf.setpassword(password.encode('utf-8'))
        
        return output_zip_path
    except Exception as e:
        raise IOError(f"Error creating password-protected zip: {str(e)}")