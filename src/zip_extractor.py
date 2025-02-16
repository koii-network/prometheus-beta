import os
import zipfile

def extract_zip_archive(zip_path, extract_path=None):
    """
    Extract all files from a zip archive.
    
    Args:
        zip_path (str): Path to the zip file to extract
        extract_path (str, optional): Destination path for extraction. 
                                      If None, extract to the same directory as the zip file.
    
    Returns:
        list: List of extracted file paths
    
    Raises:
        FileNotFoundError: If the zip file does not exist
        zipfile.BadZipFile: If the zip file is corrupt
        PermissionError: If there are permission issues during extraction
    """
    # Validate zip file exists
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Zip file not found: {zip_path}")
    
    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(zip_path)
    
    # Ensure extraction path exists
    os.makedirs(extract_path, exist_ok=True)
    
    # List to store extracted file paths
    extracted_files = []
    
    # Extract zip contents
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract all files
        zip_ref.extractall(path=extract_path)
        
        # Build list of full paths for extracted files
        for file_info in zip_ref.infolist():
            extracted_path = os.path.join(extract_path, file_info.filename)
            extracted_files.append(extracted_path)
    
    return extracted_files