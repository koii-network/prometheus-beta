import os

def split_file_into_chunks(input_file, chunk_size_mb=10, output_dir=None):
    """
    Split a large file into smaller chunks.
    
    Args:
        input_file (str): Path to the input file to be split
        chunk_size_mb (int, optional): Size of each chunk in megabytes. Defaults to 10.
        output_dir (str, optional): Directory to save chunks. Defaults to input file's directory.
    
    Returns:
        list: Paths to the created chunk files
    
    Raises:
        FileNotFoundError: If input file does not exist
        ValueError: If chunk size is less than or equal to 0
    """
    # Validate inputs
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist")
    
    if chunk_size_mb <= 0:
        raise ValueError("Chunk size must be greater than 0")
    
    # Determine output directory
    if output_dir is None:
        output_dir = os.path.dirname(input_file)
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Get input file name and base path
    input_filename = os.path.basename(input_file)
    
    # Convert chunk size to bytes
    chunk_size_bytes = chunk_size_mb * 1024 * 1024
    
    # List to store chunk file paths
    chunk_files = []
    
    # Open input file and start chunking
    with open(input_file, 'rb') as f:
        chunk_number = 1
        while True:
            # Read chunk
            chunk = f.read(chunk_size_bytes)
            
            # Break if no more data
            if not chunk:
                break
            
            # Create chunk filename
            chunk_filename = os.path.join(
                output_dir, 
                f"{input_filename}.part{chunk_number:03d}"
            )
            
            # Write chunk
            with open(chunk_filename, 'wb') as chunk_file:
                chunk_file.write(chunk)
            
            chunk_files.append(chunk_filename)
            chunk_number += 1
    
    return chunk_files