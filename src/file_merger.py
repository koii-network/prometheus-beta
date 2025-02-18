import os

def merge_files(input_files, output_file):
    """
    Merge multiple input files into a single output file.
    
    Args:
        input_files (list): A list of paths to input files to be merged
        output_file (str): Path to the output merged file
    
    Raises:
        ValueError: If input_files is empty or contains non-existent files
        IOError: If there are issues reading or writing files
    """
    # Validate input files
    if not input_files:
        raise ValueError("No input files provided")
    
    # Check that all input files exist
    non_existent_files = [f for f in input_files if not os.path.exists(f)]
    if non_existent_files:
        raise ValueError(f"The following files do not exist: {non_existent_files}")
    
    try:
        # Open the output file in write mode
        with open(output_file, 'w') as outfile:
            # Iterate through each input file
            for input_file in input_files:
                # Read the content of the input file
                with open(input_file, 'r') as infile:
                    # Write the content to the output file
                    outfile.write(infile.read())
                    # Add a newline between files if the last character is not a newline
                    if not infile.read(1):
                        outfile.write('\n')
        
        return output_file
    except IOError as e:
        raise IOError(f"Error merging files: {e}")