import os

def create_text_file(file_path, content=''):
    """
    Create a new text file with optional content.
    
    Args:
        file_path (str): The path and name of the file to create
        content (str, optional): Content to write in the file. Defaults to empty string.
    
    Raises:
        ValueError: If file_path is empty or None
        IOError: If the file cannot be created due to permission or path issues
    """
    if not file_path:
        raise ValueError("File path cannot be empty")
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True) if os.path.dirname(file_path) else None
    
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return True
    except Exception as e:
        raise IOError(f"Error creating file: {e}")