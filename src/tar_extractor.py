import os
import tarfile
from typing import Union, List, Optional

def extract_tar_archive(
    archive_path: str, 
    extract_path: Optional[str] = None, 
    specific_files: Optional[List[str]] = None
) -> List[str]:
    """
    Extract files from a tar archive.

    Args:
        archive_path (str): Path to the tar archive file.
        extract_path (Optional[str], optional): Directory to extract files to. 
            Defaults to the directory of the archive if not specified.
        specific_files (Optional[List[str]], optional): List of specific files to extract. 
            Extracts all files if None.

    Returns:
        List[str]: List of paths to extracted files.

    Raises:
        FileNotFoundError: If the archive file does not exist.
        ValueError: If the archive is invalid or cannot be opened.
        PermissionError: If there are insufficient permissions to extract files.
    """
    # Validate input archive path
    if not os.path.exists(archive_path):
        raise FileNotFoundError(f"Archive file not found: {archive_path}")

    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(os.path.abspath(archive_path))
    else:
        # Ensure extraction directory exists
        os.makedirs(extract_path, exist_ok=True)

    # List to store extracted file paths
    extracted_files = []

    try:
        # Open the tar archive
        with tarfile.open(archive_path, 'r:*') as tar:
            # If specific files are provided, validate they exist in the archive
            if specific_files:
                # Check if all specified files exist in the archive
                archive_members = tar.getnames()
                for file in specific_files:
                    if file not in archive_members:
                        raise ValueError(f"File {file} not found in the archive")
                
                # Extract only specified files
                for member in tar.getmembers():
                    if member.name in specific_files:
                        tar.extract(member, path=extract_path)
                        extracted_files.append(os.path.join(extract_path, member.name))
            else:
                # Extract all files
                tar.extractall(path=extract_path)
                extracted_files = [
                    os.path.join(extract_path, member.name) 
                    for member in tar.getmembers() 
                    if member.isfile()
                ]

    except tarfile.TarError as e:
        raise ValueError(f"Error processing tar archive: {e}")
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to extract files to {extract_path}")

    return extracted_files