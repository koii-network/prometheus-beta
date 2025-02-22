import lzma
import os

def compress_file(input_path, output_path=None):
    """
    Compress a file using LZMA compression.
    
    Args:
        input_path (str): Path to the input file to be compressed
        output_path (str, optional): Path to save the compressed file. 
                                     If not provided, appends '.lzma' to input path.
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues
        IOError: For other I/O related errors
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Determine output path if not provided
    if output_path is None:
        output_path = input_path + '.lzma'
    
    try:
        # Open input and output files
        with open(input_path, 'rb') as input_file, \
             lzma.open(output_path, 'wb') as compressed_file:
            # Read and compress in chunks to handle large files
            chunk = input_file.read(1024 * 1024)  # 1MB chunks
            while chunk:
                compressed_file.write(chunk)
                chunk = input_file.read(1024 * 1024)
        
        return output_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files: {input_path}, {output_path}")
    except IOError as e:
        raise IOError(f"Error during compression: {str(e)}")

def decompress_file(input_path, output_path=None):
    """
    Decompress a file compressed with LZMA.
    
    Args:
        input_path (str): Path to the LZMA compressed input file
        output_path (str, optional): Path to save the decompressed file. 
                                     If not provided, removes '.lzma' from input path.
    
    Returns:
        str: Path to the decompressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues
        IOError: For other I/O related errors
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input compressed file not found: {input_path}")
    
    # Determine output path if not provided
    if output_path is None:
        if not input_path.endswith('.lzma'):
            raise ValueError("Input file must have .lzma extension or output path must be specified")
        output_path = input_path[:-5]  # Remove .lzma extension
    
    try:
        # Open input and output files
        with lzma.open(input_path, 'rb') as compressed_file, \
             open(output_path, 'wb') as output_file:
            # Read and decompress in chunks to handle large files
            chunk = compressed_file.read(1024 * 1024)  # 1MB chunks
            while chunk:
                output_file.write(chunk)
                chunk = compressed_file.read(1024 * 1024)
        
        return output_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files: {input_path}, {output_path}")
    except IOError as e:
        raise IOError(f"Error during decompression: {str(e)}")