import zipfile
import os

def create_password_protected_zip(source_files, output_zip_path, password):
    """
    Create a password-protected zip file from given source files.
    
    Args:
        source_files (list): List of file paths to be zipped
        output_zip_path (str): Path for the output zip file
        password (str): Password to encrypt the zip file
    
    Raises:
        ValueError: If source files are invalid or password is empty
        IOError: If there are issues creating the zip file
    """
    # Validate inputs
    if not source_files:
        raise ValueError("At least one source file must be provided")
    
    if not password:
        raise ValueError("Password cannot be empty")
    
    # Ensure all source files exist
    for file_path in source_files:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Source file not found: {file_path}")
    
    # Create password-protected zip file
    try:
        with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in source_files:
                # Add file to zip with encryption
                zipf.writestr(
                    os.path.basename(file_path), 
                    open(file_path, 'rb').read(), 
                    zipfile.ZIP_DEFLATED
                )
                zipf.setpassword(password.encode())
        
        return output_zip_path
    
    except Exception as e:
        raise IOError(f"Error creating password-protected zip: {str(e)}")