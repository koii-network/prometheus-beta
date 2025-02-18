import os

def merge_files(input_files, output_file):
    """
    Merge multiple input files into a single output file.
    
    Args:
        input_files (list): List of paths to input files to be merged
        output_file (str): Path to the output merged file
    
    Raises:
        ValueError: If input_files is empty or None
        FileNotFoundError: If any of the input files do not exist
    """
    # Input validation
    if not input_files:
        raise ValueError("No input files provided")
    
    # Check that all input files exist
    for file in input_files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"Input file not found: {file}")
    
    # Open output file in write mode
    with open(output_file, 'w') as outfile:
        # Iterate through each input file
        for input_file in input_files:
            # Open each input file and read its contents
            with open(input_file, 'r') as infile:
                # Write the contents to the output file
                outfile.write(infile.read())
                # Add a newline between files if the last character is not a newline
                if not infile.read(-1).endswith('\n'):
                    outfile.write('\n')
    
    return output_file  # Return the path of the merged file