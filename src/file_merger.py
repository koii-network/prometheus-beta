import os
from typing import List, Union

def merge_files(input_files: List[str], output_file: str, overwrite: bool = False) -> None:
    """
    Merge multiple files into a single output file.

    Args:
        input_files (List[str]): List of paths to input files to be merged.
        output_file (str): Path to the output merged file.
        overwrite (bool, optional): Whether to overwrite existing output file. Defaults to False.

    Raises:
        FileNotFoundError: If any of the input files do not exist.
        PermissionError: If there are permission issues reading/writing files.
        ValueError: If input_files is empty or output_file is invalid.
    """
    # Validate input
    if not input_files:
        raise ValueError("At least one input file must be provided.")
    
    # Validate input files exist
    for file in input_files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"Input file not found: {file}")
    
    # Check output file
    if not output_file:
        raise ValueError("Output file path cannot be empty.")
    
    # Check overwrite condition
    if os.path.exists(output_file) and not overwrite:
        raise FileExistsError(f"Output file {output_file} already exists. Use overwrite=True to replace.")
    
    try:
        # Open output file in write mode
        with open(output_file, 'w') as outfile:
            # Iterate through input files and write their contents
            for input_file in input_files:
                with open(input_file, 'r') as infile:
                    # Add a newline between files if the last line doesn't end with a newline
                    content = infile.read()
                    if content and not content.endswith('\n'):
                        content += '\n'
                    outfile.write(content)
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to write to {output_file}")
    except IOError as e:
        raise IOError(f"Error merging files: {str(e)}")