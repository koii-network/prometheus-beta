import os
import zipfile

def extract_zip_files(zip_path, extract_path=None):
    """
    Extract all files from a zip archive to a specified directory.
    
    Args:
        zip_path (str): Path to the zip file to be extracted.
        extract_path (str, optional): Directory to extract files to. 
                                      If None, extracts to the zip file's directory.
    
    Returns:
        list: List of paths to extracted files.
    
    Raises:
        FileNotFoundError: If the zip file does not exist.
        ValueError: If the zip_path is not a valid zip file.
    """
    # Validate input
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Zip file not found: {zip_path}")
    
    if not zipfile.is_zipfile(zip_path):
        raise ValueError(f"Not a valid zip file: {zip_path}")
    
    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(zip_path)
    
    # Ensure extraction path exists
    os.makedirs(extract_path, exist_ok=True)
    
    # Extract files
    extracted_files = []
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
        extracted_files = [os.path.join(extract_path, name) for name in zip_ref.namelist()]
    
    return extracted_files