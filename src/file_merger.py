import os
from typing import List, Union

def merge_files(input_files: List[str], output_file: str, separator: str = '\n\n') -> None:
    """
    Merge multiple files into a single output file.

    Args:
        input_files (List[str]): List of paths to input files to be merged.
        output_file (str): Path to the output merged file.
        separator (str, optional): Separator to use between file contents. 
                                   Defaults to double newline.

    Raises:
        FileNotFoundError: If any of the input files do not exist.
        PermissionError: If there are permission issues reading/writing files.
        TypeError: If input arguments are of incorrect type.
        ValueError: If input_files list is empty.
    """
    # Input validation
    if not isinstance(input_files, list):
        raise TypeError("input_files must be a list of file paths")
    
    if len(input_files) == 0:
        raise ValueError("input_files list cannot be empty")
    
    if not isinstance(output_file, str):
        raise TypeError("output_file must be a string")
    
    if not isinstance(separator, str):
        raise TypeError("separator must be a string")

    # Check if all input files exist
    for file_path in input_files:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Input file not found: {file_path}")

    # Read and merge file contents
    try:
        with open(output_file, 'w') as outfile:
            for i, file_path in enumerate(input_files):
                with open(file_path, 'r') as infile:
                    content = infile.read()
                    outfile.write(content)
                    
                    # Add separator between files, but not after the last file
                    if i < len(input_files) - 1:
                        outfile.write(separator)
    except PermissionError:
        raise PermissionError(f"Permission denied when writing to {output_file}")