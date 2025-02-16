import os
import zipfile
from typing import List, Union

def create_zip_archive(files: List[str], archive_name: str) -> Union[str, None]:
    """
    Create a zip archive containing the specified files.

    Args:
        files (List[str]): List of file paths to be included in the zip archive
        archive_name (str): Name of the output zip file (should end with .zip)

    Returns:
        Union[str, None]: Path to the created zip archive or None if creation fails
    """
    try:
        # Validate input files
        if not files:
            return None
        
        # Validate archive name
        if not archive_name.endswith('.zip'):
            archive_name += '.zip'
        
        # Check if files exist
        non_existent_files = [f for f in files if not os.path.exists(f)]
        if non_existent_files:
            raise FileNotFoundError(f"Files not found: {non_existent_files}")
        
        # Create zip archive
        with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                zipf.write(file, os.path.basename(file))
        
        return archive_name
    
    except (IOError, OSError, zipfile.BadZipFile) as e:
        print(f"Error creating zip archive: {e}")
        return None