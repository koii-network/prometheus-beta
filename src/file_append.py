def append_text_to_file(file_path: str, text: str) -> bool:
    """
    Append text to an existing file.
    
    Args:
        file_path (str): Path to the file to append text to
        text (str): Text to append to the file
    
    Returns:
        bool: True if append was successful, False otherwise
    
    Raises:
        FileNotFoundError: If the specified file does not exist
        PermissionError: If there are insufficient permissions to write to the file
    """
    try:
        with open(file_path, 'a') as file:
            file.write(text)
        return True
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to write to {file_path}.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
        return False