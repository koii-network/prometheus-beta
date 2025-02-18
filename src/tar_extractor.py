import os
import tarfile
from typing import Union, List

def extract_tar_archive(tar_path: str, extract_path: Union[str, None] = None) -> List[str]:
    """
    Extract files from a tar archive.

    Args:
        tar_path (str): Path to the tar archive file
        extract_path (str, optional): Destination directory to extract files. 
                                      If None, extracts to the same directory as the tar file.

    Returns:
        List[str]: List of extracted file paths

    Raises:
        FileNotFoundError: If tar file does not exist
        tarfile.TarError: If there are issues with the tar file
    """
    # Validate tar file exists
    if not os.path.exists(tar_path):
        raise FileNotFoundError(f"Tar file not found: {tar_path}")

    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(tar_path)
    
    # Ensure extraction directory exists
    os.makedirs(extract_path, exist_ok=True)

    # List to store extracted file paths
    extracted_files = []

    try:
        # Open the tar file
        with tarfile.open(tar_path, 'r:*') as tar:
            # Extract all members
            tar.extractall(path=extract_path)
            
            # Get full paths of extracted files
            for member in tar.getmembers():
                extracted_file_path = os.path.join(extract_path, member.name)
                if os.path.exists(extracted_file_path):
                    extracted_files.append(extracted_file_path)

    except tarfile.TarError as e:
        raise tarfile.TarError(f"Error extracting tar file: {e}")

    return extracted_files