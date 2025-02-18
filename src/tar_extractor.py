import os
import tarfile

def extract_tar_archive(tar_path, extract_path=None):
    """
    Extract files from a tar archive to a specified directory.
    
    Args:
        tar_path (str): Path to the tar archive file
        extract_path (str, optional): Directory to extract files to. 
                                      Defaults to the directory of the tar file.
    
    Returns:
        list: List of extracted file paths
    
    Raises:
        FileNotFoundError: If the tar file does not exist
        tarfile.TarError: If there's an error during tar extraction
    """
    # Validate tar file exists
    if not os.path.exists(tar_path):
        raise FileNotFoundError(f"Tar archive not found: {tar_path}")
    
    # If no extract path is provided, use the tar file's directory
    if extract_path is None:
        extract_path = os.path.dirname(os.path.abspath(tar_path))
    
    # Ensure extract path exists
    os.makedirs(extract_path, exist_ok=True)
    
    # List to store extracted file paths
    extracted_files = []
    
    try:
        # Open the tar file
        with tarfile.open(tar_path, 'r:*') as tar:
            # Extract all members
            tar.extractall(path=extract_path)
            
            # Get list of extracted file paths
            for member in tar.getmembers():
                extracted_file_path = os.path.join(extract_path, member.name)
                extracted_files.append(extracted_file_path)
    
    except tarfile.TarError as e:
        raise tarfile.TarError(f"Error extracting tar archive: {e}")
    
    return extracted_files