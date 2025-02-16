import os
import tarfile

def extract_tar_archive(archive_path, extract_path=None):
    """
    Extract files from a tar archive to a specified directory.
    
    Args:
        archive_path (str): Path to the tar archive file.
        extract_path (str, optional): Directory to extract files to. 
                                      Defaults to the archive's directory if not specified.
    
    Returns:
        list: List of extracted file paths.
    
    Raises:
        FileNotFoundError: If the archive file does not exist.
        ValueError: If the archive path is invalid or not a .tar file.
        tarfile.TarError: For other tar-related extraction errors.
    """
    # Validate archive path
    if not os.path.exists(archive_path):
        raise FileNotFoundError(f"Archive file not found: {archive_path}")
    
    # Validate file extension
    if not archive_path.lower().endswith(('.tar', '.tar.gz', '.tgz')):
        raise ValueError(f"Invalid tar archive format: {archive_path}")
    
    # Set default extract path if not provided
    if extract_path is None:
        extract_path = os.path.dirname(os.path.abspath(archive_path))
    
    # Ensure extract path exists
    os.makedirs(extract_path, exist_ok=True)
    
    # Extract files
    extracted_files = []
    try:
        with tarfile.open(archive_path, 'r:*') as tar:
            tar.extractall(path=extract_path)
            extracted_files = [os.path.join(extract_path, name) for name in tar.getnames()]
    except tarfile.TarError as e:
        raise tarfile.TarError(f"Error extracting tar archive: {e}")
    
    return extracted_files