import os
import tarfile
from typing import Union, List, Optional

def create_tar_archive(source_dir: str, 
                       archive_path: Optional[str] = None, 
                       exclude_patterns: Optional[List[str]] = None) -> str:
    """
    Create a tar archive of a directory.
    
    Args:
        source_dir (str): Path to the directory to be archived
        archive_path (Optional[str]): Path where the tar archive will be saved. 
                                      If None, saves in the same directory as source_dir
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
    
    # Ensure the directory for the archive exists
    os.makedirs(os.path.dirname(archive_path), exist_ok=True)
    
    # Create tar archive
    with tarfile.open(archive_path, "w:gz") as tar:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                
                # Check exclusion patterns
                if exclude_patterns:
                    skip_file = any(
                        pattern in file_path for pattern in exclude_patterns
                    )
                    if skip_file:
                        continue
                
                # Create tarinfo and add file to archive
                arcname = os.path.relpath(file_path, source_dir)
                tar.add(file_path, arcname=arcname)
    
    return archive_path