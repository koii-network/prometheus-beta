import lzma
import os

def compress_lzma(input_file_path, output_file_path=None):
    """
    Compress a file using LZMA compression algorithm.
    
    :param input_file_path: Path to the input file to be compressed
    :param output_file_path: Optional path for the compressed file. 
                              If not provided, appends '.lzma' to input file path
    :return: Path to the compressed file
    :raises FileNotFoundError: If input file does not exist
    :raises PermissionError: If there are permission issues reading/writing files
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    # Determine output file path
    if output_file_path is None:
        output_file_path = input_file_path + '.lzma'
    
    try:
        # Read input file contents
        with open(input_file_path, 'rb') as input_file:
            input_data = input_file.read()
        
        # Compress data using LZMA
        compressed_data = lzma.compress(input_data)
        
        # Write compressed data to output file
        with open(output_file_path, 'wb') as output_file:
            output_file.write(compressed_data)
        
        return output_file_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files: {input_file_path}, {output_file_path}")
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def decompress_lzma(input_file_path, output_file_path=None):
    """
    Decompress a file compressed with LZMA compression algorithm.
    
    :param input_file_path: Path to the compressed LZMA file
    :param output_file_path: Optional path for the decompressed file. 
                              If not provided, removes '.lzma' from input file path
    :return: Path to the decompressed file
    :raises FileNotFoundError: If input file does not exist
    :raises PermissionError: If there are permission issues reading/writing files
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input compressed file not found: {input_file_path}")
    
    # Determine output file path
    if output_file_path is None:
        if input_file_path.endswith('.lzma'):
            output_file_path = input_file_path[:-5]
        else:
            output_file_path = input_file_path + '_decompressed'
    
    try:
        # Read input file contents
        with open(input_file_path, 'rb') as input_file:
            compressed_data = input_file.read()
        
        # Decompress data using LZMA
        decompressed_data = lzma.decompress(compressed_data)
        
        # Write decompressed data to output file
        with open(output_file_path, 'wb') as output_file:
            output_file.write(decompressed_data)
        
        return output_file_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files: {input_file_path}, {output_file_path}")
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")