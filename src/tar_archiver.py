import os
import tarfile
from typing import Union, Optional


def create_tar_archive(source_dir: str, 
                       output_path: Optional[str] = None, 
                       compression: str = 'gz') -> str:
    """
    Create a tar archive of a given directory.

    Args:
        source_dir (str): Path to the directory to be archived
        output_path (Optional[str], optional): Path for the output tar file. 
            If None, uses source directory name in current working directory. 
        compression (str, optional): Compression type. 
            Supports 'gz' (default), 'bz2', or 'xz'. 
            Use None for uncompressed tar.

    Returns:
        str: Path to the created tar archive

    Raises:
        ValueError: If source directory does not exist or is not a directory
        ValueError: If invalid compression type is specified
    """
    # Validate source directory
    source_dir = os.path.abspath(source_dir)
    if not os.path.exists(source_dir):
        raise ValueError(f"Source directory does not exist: {source_dir}")
    if not os.path.isdir(source_dir):
        raise ValueError(f"Source path is not a directory: {source_dir}")

    # Validate compression type
    valid_compressions = {'gz', 'bz2', 'xz', None}
    if compression not in valid_compressions:
        raise ValueError(f"Invalid compression type. Must be one of {valid_compressions}")

    # Determine output path
    if output_path is None:
        # Use source directory name as base for tar file
        base_name = os.path.basename(source_dir.rstrip('/'))
        output_path = f"{base_name}.tar"
        
        # Add compression extension if applicable
        if compression:
            output_path += f".{compression}"

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)

    # Create tar archive with specified compression
    mode = f"w:{compression}" if compression else "w"
    with tarfile.open(output_path, mode) as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

    return os.path.abspath(output_path)