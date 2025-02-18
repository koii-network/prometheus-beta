import os
import zipfile
from typing import List, Union

def create_zip_archive(files: List[str], archive_name: str) -> Union[str, None]:
    """
    Create a zip archive containing specified files.
    
    Args:
        files (List[str]): List of file paths to include in the zip archive
        archive_name (str): Name of the output zip file (should end with .zip)
    
    Returns:
        str: Path to the created zip file, or None if archive creation failed
    
    Raises:
        ValueError: If no files are provided or archive name is invalid
        FileNotFoundError: If any of the specified files do not exist
    """
    # Validate inputs
    if not files:
        raise ValueError("At least one file must be specified for archiving")
    
    if not archive_name.endswith('.zip'):
        archive_name += '.zip'
    
    # Check file existence
    for file_path in files:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
    
    try:
        # Create zip archive
        with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in files:
                # Use the basename to preserve original filename in archive
                zipf.write(file_path, os.path.basename(file_path))
        
        return archive_name
    except Exception as e:
        print(f"Error creating zip archive: {e}")
        return None