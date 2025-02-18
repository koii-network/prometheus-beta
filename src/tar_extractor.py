import os
import tarfile
from typing import Union, List

def extract_tar_archive(tar_path: str, extract_path: Union[str, None] = None) -> List[str]:
    """
    Extract files from a tar archive.
    
    Args:
        tar_path (str): Path to the tar archive file
        extract_path (str, optional): Directory to extract files to. 
                                      If None, extracts to the tar file's directory.
    
    Returns:
        List[str]: List of extracted file paths
    
    Raises:
        FileNotFoundError: If the tar file does not exist
        ValueError: If tar_path is not a valid tar archive
        PermissionError: If there are permission issues during extraction
    """
    # Validate input
    if not os.path.exists(tar_path):
        raise FileNotFoundError(f"Tar archive not found: {tar_path}")
    
    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(tar_path)
    
    # Ensure extraction path exists
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
                # Construct full path of extracted file
                full_path = os.path.normpath(os.path.join(extract_path, member.name))
                
                # Only add files (not directories) to the list
                if os.path.isfile(full_path):
                    extracted_files.append(full_path)
    
    except tarfile.TarError as e:
        raise ValueError(f"Invalid tar archive: {e}")
    except PermissionError:
        raise PermissionError(f"Permission denied when extracting to {extract_path}")
    
    return extracted_files