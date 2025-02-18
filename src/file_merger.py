import os

def merge_files(input_files, output_file, separator='\n\n'):
    """
    Merge multiple input files into a single output file.
    
    Args:
        input_files (list): List of paths to input files to be merged
        output_file (str): Path to the output merged file
        separator (str, optional): Separator between file contents. Defaults to two newlines.
    
    Raises:
        ValueError: If input_files is empty
        FileNotFoundError: If any input file does not exist
        IOError: If there are issues reading or writing files
    """
    # Validate input
    if not input_files:
        raise ValueError("No input files provided")
    
    # Check that all input files exist
    for file in input_files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"Input file not found: {file}")
    
    # Read contents of all files
    try:
        file_contents = []
        for file in input_files:
            with open(file, 'r') as f:
                file_contents.append(f.read().strip())
        
        # Write merged contents to output file
        with open(output_file, 'w') as f:
            f.write(separator.join(file_contents))
        
        return output_file
    except IOError as e:
        raise IOError(f"Error merging files: {e}")