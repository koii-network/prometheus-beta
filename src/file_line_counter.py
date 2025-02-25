def count_file_lines(file_path):
    """
    Count the number of lines in a given file.

    Args:
        file_path (str): Path to the file to be read.

    Returns:
        int: Number of lines in the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If there's a permission issue reading the file.
        IOError: If there's another issue reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            # readlines() reads all lines, so we can simply count its length
            return len(file.readlines())
    except PermissionError:
        raise PermissionError(f"Permission denied: Unable to read file {file_path}")
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")