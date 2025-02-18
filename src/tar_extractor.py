import os
import tarfile

def extract_tar_archive(tar_path, extract_path=None):
    """
    Extract files from a tar archive.
    
    Args:
        tar_path (str): Path to the tar archive file
        extract_path (str, optional): Destination directory for extraction. 
                                      If None, extracts to the same directory as the tar file.
    
    Returns:
        list: List of extracted file paths
    
    Raises:
        FileNotFoundError: If the tar file does not exist
        tarfile.TarError: If there's an error during tar extraction
    """
    # Validate input tar file exists
    if not os.path.exists(tar_path):
        raise FileNotFoundError(f"Tar archive not found: {tar_path}")
    
    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(tar_path)
    
    # Ensure extraction directory exists
    os.makedirs(extract_path, exist_ok=True)
    
    # List to store extracted file paths
    extracted_files = []
    
    # Open and extract the tar archive
    try:
        with tarfile.open(tar_path, 'r:*') as tar:
            # Extract all members
            tar.extractall(path=extract_path)
            
            # Generate full paths for extracted files
            extracted_files = [
                os.path.join(extract_path, member.name) 
                for member in tar.getmembers() 
                if member.isfile()
            ]
    except tarfile.TarError as e:
        raise tarfile.TarError(f"Error extracting tar archive: {e}")
    
    return extracted_files