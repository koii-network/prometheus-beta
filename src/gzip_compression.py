import gzip
import os

def gzip_compress(input_path, output_path=None):
    """
    Compress a file using Gzip compression.
    
    Args:
        input_path (str): Path to the input file to be compressed
        output_path (str, optional): Path for the output compressed file. 
                                     If not provided, appends '.gz' to input path.
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues
        ValueError: If input paths are invalid
    """
    # Validate input path
    if not isinstance(input_path, str) or not input_path:
        raise ValueError("Input path must be a non-empty string")
    
    # Check if input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Determine output path
    if output_path is None:
        output_path = input_path + '.gz'
    
    try:
        # Open input file for reading
        with open(input_path, 'rb') as f_in:
            # Open output file for gzip compression
            with gzip.open(output_path, 'wb') as f_out:
                # Read and compress the file in chunks to handle large files
                chunk = f_in.read(8192)
                while chunk:
                    f_out.write(chunk)
                    chunk = f_in.read(8192)
        
        return output_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot read {input_path} or write to {output_path}")
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")