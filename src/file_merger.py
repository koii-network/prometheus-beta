import os

def merge_files(input_files, output_file):
    """
    Merge multiple input files into a single output file.
    
    Args:
        input_files (list): List of paths to input files to be merged
        output_file (str): Path to the output merged file
    
    Raises:
        FileNotFoundError: If any of the input files do not exist
        ValueError: If input_files is empty
    """
    # Validate input
    if not input_files:
        raise ValueError("No input files provided")
    
    # Check if all input files exist
    for file in input_files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"Input file not found: {file}")
    
    # Open output file in write mode
    with open(output_file, 'w') as outfile:
        # Iterate through input files
        for file in input_files:
            # Read and write contents of each input file
            with open(file, 'r') as infile:
                outfile.write(infile.read())
                # Add a newline between files if they don't end with a newline
                outfile.write('\n')
    
    return output_file