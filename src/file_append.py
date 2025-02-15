def append_text_to_file(file_path: str, text: str) -> None:
    """
    Append text to an existing file.
    
    Args:
        file_path (str): The path to the file to append text to.
        text (str): The text to append to the file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there are issues writing to the file.
    """
    try:
        with open(file_path, 'a') as file:
            file.write(text)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except IOError as e:
        raise IOError(f"Error appending to file: {e}")