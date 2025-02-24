import os
from typing import Union, Optional

def find_largest_file(directory: str) -> Optional[str]:
    """
    Find the largest file in a given directory.

    Args:
        directory (str): Path to the directory to search.

    Returns:
        Optional[str]: Path to the largest file, or None if no files exist.

    Raises:
        ValueError: If the directory does not exist or is not a directory.
    """
    # Validate input directory
    if not os.path.exists(directory):
        raise ValueError(f"Directory does not exist: {directory}")
    
    if not os.path.isdir(directory):
        raise ValueError(f"Path is not a directory: {directory}")

    # Initialize variables
    largest_file = None
    max_size = 0

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            
            # Skip if not a file
            if not os.path.isfile(filepath):
                continue

            try:
                # Get file size ensuring file is readable
                if os.access(filepath, os.R_OK):
                    file_size = os.path.getsize(filepath)
                    
                    # Update largest file if current file is larger
                    if file_size > max_size:
                        max_size = file_size
                        largest_file = filepath
            except (OSError, IOError):
                # Skip files that can't be read
                continue

    return largest_file