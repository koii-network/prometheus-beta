import os

def create_text_file(file_path, content=''):
    """
    Create a new text file with optional content.
    
    Args:
        file_path (str): The path and name of the file to create
        content (str, optional): The content to write to the file. Defaults to empty string.
    
    Raises:
        ValueError: If file_path is empty or None
        IOError: If file cannot be created due to permission or path issues
    """
    # Validate input
    if not file_path:
        raise ValueError("File path cannot be empty")
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True) if os.path.dirname(file_path) else None
    
    # Create and write to file
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return file_path
    except PermissionError:
        raise IOError(f"Permission denied: Cannot create file at {file_path}")
    except Exception as e:
        raise IOError(f"Error creating file: {str(e)}")