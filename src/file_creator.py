import os

def create_text_file(file_path, content=''):
    """
    Create a new text file with optional content.

    Args:
        file_path (str): The path where the file should be created.
        content (str or any, optional): The content to write to the file. 
                                       Defaults to empty string.
                                       Non-string content will be converted to str.

    Raises:
        ValueError: If file_path is empty or None.
        PermissionError: If there's no permission to create the file.
        OSError: If the directory path is invalid or cannot be created.
    """
    # Validate input
    if not file_path:
        raise ValueError("File path cannot be empty")

    # Ensure directory exists
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    # Convert content to string
    str_content = str(content)

    # Create and write to the file
    try:
        with open(file_path, 'w') as file:
            file.write(str_content)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot create file at {file_path}")
    except OSError as e:
        raise OSError(f"Error creating file at {file_path}: {str(e)}")

    return file_path