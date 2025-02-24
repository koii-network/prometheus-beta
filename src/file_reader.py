def read_text_file(file_path):
    """
    Read and return the contents of a text file.

    Args:
        file_path (str): The path to the text file to be read.

    Returns:
        str: The contents of the text file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there are insufficient permissions to read the file.
        IsADirectoryError: If the path points to a directory instead of a file.
        IOError: For other input/output related errors.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to read {file_path}.")
    except IsADirectoryError:
        raise IsADirectoryError(f"{file_path} is a directory, not a file.")
    except IOError as e:
        raise IOError(f"An error occurred while reading {file_path}: {str(e)}")