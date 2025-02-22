def write_string_to_file(file_path: str, content: str) -> None:
    """
    Write a given string to a text file.

    Args:
        file_path (str): The path to the file where the string will be written.
        content (str): The string content to write to the file.

    Raises:
        IOError: If there's an error writing to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError as e:
        raise IOError(f"Error writing to file {file_path}: {e}")