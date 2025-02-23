import os
import zipfile

def create_password_protected_zip(source_files, output_zip_path, password):
    """
    Create a password-protected zip file from given source files.

    Args:
        source_files (list): List of file paths to be added to the zip archive
        output_zip_path (str): Path where the encrypted zip file will be saved
        password (str): Password to encrypt the zip file

    Raises:
        ValueError: If source_files is empty or contains invalid paths
        TypeError: If inputs are not of the correct type
        IOError: If there are issues reading source files or creating zip
    """
    # Input validation
    if not isinstance(source_files, list):
        raise TypeError("source_files must be a list of file paths")
    
    if not source_files:
        raise ValueError("At least one source file must be provided")
    
    if not isinstance(output_zip_path, str):
        raise TypeError("output_zip_path must be a string")
    
    if not isinstance(password, str):
        raise TypeError("password must be a string")
    
    if len(password) < 4:
        raise ValueError("Password must be at least 4 characters long")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_zip_path) or '.', exist_ok=True)

    # Validate source files
    invalid_files = [f for f in source_files if not os.path.isfile(f)]
    if invalid_files:
        raise ValueError(f"Invalid files: {invalid_files}")

    # Create encrypted zip file
    try:
        with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in source_files:
                # Encrypt each file individually
                zipf.writestr(
                    os.path.basename(file_path), 
                    open(file_path, 'rb').read(), 
                    zipfile.ZIP_ENCRYPTED
                )
                # Set password for each file
                zipf.setpassword(password.encode())
        
        return output_zip_path
    except Exception as e:
        raise IOError(f"Error creating zip file: {str(e)}")