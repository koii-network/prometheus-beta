import os
import zipfile
from typing import List, Union

def create_zip_archive(files: List[str], archive_name: str) -> str:
    """
    Create a zip archive containing specified files.
    
    Args:
        files (List[str]): List of file paths to include in the zip archive
        archive_name (str): Name of the output zip archive (including .zip extension)
    
    Returns:
        str: Path to the created zip archive
    
    Raises:
        FileNotFoundError: If any of the specified files do not exist
        ValueError: If no files are provided or archive name is invalid
    """
    # Validate input
    if not files:
        raise ValueError("At least one file must be specified")
    
    if not archive_name.endswith('.zip'):
        raise ValueError("Archive name must end with .zip")
    
    # Check that all files exist
    for file in files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"File not found: {file}")
    
    # Create zip archive
    try:
        with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                # Use basename to preserve file structure in zip
                zipf.write(file, os.path.basename(file))
        
        return archive_name
    except Exception as e:
        raise IOError(f"Error creating zip archive: {str(e)}")