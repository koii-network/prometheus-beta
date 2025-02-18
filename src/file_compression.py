import os
import zlib

def calculate_compression_ratio(file_path):
    """
    Calculate the compression ratio of a file using zlib compression.
    
    :param file_path: Path to the file to be analyzed
    :return: Compression ratio (original size / compressed size)
    :raises FileNotFoundError: If the file does not exist
    :raises ValueError: If the file is empty or cannot be read
    """
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check file size
    file_size = os.path.getsize(file_path)
    if file_size == 0:
        raise ValueError("Cannot calculate compression ratio for an empty file")
    
    # Read file contents
    try:
        with open(file_path, 'rb') as f:
            file_contents = f.read()
    except IOError:
        raise ValueError(f"Unable to read file: {file_path}")
    
    # Compress the file contents
    compressed_contents = zlib.compress(file_contents)
    
    # Calculate and return compression ratio
    compressed_size = len(compressed_contents)
    return file_size / compressed_size if compressed_size > 0 else 1.0