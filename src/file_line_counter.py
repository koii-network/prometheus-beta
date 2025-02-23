def count_file_lines(file_path):
    """
    Count the number of lines in a given file.

    Args:
        file_path (str): Path to the file to be counted.

    Returns:
        int: Number of lines in the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there's an issue reading the file.
    """
    try:
        with open(file_path, 'r') as file:
            # Count lines efficiently
            return sum(1 for _ in file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {e}")