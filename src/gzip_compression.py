import gzip
import os
import typing

def compress_file(input_path: str, output_path: str = None) -> str:
    """
    Compress a file using Gzip compression.
    
    Args:
        input_path (str): Path to the input file to be compressed
        output_path (str, optional): Path for the compressed output file. 
                                     If not provided, appends .gz to input path
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues
        ValueError: If input or output paths are invalid
    """
    # Validate input path
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # If no output path is provided, create one by appending .gz
    if output_path is None:
        output_path = input_path + '.gz'
    
    # Validate output path
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        # Perform Gzip compression
        with open(input_path, 'rb') as f_in:
            with gzip.open(output_path, 'wb') as f_out:
                f_out.writelines(f_in)
        
        return output_path
    except PermissionError:
        raise PermissionError(f"Permission denied when compressing {input_path}")
    except Exception as e:
        raise ValueError(f"Compression error: {str(e)}")

def decompress_file(input_path: str, output_path: str = None) -> str:
    """
    Decompress a Gzip compressed file.
    
    Args:
        input_path (str): Path to the Gzip compressed input file
        output_path (str, optional): Path for the decompressed output file. 
                                     If not provided, removes .gz from input path
    
    Returns:
        str: Path to the decompressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues
        ValueError: If input or output paths are invalid
    """
    # Validate input path
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # If no output path is provided, create one by removing .gz
    if output_path is None:
        output_path = input_path.removesuffix('.gz')
        if output_path == input_path:
            output_path += '.decompressed'
    
    # Validate output path
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        # Perform Gzip decompression
        with gzip.open(input_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                f_out.writelines(f_in)
        
        return output_path
    except PermissionError:
        raise PermissionError(f"Permission denied when decompressing {input_path}")
    except Exception as e:
        raise ValueError(f"Decompression error: {str(e)}")