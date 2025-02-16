import lzo
import os

def lzop_compress(input_file, output_file=None):
    """
    Compress a file using LZOP compression algorithm.
    
    :param input_file: Path to the input file to be compressed
    :param output_file: Optional path for the compressed output file. 
                        If not provided, appends '.lzo' to input filename
    :return: Path to the compressed file
    :raises FileNotFoundError: If input file does not exist
    :raises IOError: If there are issues during compression
    """
    # Validate input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    # Determine output file path if not provided
    if output_file is None:
        output_file = input_file + '.lzo'
    
    try:
        # Read input file
        with open(input_file, 'rb') as f_in:
            input_data = f_in.read()
        
        # Compress data using python-lzo
        compressed_data = lzo.compress(input_data)
        
        # Write compressed data to output file
        with open(output_file, 'wb') as f_out:
            f_out.write(compressed_data)
        
        return output_file
    
    except Exception as e:
        raise IOError(f"Compression failed: {str(e)}")

def lzop_decompress(input_file, output_file=None):
    """
    Decompress a file compressed with LZOP compression algorithm.
    
    :param input_file: Path to the LZO compressed input file
    :param output_file: Optional path for the decompressed output file. 
                        If not provided, removes '.lzo' from input filename
    :return: Path to the decompressed file
    :raises FileNotFoundError: If input file does not exist
    :raises IOError: If there are issues during decompression
    """
    # Validate input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    # Determine output file path if not provided
    if output_file is None:
        output_file = input_file.removesuffix('.lzo')
        if output_file == input_file:  # if no .lzo extension
            output_file += '.decompressed'
    
    try:
        # Read input file
        with open(input_file, 'rb') as f_in:
            input_data = f_in.read()
        
        # Decompress data using python-lzo
        decompressed_data = lzo.decompress(input_data)
        
        # Write decompressed data to output file
        with open(output_file, 'wb') as f_out:
            f_out.write(decompressed_data)
        
        return output_file
    
    except Exception as e:
        raise IOError(f"Decompression failed: {str(e)}")