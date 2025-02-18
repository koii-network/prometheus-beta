import os

def split_file_into_chunks(file_path, chunk_size_mb=10, output_dir=None):
    """
    Split a large file into smaller chunks.
    
    :param file_path: Path to the file to be split
    :param chunk_size_mb: Size of each chunk in megabytes (default 10MB)
    :param output_dir: Directory to save chunks (defaults to same directory as source file)
    :return: List of chunk file paths
    """
    # Validate input parameters
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if chunk_size_mb <= 0:
        raise ValueError("Chunk size must be a positive number")
    
    # Determine output directory
    if output_dir is None:
        output_dir = os.path.dirname(file_path)
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Get base filename for chunks
    base_filename = os.path.basename(file_path)
    
    # Convert chunk size to bytes
    chunk_size_bytes = chunk_size_mb * 1024 * 1024
    
    # List to store chunk file paths
    chunk_files = []
    
    # Open source file and read/write chunks
    with open(file_path, 'rb') as source_file:
        chunk_number = 1
        while True:
            # Read chunk
            chunk = source_file.read(chunk_size_bytes)
            
            # Break if no more data
            if not chunk:
                break
            
            # Create chunk filename
            chunk_filename = os.path.join(
                output_dir, 
                f"{base_filename}.part{chunk_number:03d}"
            )
            
            # Write chunk to file
            with open(chunk_filename, 'wb') as chunk_file:
                chunk_file.write(chunk)
            
            chunk_files.append(chunk_filename)
            chunk_number += 1
    
    return chunk_files