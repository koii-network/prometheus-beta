import bz2
import os

def compress_bzip2(input_path, output_path=None):
    """
    Compress a file or directory using Bzip2 compression.
    
    Args:
        input_path (str): Path to the file or directory to compress
        output_path (str, optional): Path to save the compressed file. 
                                     If not provided, creates a .bz2 file in the same location.
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If input path does not exist
        IsADirectoryError: If input path is a directory and compression of directories is not supported
        PermissionError: If there are insufficient permissions to read/write files
    """
    # Validate input path exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input path does not exist: {input_path}")
    
    # Check if input is a directory
    if os.path.isdir(input_path):
        raise IsADirectoryError("Directory compression is not supported. Compress individual files.")
    
    # Determine output path if not provided
    if output_path is None:
        output_path = input_path + '.bz2'
    
    # Perform compression
    try:
        with open(input_path, 'rb') as input_file:
            data = input_file.read()
            compressed_data = bz2.compress(data)
        
        with open(output_path, 'wb') as output_file:
            output_file.write(compressed_data)
        
        return output_path
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to read {input_path} or write {output_path}")
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def decompress_bzip2(input_path, output_path=None):
    """
    Decompress a Bzip2 compressed file.
    
    Args:
        input_path (str): Path to the Bzip2 compressed file
        output_path (str, optional): Path to save the decompressed file. 
                                     If not provided, removes .bz2 extension.
    
    Returns:
        str: Path to the decompressed file
    
    Raises:
        FileNotFoundError: If input path does not exist
        ValueError: If input file is not a valid Bzip2 compressed file
    """
    # Validate input path exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input path does not exist: {input_path}")
    
    # Determine output path if not provided
    if output_path is None:
        if not input_path.endswith('.bz2'):
            raise ValueError("Input file must have .bz2 extension if no output path is provided")
        output_path = input_path[:-4]  # Remove .bz2 extension
    
    # Perform decompression
    try:
        with open(input_path, 'rb') as input_file:
            compressed_data = input_file.read()
            decompressed_data = bz2.decompress(compressed_data)
        
        with open(output_path, 'wb') as output_file:
            output_file.write(decompressed_data)
        
        return output_path
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")