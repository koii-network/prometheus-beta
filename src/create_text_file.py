import os

def create_text_file(file_path, content=''):
    """
    Create a new text file with optional content.
    
    Args:
        file_path (str): The path where the text file will be created
        content (str, optional): The content to write to the file. Defaults to an empty string.
    
    Raises:
        ValueError: If the file path is invalid or empty
        PermissionError: If there are insufficient permissions to create the file
        FileExistsError: If the file already exists
    """
    # Validate file path
    if not file_path or not isinstance(file_path, str):
        raise ValueError("Invalid file path")
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True) if os.path.dirname(file_path) else None
    
    # Check if file already exists
    if os.path.exists(file_path):
        raise FileExistsError(f"File {file_path} already exists")
    
    # Create and write to the file
    try:
        with open(file_path, 'w') as f:
            f.write(str(content))
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to create file {file_path}")
    
    return file_path