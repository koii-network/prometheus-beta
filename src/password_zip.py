import zipfile
import os

def create_password_protected_zip(source_files, zip_filename, password):
    """
    Create a password-protected zip file from given source files.

    :param source_files: List of file paths to be zipped
    :param zip_filename: Output zip file name
    :param password: Password to encrypt the zip file
    :return: Path to the created zip file
    :raises ValueError: If source files are invalid or empty
    :raises PermissionError: If files cannot be accessed
    """
    # Validate input
    if not source_files:
        raise ValueError("No source files provided")
    
    # Ensure all source files exist
    for file in source_files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"Source file not found: {file}")
    
    # Ensure zip filename has .zip extension
    if not zip_filename.lower().endswith('.zip'):
        zip_filename += '.zip'
    
    try:
        # Create password-protected zip file
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in source_files:
                # Add each file to the zip with its base name
                zipf.write(file, os.path.basename(file))
            
            # Set password protection
            zipf.setpassword(password.encode())
        
        return zip_filename
    
    except PermissionError:
        raise PermissionError("Permission denied when creating zip file")
    except Exception as e:
        raise RuntimeError(f"Error creating zip file: {str(e)}")