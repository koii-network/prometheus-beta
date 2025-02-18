import os
import tarfile
from typing import Union, List, Optional

def create_tar_archive(
    source_dir: str, 
    output_path: Optional[str] = None, 
    compression: str = 'gz', 
    exclude_patterns: Optional[List[str]] = None
) -> str:
    """
    Create a tar archive from a given directory.
    
    Args:
        source_dir (str): Path to the source directory to archive
        output_path (str, optional): Path for the output tar file. 
            If not provided, uses source directory name with .tar.gz extension
        compression (str, optional): Compression type. 
            Supports 'gz', 'bz2', or None. Defaults to 'gz'
        exclude_patterns (List[str], optional): List of patterns to exclude from archive
    
    Returns:
        str: Path to the created tar archive
    
    Raises:
        ValueError: If source directory does not exist or is not a directory
        ValueError: If invalid compression type is provided
    """
    # Validate source directory
    source_dir = os.path.abspath(source_dir)
    if not os.path.exists(source_dir):
        raise ValueError(f"Source directory does not exist: {source_dir}")
    if not os.path.isdir(source_dir):
        raise ValueError(f"Source is not a directory: {source_dir}")
    
    # Determine compression mode
    compression_modes = {
        'gz': 'w:gz',
        'bz2': 'w:bz2',
        None: 'w'
    }
    if compression not in compression_modes:
        raise ValueError(f"Unsupported compression type: {compression}")
    
    # Determine output path
    if output_path is None:
        output_path = f"{source_dir}.tar.{compression}" if compression else f"{source_dir}.tar"
    output_path = os.path.abspath(output_path)
    
    # Prepare exclude patterns
    if exclude_patterns is None:
        exclude_patterns = []
    
    # Create tar archive
    with tarfile.open(output_path, compression_modes[compression]) as tar:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Check exclusion patterns
                if not any(pattern in file_path for pattern in exclude_patterns):
                    arcname = os.path.relpath(file_path, source_dir)
                    tar.add(file_path, arcname=arcname)
    
    return output_path