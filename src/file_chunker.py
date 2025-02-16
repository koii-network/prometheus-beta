import os
import typing

def split_file_into_chunks(
    input_file_path: str, 
    chunk_size_bytes: int, 
    output_dir: typing.Optional[str] = None
) -> typing.List[str]:
    """
    Split a large file into smaller chunks.
    
    Args:
        input_file_path (str): Path to the input file to be chunked
        chunk_size_bytes (int): Size of each chunk in bytes
        output_dir (str, optional): Directory to save chunks. 
                                    Defaults to same directory as input file.
    
    Returns:
        List[str]: Paths to the created chunk files
    
    Raises:
        ValueError: If input file does not exist or chunk size is invalid
        IOError: If there are issues reading/writing files
    """
    # Validate inputs
    if not os.path.exists(input_file_path):
        raise ValueError(f"Input file {input_file_path} does not exist")
    
    if chunk_size_bytes <= 0:
        raise ValueError("Chunk size must be a positive integer")
    
    # Determine output directory
    if output_dir is None:
        output_dir = os.path.dirname(input_file_path) or '.'
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get base filename for chunk naming
    base_filename = os.path.splitext(os.path.basename(input_file_path))[0]
    
    # List to store chunk file paths
    chunk_files = []
    
    # Open input file and read/write chunks
    with open(input_file_path, 'rb') as input_file:
        chunk_number = 1
        while True:
            # Read chunk
            chunk = input_file.read(chunk_size_bytes)
            
            # Break if no more data
            if not chunk:
                break
            
            # Create chunk filename
            chunk_filename = os.path.join(
                output_dir, 
                f"{base_filename}_chunk_{chunk_number:03d}"
            )
            
            # Write chunk to file
            with open(chunk_filename, 'wb') as chunk_file:
                chunk_file.write(chunk)
            
            chunk_files.append(chunk_filename)
            chunk_number += 1
    
    return chunk_files