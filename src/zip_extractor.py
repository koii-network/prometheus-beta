import os
import zipfile


def extract_zip_files(zip_path, extract_path=None):
    """
    Extract all files from a zip archive to a specified directory.

    Args:
        zip_path (str): Path to the zip file to be extracted.
        extract_path (str, optional): Directory to extract files to. 
                                      Defaults to the zip file's directory.

    Returns:
        list: A list of full paths to the extracted files.

    Raises:
        FileNotFoundError: If the zip file does not exist.
        ValueError: If the zip_path is not a valid zip file.
        PermissionError: If there are permission issues during extraction.
    """
    # Validate input
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"Zip file not found: {zip_path}")
    
    # Validate zip file
    if not zipfile.is_zipfile(zip_path):
        raise ValueError(f"Not a valid zip file: {zip_path}")
    
    # Determine extraction path
    if extract_path is None:
        extract_path = os.path.dirname(os.path.abspath(zip_path))
    
    # Ensure extraction directory exists
    os.makedirs(extract_path, exist_ok=True)
    
    # List to store extracted file paths
    extracted_files = []
    
    try:
        # Open and extract the zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Extract all files
            for file_info in zip_ref.infolist():
                # Extract the file
                extracted_file_path = zip_ref.extract(file_info, path=extract_path)
                extracted_files.append(os.path.abspath(extracted_file_path))
    
    except PermissionError:
        raise PermissionError(f"Permission denied when extracting to {extract_path}")
    
    return extracted_files