import os
import zipfile
from typing import List, Union

def create_zip_archive(files: List[str], output_path: str) -> bool:
    """
    Create a zip archive containing specified files.
    
    Args:
        files (List[str]): List of file paths to be added to the zip archive
        output_path (str): Path of the output zip file
    
    Returns:
        bool: True if zip archive is created successfully, False otherwise
    
    Raises:
        ValueError: If no files are provided or output path is invalid
        FileNotFoundError: If any of the input files do not exist
    """
    # Validate input
    if not files:
        raise ValueError("No files provided for zip archive")
    
    # Validate output path
    if not output_path.endswith('.zip'):
        output_path += '.zip'
    
    try:
        # Create a ZipFile object
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add each file to the zip archive
            for file_path in files:
                # Check if file exists
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"File not found: {file_path}")
                
                # Add file to zip, preserving directory structure relative to current working directory
                zipf.write(file_path, arcname=os.path.basename(file_path))
        
        return True
    except Exception as e:
        print(f"Error creating zip archive: {e}")
        return False