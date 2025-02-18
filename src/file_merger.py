import os

def merge_files(input_files, output_file, separator='\n'):
    """
    Merge multiple input files into a single output file.
    
    :param input_files: List of input file paths to merge
    :param output_file: Path of the output merged file
    :param separator: Optional separator between file contents (default is newline)
    :raises FileNotFoundError: If any input file does not exist
    :raises ValueError: If input_files is empty
    """
    # Validate input
    if not input_files:
        raise ValueError("No input files provided for merging")
    
    # Check if all input files exist
    for file in input_files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"Input file not found: {file}")
    
    # Read and merge file contents
    merged_content = []
    for file in input_files:
        with open(file, 'r') as f:
            merged_content.append(f.read().strip())
    
    # Write merged content to output file
    with open(output_file, 'w') as f:
        f.write(separator.join(merged_content))
    
    return output_file