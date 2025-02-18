import os
import tarfile

def extract_tar_archive(tar_path, extract_path=None):
    """
    Extract files from a tar archive to a specified destination.
    
    Args:
        tar_path (str): Path to the tar archive file
        extract_path (str, optional): Destination directory for extraction. 
                                      If None, extract to the same directory as the tar file.
    
    Returns:
        list: List of extracted file paths
    
    Raises:
        FileNotFoundError: If the tar file does not exist
        tarfile.TarError: If there's an error during tar extraction
    """
    # Validate tar file exists
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
        # Open the tar archive
        with tarfile.open(tar_path, 'r:*') as tar:
            # Extract all files
            tar.extractall(path=extract_path)
            
            # Get the full paths of extracted files
            extracted_files = [
                os.path.join(extract_path, name) 
                for name in tar.getnames()
            ]
        
        return extracted_files
    
    except tarfile.TarError as e:
        raise tarfile.TarError(f"Error extracting tar archive: {e}")