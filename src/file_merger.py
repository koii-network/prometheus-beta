import os
from typing import List, Union

def merge_files(input_files: List[str], output_file: str, separator: str = '\n') -> None:
    """
    Merge multiple input files into a single output file.

    Args:
        input_files (List[str]): List of paths to input files to be merged.
        output_file (str): Path to the output merged file.
        separator (str, optional): Separator to use between file contents. 
                                   Defaults to newline character.

    Raises:
        FileNotFoundError: If any of the input files do not exist.
        ValueError: If input_files list is empty.
        IOError: If there are issues reading or writing files.
    """
    # Validate input
    if not input_files:
        raise ValueError("At least one input file must be provided")
    
    # Check if all input files exist
    for file in input_files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"Input file not found: {file}")
    
    try:
        # Open output file in write mode
        with open(output_file, 'w') as outfile:
            # Iterate through input files
            for i, input_file in enumerate(input_files):
                # Read content of each input file
                with open(input_file, 'r') as infile:
                    content = infile.read()
                    
                    # Write content to output file
                    outfile.write(content)
                    
                    # Add separator between files, but not after the last file
                    if i < len(input_files) - 1:
                        outfile.write(separator)
    except IOError as e:
        raise IOError(f"Error merging files: {e}")