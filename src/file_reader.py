def read_file_line_by_line(file_path):
    """
    Read a file line by line and return a list of lines.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        list: A list of strings, where each string is a line from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there is an error reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")