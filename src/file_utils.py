import os

def find_largest_file(directory):
    """
    Find the largest file in a given directory.
    
    Args:
        directory (str): Path to the directory to search
    
    Returns:
        dict: A dictionary containing details of the largest file, with keys:
            - 'path': Full path to the largest file
            - 'size': Size of the file in bytes
            - 'filename': Name of the file
        
        Returns None if no files are found or directory is invalid
    """
    # Validate directory input
    if not directory or not os.path.isdir(directory):
        return None
    
    largest_file = None
    largest_size = -1
    
    try:
        # Walk through the directory
        for root, dirs, files in os.walk(directory):
            for file in files:
                full_path = os.path.join(root, file)
                
                # Check file accessibility and get size
                try:
                    file_size = os.path.getsize(full_path)
                    
                    # Update largest file if current file is larger
                    if file_size > largest_size:
                        largest_size = file_size
                        largest_file = {
                            'path': full_path,
                            'size': file_size,
                            'filename': file
                        }
                except (PermissionError, OSError):
                    # Skip files we can't access
                    continue
        
        return largest_file
    
    except Exception:
        # Handle any unexpected errors
        return None