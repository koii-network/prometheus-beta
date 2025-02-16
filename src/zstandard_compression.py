import zstandard as zstd
import os

def compress_file(input_path, output_path=None):
    """
    Compress a file using Zstandard compression algorithm.
    
    Args:
        input_path (str): Path to the input file to be compressed
        output_path (str, optional): Path to save the compressed file. 
                                     If not provided, appends .zst to input path
    
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
    
    # Determine output path
    if output_path is None:
        output_path = input_path + '.zst'
    
    try:
        # Create a Zstandard compressor
        cctx = zstd.ZstdCompressor()
        
        # Compress the file
        with open(input_path, 'rb') as input_file:
            with open(output_path, 'wb') as output_file:
                cctx.copy_stream(input_file, output_file)
        
        return output_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files")
    except Exception as e:
        raise ValueError(f"Compression error: {str(e)}")

def decompress_file(input_path, output_path=None):
    """
    Decompress a Zstandard compressed file.
    
    Args:
        input_path (str): Path to the Zstandard compressed file
        output_path (str, optional): Path to save the decompressed file.
                                     If not provided, removes .zst extension
    
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
    
    # Determine output path
    if output_path is None:
        if not input_path.endswith('.zst'):
            raise ValueError(f"Input file must have .zst extension or output path must be specified")
        output_path = input_path[:-4]  # Remove .zst extension
    
    try:
        # Create a Zstandard decompressor
        dctx = zstd.ZstdDecompressor()
        
        # Decompress the file
        with open(input_path, 'rb') as input_file:
            with open(output_path, 'wb') as output_file:
                dctx.copy_stream(input_file, output_file)
        
        return output_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files")
    except Exception as e:
        raise ValueError(f"Decompression error: {str(e)}")