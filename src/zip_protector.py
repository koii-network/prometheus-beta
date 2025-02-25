import os
import zipfile

def create_password_protected_zip(source_path, zip_path, password):
    """
    Create a password-protected zip file from a source file or directory.

    Args:
        source_path (str): Path to the file or directory to be zipped
        zip_path (str): Path where the zip file will be created
        password (str): Password to protect the zip file

    Raises:
        ValueError: If source_path does not exist or password is invalid
        TypeError: If inputs are not strings
    """
    # Input validation
    if not isinstance(source_path, str) or not isinstance(zip_path, str) or not isinstance(password, str):
        raise TypeError("All arguments must be strings")
    
    # Check if source path exists
    if not os.path.exists(source_path):
        raise ValueError(f"Source path {source_path} does not exist")
    
    # Validate password
    if not password or len(password) < 4:
        raise ValueError("Password must be at least 4 characters long")
    
    # Ensure zip path has .zip extension
    if not zip_path.lower().endswith('.zip'):
        zip_path += '.zip'
    
    # Create zip file with password protection
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # If source is a directory, walk through and add all files
            if os.path.isdir(source_path):
                for root, _, files in os.walk(source_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        # Calculate relative path within the zip
                        arcname = os.path.relpath(file_path, source_path)
                        zipf.writestr(arcname, open(file_path, 'rb').read(), zipfile.ZIP_DEFLATED)
                        # Set password for each file
                        zipf.setpassword(password.encode())
            # If source is a file, add it directly
            else:
                zipf.writestr(os.path.basename(source_path), 
                              open(source_path, 'rb').read(), 
                              zipfile.ZIP_DEFLATED)
                zipf.setpassword(password.encode())
        
        return zip_path
    except Exception as e:
        raise RuntimeError(f"Error creating zip file: {str(e)}")