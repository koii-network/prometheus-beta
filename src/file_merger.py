import os

def merge_files(input_files, output_file, separator='\n\n'):
    """
    Merge multiple input files into a single output file.
    
    Args:
        input_files (list): List of paths to input files to be merged
        output_file (str): Path to the output merged file
        separator (str, optional): Separator to use between file contents. Defaults to two newlines.
    
    Raises:
        FileNotFoundError: If any of the input files do not exist
        ValueError: If input_files is empty
        PermissionError: If there are permission issues writing the output file
    """
    # Validate input
    if not input_files:
        raise ValueError("No input files provided")
    
    # Check that all input files exist
    for file in input_files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"Input file not found: {file}")
    
    # Read contents of input files
    try:
        file_contents = []
        for file in input_files:
            with open(file, 'r', encoding='utf-8') as f:
                file_contents.append(f.read().strip())
        
        # Write merged contents to output file
        with open(output_file, 'w', encoding='utf-8') as out_file:
            out_file.write(separator.join(file_contents))
        
        return output_file
    except PermissionError:
        raise PermissionError(f"Permission denied when writing to {output_file}")