import os
import zipfile
from typing import List, Union

def create_zip_archive(files: List[str], output_path: str) -> bool:
    """
    Create a zip archive containing the specified files.

    Args:
        files (List[str]): List of file paths to be added to the zip archive
        output_path (str): Path where the zip archive will be created

    Returns:
        bool: True if zip archive creation was successful, False otherwise
    
    Raises:
        ValueError: If no files are provided or output path is invalid
        FileNotFoundError: If any of the source files do not exist
    """
    # Validate input
    if not files:
        raise ValueError("At least one file must be provided")
    
    if not output_path:
        raise ValueError("Output path must be specified")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    try:
        # Create the zip archive
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in files:
                # Check if file exists
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"File not found: {file_path}")
                
                # Add file to zip, preserving directory structure relative to current directory
                zipf.write(file_path, arcname=os.path.basename(file_path))
        
        return True
    except Exception as e:
        print(f"Error creating zip archive: {e}")
        return False