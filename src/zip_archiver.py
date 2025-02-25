import os
import zipfile
from typing import List, Union


def create_zip_archive(files: List[str], output_path: str) -> bool:
    """
    Create a zip archive containing multiple files.

    Args:
        files (List[str]): List of file paths to be included in the zip archive.
        output_path (str): Path where the zip archive will be created.

    Returns:
        bool: True if the zip archive was created successfully, False otherwise.

    Raises:
        ValueError: If no files are provided or output path is invalid.
        FileNotFoundError: If any of the input files do not exist.
    """
    # Validate input
    if not files:
        raise ValueError("At least one file must be provided to create a zip archive.")
    
    # Validate output path
    if not output_path.lower().endswith('.zip'):
        output_path += '.zip'
    
    # Check if all files exist
    for file in files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"File not found: {file}")
    
    try:
        # Create zip archive
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                # Use the basename to preserve original filename in the archive
                zipf.write(file, os.path.basename(file))
        
        return True
    except Exception as e:
        # Log or handle any unexpected errors during zip creation
        print(f"Error creating zip archive: {e}")
        return False