def count_file_lines(file_path):
    """
    Count the number of lines in a given file.

    Args:
        file_path (str): Path to the file to be read.

    Returns:
        int: Number of lines in the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there's an issue reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            # readlines() reads all lines, so we can simply count its length
            return len(file.readlines())
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")