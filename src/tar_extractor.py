import os
import tarfile

def extract_tar_archive(tar_path, extract_path=None):
    """
    Extract files from a tar archive.
    
    Args:
        tar_path (str): Path to the tar archive file.
        extract_path (str, optional): Directory to extract files to. 
                                      Defaults to the same directory as the tar file.
    
    Raises:
        FileNotFoundError: If the tar file does not exist.
        ValueError: If the tar path is not a .tar, .tar.gz, or .tgz file.
        PermissionError: If there are permission issues during extraction.
    
    Returns:
        list: List of extracted file paths.
    """
    # Validate tar file extension
    valid_extensions = ['.tar', '.tar.gz', '.tgz']
    if not any(tar_path.endswith(ext) for ext in valid_extensions):
        raise ValueError(f"Invalid tar file extension. Supported extensions: {', '.join(valid_extensions)}")
    
    # Check if tar file exists
    if not os.path.exists(tar_path):
        raise FileNotFoundError(f"Tar file not found: {tar_path}")
    
    # Set extract path to tar file directory if not specified
    if extract_path is None:
        extract_path = os.path.dirname(tar_path) or '.'
    
    # Ensure extract path exists
    os.makedirs(extract_path, exist_ok=True)
    
    # List to store extracted file paths
    extracted_files = []
    
    try:
        # Open the tar file
        with tarfile.open(tar_path, 'r:*') as tar:
            # Extract all members
            tar.extractall(path=extract_path)
            
            # Get full paths of extracted files
            extracted_files = [
                os.path.join(extract_path, name) 
                for name in tar.getnames()
            ]
    
    except PermissionError:
        raise PermissionError(f"Permission denied when extracting to {extract_path}")
    except tarfile.TarError as e:
        raise ValueError(f"Error extracting tar file: {e}")
    
    return extracted_files