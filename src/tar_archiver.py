import os
import tarfile
from typing import Union, List, Optional

def create_tar_archive(source_dir: str, 
                       archive_path: Optional[str] = None, 
                       exclude_patterns: Optional[List[str]] = None) -> str:
    """
    Create a tar archive of a given directory.
    
    Args:
        source_dir (str): Path to the directory to be archived
        archive_path (Optional[str]): Path where the tar archive will be saved. 
                                      If None, creates archive in the same directory.
        exclude_patterns (Optional[List[str]]): List of patterns to exclude from the archive
    
    Returns:
        str: Path to the created tar archive
    
    Raises:
        ValueError: If source directory does not exist
        OSError: If there are issues creating the archive
    """
    # Validate source directory exists
    source_dir = os.path.abspath(source_dir)
    if not os.path.isdir(source_dir):
        raise ValueError(f"Source directory does not exist: {source_dir}")
    
    # Determine archive path
    if archive_path is None:
        archive_path = os.path.join(os.path.dirname(source_dir), 
                                    f"{os.path.basename(source_dir)}.tar.gz")
    
    # Ensure archive path has .tar.gz extension
    if not archive_path.endswith('.tar.gz'):
        archive_path += '.tar.gz'
    
    # Create tar archive
    with tarfile.open(archive_path, 'w:gz') as tar:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                # Construct full file path
                file_path = os.path.join(root, file)
                
                # Skip files matching exclude patterns if provided
                if exclude_patterns:
                    if any(pattern in file_path for pattern in exclude_patterns):
                        continue
                
                # Add file to archive, preserving relative path
                arcname = os.path.relpath(file_path, source_dir)
                tar.add(file_path, arcname=arcname)
    
    return archive_path