import lzma
import os

def compress_to_xz(input_path, output_path=None):
    """
    Compress a file or directory using XZ compression.
    
    Args:
        input_path (str): Path to the file or directory to compress
        output_path (str, optional): Path to save the compressed file. 
                                     If not provided, appends '.xz' to input path.
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If input path does not exist
        IsADirectoryError: If input is a directory and compression of entire directory is not supported
        PermissionError: If there are insufficient permissions to read/write
    """
    # Validate input path exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input path does not exist: {input_path}")
    
    # If input is a directory, raise an error (for simplicity)
    if os.path.isdir(input_path):
        raise IsADirectoryError("Directory compression is not supported. Please compress individual files.")
    
    # Determine output path if not provided
    if output_path is None:
        output_path = input_path + '.xz'
    
    try:
        # Perform XZ compression
        with open(input_path, 'rb') as input_file:
            with lzma.open(output_path, 'wb') as output_file:
                output_file.write(input_file.read())
        
        return output_path
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to read {input_path} or write to {output_path}")
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")