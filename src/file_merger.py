import os
import shutil

def merge_files(input_files, output_file):
    """
    Merge multiple input files into a single output file.
    
    Args:
        input_files (list): List of paths to input files to be merged
        output_file (str): Path to the output merged file
    
    Raises:
        ValueError: If input_files is empty or output_file is not specified
        FileNotFoundError: If any of the input files do not exist
    """
    # Validate inputs
    if not input_files:
        raise ValueError("No input files provided")
    
    if not output_file:
        raise ValueError("No output file specified")
    
    # Check that all input files exist
    for file_path in input_files:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Input file not found: {file_path}")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Open output file in write mode
    with open(output_file, 'wb') as outfile:
        for file_path in input_files:
            # Open each input file in read-binary mode and copy contents
            with open(file_path, 'rb') as infile:
                shutil.copyfileobj(infile, outfile)
    
    return output_file