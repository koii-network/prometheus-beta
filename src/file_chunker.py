import os

def chunk_file(input_file, chunk_size_mb=10, output_dir=None):
    """
    Split a large file into smaller chunks.
    
    Args:
        input_file (str): Path to the input file to be chunked
        chunk_size_mb (int, optional): Size of each chunk in megabytes. Defaults to 10.
        output_dir (str, optional): Directory to save chunks. Defaults to input file's directory.
    
    Returns:
        list: Paths of created chunk files
    
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
    os.makedirs(output_dir, exist_ok=True)
    
    # Prepare file naming
    base_filename = os.path.basename(input_file)
    chunk_size_bytes = chunk_size_mb * 1024 * 1024
    chunk_files = []
    
    # Chunk the file
    with open(input_file, 'rb') as f:
        chunk_number = 1
        while True:
            chunk_data = f.read(chunk_size_bytes)
            if not chunk_data:
                break
            
            chunk_filename = os.path.join(output_dir, f"{base_filename}_chunk_{chunk_number}")
            with open(chunk_filename, 'wb') as chunk_file:
                chunk_file.write(chunk_data)
            
            chunk_files.append(chunk_filename)
            chunk_number += 1
    
    return chunk_files